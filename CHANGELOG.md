## vyos-1x
- wireless: T6513: rename "security wpa passphrase" to "security wpa password"
   - PR: vyos/vyos-1x#5651
- http-api: T9631: use constant-time comparison of keys
   - PR: vyos/vyos-1x#5655
- policy: T9617: keep VRF protocol dictionaries out of the name-keyed traversal
   - PR: vyos/vyos-1x#5649
- image: T9635: honor kdump memory default when upgrading the system image
   - PR: vyos/vyos-1x#5658
- T8958: add support for optional diff calculation of comments
   - PR: vyos/vyos-1x#5645


## vyos-build
- frr: T9620: make patch failures build failures
   - PR: vyos/vyos-build#1356
- Kernel: T9598: Update Linux Kernel to 6.18.63
   - PR: vyos/vyos-build#1358
- Kernel: T9628: Update Linux Kernel to 6.18.64
   - PR: vyos/vyos-build#1360
- T9627: Update frr_exporter version to v1.12.0 for OSPF metrics
   - PR: vyos/vyos-build#1359
- container: T9626: remove VyOS Kernel modules from the OCI image
   - PR: vyos/vyos-build#1361
- smoketest: T9634: boot into upgraded image in image update test
   - PR: vyos/vyos-build#1363


