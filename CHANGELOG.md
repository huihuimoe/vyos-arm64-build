## vyos-1x
- smoketest: T9622: verify PIDs of all FRR daemons after every test
   - PR: vyos/vyos-1x#5652
- T9662: raise ConfigError if TACACS is configured without a server
   - PR: vyos/vyos-1x#5667
- T9605: system-option: do not fail commits on dynamic debug writes
   - PR: vyos/vyos-1x#5660
- T9621: Fix firewall negated time weekdays
   - PR: vyos/vyos-1x#5657
- conf-mode: T9672: add missing f-string prefixes to error messages
   - PR: vyos/vyos-1x#5675
- configd: T9515: render FRR unless a routing script failed
   - PR: vyos/vyos-1x#5635
- dhcp-server: T9674: enforce Kea data directory ownership on every commit
   - PR: vyos/vyos-1x#5677
- T9508: add support for completion of values of reference tree paths
   - PR: vyos/vyos-1x#5592
- op-mode: T9667: raise an error for an unknown protocol in reset vpn
   - PR: vyos/vyos-1x#5671
- wan-load-balancing: T9671: show the warning for an empty firewall group
   - PR: vyos/vyos-1x#5674
- remote: T9619: Fix commit-archive in a VRF for non-root users
   - PR: vyos/vyos-1x#5656
- tech-support: T9654: Enhance archive security by permissions
   - PR: vyos/vyos-1x#5668
- firewall: T9463: fix migration repointing rules at the wrong group
   - PR: vyos/vyos-1x#5559
- vpp: T9524: Fix VPP restart after a crash
   - PR: vyos/vyos-1x#5669
- dhcpv6: T9689: accept static mappings without address or prefix
   - PR: vyos/vyos-1x#5682
- vyos-netlinkd: T9675: fix DHCPv6-PD loss after a short carrier drop
   - PR: vyos/vyos-1x#5681
- T7634: openvpn: create the interface before starting the daemon
   - PR: vyos/vyos-1x#5680


## vyos-build
- frr: T9622: fix nhrpd use-after-free on GRE tunnel deletion
   - PR: vyos/vyos-build#1357
- Kernel: T9682: Update Linux Kernel to 6.18.65
   - PR: vyos/vyos-build#1373
- Kernel: T9682: perf jitdump: include linux/string.h for strlcpy()
   - PR: vyos/vyos-build#1374
- T9483: frr: enhance performance of clear bgp
   - PR: vyos/vyos-build#1372
- T9705: frr: backport small bgpd fixes
   - PR: vyos/vyos-build#1379
- T9711: Modify PR rules to allow the revert operation label
   - PR: vyos/vyos-build#1378
- T9211: Update accel-ppp-ng version to 0b30c7b
   - PR: vyos/vyos-build#1376
- accel-ppp-ng: T7935: link against VPP packages from the APT repository
   - PR: vyos/vyos-build#1377
- netavark: T9680: nft: only skip ct invalid drop rule if it exists for this bridge
   - PR: vyos/vyos-build#1380


