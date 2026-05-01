## vyos-1x
- VPP: T8495: fix issue with assigning  acl on sub interfaces
   - PR: vyos/vyos-1x#5129
- vpp: T8460: Use isolated cpus for VPP cpu-cores
   - PR: vyos/vyos-1x#5130
- T8535: Remove next-hop-self for BGP link state
   - PR: vyos/vyos-1x#5144
- T8293: Add ability to set timeout for high-availability health-check
   - PR: vyos/vyos-1x#5151
- utils: T8541: add write-config-file-value helper
   - PR: vyos/vyos-1x#5146
- kea: T8586: Skip static mappings without match criteria
   - PR: vyos/vyos-1x#5153
- op-mode: T8305: Fix completion for "show isis neighbor <system-id>" command
   - PR: vyos/vyos-1x#5143
- T8531: add Mergify config with commands restrictions
   - PR: vyos/vyos-1x#5145
- bgp: T8589: Add ead, es and [1-5] to route-map match evpn route-type
   - PR: vyos/vyos-1x#5150
- T8587: fix XML data type from u32 to u64 where range exceeds uint32 max
   - PR: vyos/vyos-1x#5148
- T8539: Unable to traceroute using hostname and ipv6 source address
   - PR: vyos/vyos-1x#5140
- T6750: sr-te: Adding initial Segment Routing Traffic Engineering portion of FRR
   - PR: vyos/vyos-1x#4994
- migration: T8280: Fix auth file read for interfaces on first boot of new image
   - PR: vyos/vyos-1x#5152


## vyos-build
- linux-kernel: T8496: Add kernel config needed for PWRU
   - PR: vyos/vyos-build#1170
- hooks: T8541: inject flavor serial console settings once into config.boot.default
   - PR: vyos/vyos-build#1167
- T8531: restrict Mergify commands to maintainers team
   - PR: vyos/vyos-build#1166
- T8597: Use specific version of kea-packaging repo in build scripts
   - PR: vyos/vyos-build#1173
- Kernel: T861: add custom VyOS CA to Kernel builds for later module signing
   - PR: vyos/vyos-build#1171
- T8636: add FRR patches that fix pathd no cmds
   - PR: vyos/vyos-build#1174
- linux-kernel: T8506: Use scripts/kconfig/merge_config.sh for merging kernel config fragments
   - PR: vyos/vyos-build#1169


