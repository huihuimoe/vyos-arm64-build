## vyos-1x
- openvpn: T9334: stop rendering "keepalive 0 0"
   - PR: vyos/vyos-1x#5488
- smoketest: T9316: match VRF process names by prefix, not equality
   - PR: vyos/vyos-1x#5490
- journald: T9183: stop forwarding journal entries to syslog
   - PR: vyos/vyos-1x#5486
- configtree: T9307: serialize libvyosconfig calls across threads
   - PR: vyos/vyos-1x#5466
- wwan: T9326: fix dual-stack connect on single-PDN-context networks
   - PR: vyos/vyos-1x#5482
- ipsec: T9320: Add deprecation warning for IKEv1 key-exchange
   - PR: vyos/vyos-1x#5485
- frr: T9344: remove dead code path when vyos-configd is not running
   - PR: vyos/vyos-1x#5492
- vxlan: T9319: add VXLAN-GBP support
   - PR: vyos/vyos-1x#5484
- dhcpv6-client: T9349: do not start dhcp6c in debug mode
   - PR: vyos/vyos-1x#5498
- bgp: T9345: restore named-VRF AFI validation
   - PR: vyos/vyos-1x#5494


## vyos-build
- vbash: T7575: Resolve completion on root-level op-mode
   - PR: vyos/vyos-build#1308
- journald: T9183: delete chroot include config file - use proper systemd override
   - PR: vyos/vyos-build#1309
- T5498: Add script to run e2fsck -p to initramfs-tools
   - PR: vyos/vyos-build#1283


