"""Exercise the patched upstream hook with a real ARM64 kernel and test keys.

Requires openssl, sbsign, sbverify, patch; set VYOS_BUILD_DIR to an upstream
checkout and ARM64_KERNEL_IMAGE to the packaged gzip-compressed vmlinuz.
Run: python3 -m unittest discover -s tests -v
"""
import gzip
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
UPSTREAM = os.environ.get('VYOS_BUILD_DIR')
KERNEL = os.environ.get('ARM64_KERNEL_IMAGE')
HOOK = 'data/live-build-config/hooks/live/93-sb-sign-kernel.chroot'


@unittest.skipUnless(UPSTREAM and KERNEL, 'Set VYOS_BUILD_DIR and ARM64_KERNEL_IMAGE')
class KernelSigningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for tool in ('openssl', 'sbsign', 'sbverify', 'patch'):
            if not shutil.which(tool):
                raise RuntimeError(f'Missing required tool: {tool}')
        cls.assets = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.assets.cleanup)
        cls.assets_path = Path(cls.assets.name)
        for name in ('test', 'other'):
            subprocess.run([
                'openssl', 'req', '-new', '-x509', '-newkey', 'rsa:2048', '-nodes',
                '-keyout', str(cls.assets_path / f'{name}.key'),
                '-out', str(cls.assets_path / f'{name}.pem'),
                '-days', '1', '-subj', f'/CN={name}',
            ], check=True, capture_output=True)

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        hook = self.root / HOOK
        hook.parent.mkdir(parents=True)
        shutil.copyfile(Path(UPSTREAM) / HOOK, hook)
        with (REPO / 'data/vyos-build-007-arm64_kernel_sign.patch').open() as patch:
            subprocess.run(['patch', '--batch', '-p1', '-d', str(self.root)],
                           stdin=patch, check=True, capture_output=True)
        # Keep the real signing hook and tools; redirect only filesystem roots
        # and replace package removal / architecture / date with sandbox stubs.
        source = hook.read_text()
        for path in ('/boot/', '/var/lib/shim-signed/mok/', '/lib/modules', '/usr/lib', '/etc/'):
            source = source.replace(path, str(self.root) + path)
        hook.write_text(source)
        self.hook = hook
        for path in ('boot', 'var/lib/shim-signed/mok', 'lib/modules', 'usr/lib',
                     'etc', 'bin', 'data/mok', 'vyos-build/data/certificates'):
            (self.root / path).mkdir(parents=True, exist_ok=True)
        for name, body in {'apt-get': 'exit 0', 'dpkg': 'echo arm64', 'date': 'echo 2031'}.items():
            stub = self.root / 'bin' / name
            stub.write_text('#!/bin/sh\n' + body + '\n')
            stub.chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.root / 'bin') + ':' + os.environ['PATH'])
        self.image = self.root / 'boot/kernel'
        shutil.copyfile(KERNEL, self.image)
        (self.root / 'boot/vmlinuz').symlink_to('kernel')
        self.mok = self.root / 'var/lib/shim-signed/mok'
        self.key = self.mok / 'vyos-dev-2031-linux.key'
        self.cert = self.mok / 'vyos-dev-2031-linux.pem'

    def prepare_keys(self):
        shutil.copyfile(self.assets_path / 'test.key', self.root / 'data/mok/MOK.key')
        shutil.copyfile(self.assets_path / 'test.pem', self.root / 'data/mok/MOK.pem')
        workflow = (REPO / '.github/workflows/auto-build.yml').read_text()
        start = workflow.index('          if [ -f data/mok/MOK.key ]; then')
        end = workflow.index('          fi', start) + len('          fi')
        subprocess.run(['bash', '-eu', '-c', workflow[start:end]],
                       cwd=self.root, env=self.env, check=True)
        for file in (self.root / 'vyos-build/data/certificates').iterdir():
            shutil.copyfile(file, self.mok / file.name)
        self.assertTrue(self.key.exists(), 'Workflow must use the hook\'s current year')
        self.assertEqual((self.root / 'vyos-build/data/certificates' / self.key.name).stat().st_mode & 0o777, 0o600)

    def run_hook(self):
        return subprocess.run(['sh', str(self.hook)], env=self.env,
                              capture_output=True, text=True)

    def assert_signed(self):
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        verified = subprocess.run(['sbverify', '--cert', str(self.cert), str(self.image)],
                                  capture_output=True, text=True)
        self.assertEqual(verified.returncode, 0, verified.stdout + verified.stderr)
        self.assertFalse(self.key.exists())
        self.assertFalse(self.image.with_suffix('.tmp').exists())

    def test_packaged_gzip_kernel_is_signed_and_private_key_removed(self):
        self.prepare_keys()
        self.assert_signed()

    def test_uncompressed_kernel_is_signed(self):
        self.image.write_bytes(gzip.decompress(self.image.read_bytes()))
        self.prepare_keys()
        self.assert_signed()

    def test_no_key_preserves_original_compressed_image(self):
        original = self.image.read_bytes()
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.image.read_bytes(), original)

    def test_mismatched_certificate_fails_and_removes_key_and_temporary_image(self):
        self.prepare_keys()
        shutil.copyfile(self.assets_path / 'other.pem', self.cert)
        result = self.run_hook()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Signing of Linux Kernel failed', result.stdout)
        self.assertFalse(self.key.exists())
        self.assertFalse(self.image.with_suffix('.tmp').exists())

    def test_verification_failure_removes_key_and_temporary_image(self):
        self.prepare_keys()
        verifier = shutil.which('sbverify')
        wrapper = self.root / 'bin/sbverify'
        wrapper.write_text(f'#!/bin/sh\nexec "{verifier}" --cert "{self.assets_path / "other.pem"}" "$3"\n')
        wrapper.chmod(0o755)
        result = self.run_hook()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Signature verification failed', result.stdout)
        self.assertFalse(self.key.exists())
        self.assertFalse(self.image.with_suffix('.tmp').exists())

    def test_invalid_image_fails_signing_and_removes_key(self):
        self.prepare_keys()
        self.image.write_bytes(b'invalid kernel')
        result = self.run_hook()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Signing of Linux Kernel failed', result.stdout)
        self.assertFalse(self.key.exists())


if __name__ == '__main__':
    unittest.main()
