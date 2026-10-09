## vyos-1x
- T9365: add bindings for reference tree path from config path util
   - PR: vyos/vyos-1x#5513
- policy: T9379: prefix-list duplicate check in linear time
   - PR: vyos/vyos-1x#5525
- webproxy: T9371: fix typo in the squidGuard local-block-url rule ACL
   - PR: vyos/vyos-1x#5522
- pppoe: T9395: render default routes via FRR only
   - PR: vyos/vyos-1x#5532
- frrender: T9377: do not save the FRR configuration a second time
   - PR: vyos/vyos-1x#5524
- config-mgmt: T9399: read the committed config once in the post-commit hooks
   - PR: vyos/vyos-1x#5533
- op-mode: T861: add "show secure-boot detail" command
   - PR: vyos/vyos-1x#5537
- agents: T9348: update content in AGENTS.md to improve AI generated changes
   - PR: vyos/vyos-1x#5497
- T9351: Accel-PPP-NG: Add CLI support for Message Authenticator attribute in Access packets (Blast-RADIUS mitigation)
   - PR: vyos/vyos-1x#5442
- bgp: T9404: do not render "bgp default local-preference" when the value is 100
   - PR: vyos/vyos-1x#5536
- bgp: T9407: do not render "bgp reject-as-sets" when it is the FRR default
   - PR: vyos/vyos-1x#5538
- openvpn: T9370: add chacha20poly1305 data cipher
   - PR: vyos/vyos-1x#5523
- router-advert: T9413: add no-remove-on-exit and no-flush-* options
   - PR: vyos/vyos-1x#5541
- bgp: T9410: add route-map vrf import under ipv6-unicast
   - PR: vyos/vyos-1x#5540
- configd: T9368: reconcile FRR after a DHCP lease without the commit socket
   - PR: vyos/vyos-1x#5520


## vyos-build
- T9392: Keep kernel objects and don't create source tarball by default
   - PR: vyos/vyos-build#1316
- Kernel: T9385: Update Linux Kernel to 6.18.55
   - PR: vyos/vyos-build#1317
- Testsuite: T861: boot VyOS CA signed images as-is in Secure Boot test
   - PR: vyos/vyos-build#1320
- smoketest: T9402: stop navigating the installed system's GRUB menu
   - PR: vyos/vyos-build#1319
- agents: T9348: update content in AGENTS.md to improve AI generated changes
   - PR: vyos/vyos-build#1310
- T9400: Fix APT repository key for Debian Trixie release
   - PR: vyos/vyos-build#1318
- T9409: Bump accel-ppp-ng version to dd07b23
   - PR: vyos/vyos-build#1321


