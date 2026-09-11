## vyos-1x
- sysctl: T9283: stop low-level Kernel messages on the console
   - PR: vyos/vyos-1x#5447
- update-checker: T8497: fix command injection via crafted update server response
   - PR: vyos/vyos-1x#5450
- static: T9278: reconcile FRR config after every DHCP lease event
   - PR: vyos/vyos-1x#5446
- T9279: VPP extend num-rx and tx ring descriptiors to 32768
   - PR: vyos/vyos-1x#5448


## vyos-build
- Testsuite: T9276: RAID1 test sporadically fails due to timeout violation
   - PR: vyos/vyos-build#1290
- image: T9283: clean up warnings and errors during ISO build
   - PR: vyos/vyos-build#1292
- oci: T9269: mask systemd services for container startup and add healthcheck
   - PR: vyos/vyos-build#1289
- Kernel: T9283: run Accel-PPP depmod for the target Kernel version
   - PR: vyos/vyos-build#1293
- T9286: Update accel-ppp-ng to the 8cb6287 version multiple security fixes
   - PR: vyos/vyos-build#1294
- T9014: install flavor.json before Debian packages are installed
   - PR: vyos/vyos-build#1295
- Kernel: T9287: Update Linux Kernel to 6.18.50
   - PR: vyos/vyos-build#1297
- T9269: add OCI container image test
   - PR: vyos/vyos-build#1296
- live-boot: T5475: replace the forked live-boot package with Debian's
   - PR: vyos/vyos-build#1288
- T9245: podman: add libsystemd-dev to enable automatic health checks
   - PR: vyos/vyos-build#1278
- Kernel: T9298: make linux-firmware package architecture aware
   - PR: vyos/vyos-build#1299


