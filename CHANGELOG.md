## vyos-1x
- T8976: explicitly remove 'kernel' entry in ttyS0 device setting on choice of 'tty' during image install
   - PR: vyos/vyos-1x#5265
- dhcpv6: T8953: Add validation for duplicate static-mapping address and prefix
   - PR: vyos/vyos-1x#5269
- T8980: update config sync diff for exclude mask
   - PR: vyos/vyos-1x#5271
- pki: T8165: Add ability to show certificate full chain in pem format
   - PR: vyos/vyos-1x#5225
- VPP: T8972: Fix VPP/LCP VRF table synchronization for VPP-managed Ethernet interfaces and Ethernet VIFs.
   - PR: vyos/vyos-1x#5261
- T8923: normalize "can not" to "cannot" and other typo fixes
   - PR: vyos/vyos-1x#5277
- bgp: T8223: Prevent  in multiple BGP VRF instances simultaneously
   - PR: vyos/vyos-1x#5231
- firewall: T8991: Fix IndexError with domain resolver mishandling blank lines
   - PR: vyos/vyos-1x#5278
- vpp: T8979: Fix defunct interface retaining IP addresses after crash
   - PR: vyos/vyos-1x#5281
- pki: T8994: add graceful error handling in case certbot fails
   - PR: vyos/vyos-1x#5276
- password-reset: T8985: Fix unbounded  ranges corrupting other user blocks
   - PR: vyos/vyos-1x#5273
- T8971: upgrade from bgpq3 package to bgpq4
   - PR: vyos/vyos-1x#5270
- T8881: dns: expose PowerDNS recursor cache tuning options
   - PR: vyos/vyos-1x#5209
- firewall: T8546: Fix conntrack_required for global state-policy
   - PR: vyos/vyos-1x#5279
- dhcp-server: T8524: Validate DDNS key-name references defined tsig-key
   - PR: vyos/vyos-1x#5256
- dhcp: T8941: Support filter and sorting combination on DHCPv4/v6 server lease entries in op mode
   - PR: vyos/vyos-1x#5237


## vyos-build
- T861: add secure boot support
   - PR: vyos/vyos-build#1223
- geoip: T5746: Download ASN database
   - PR: vyos/vyos-build#1215


