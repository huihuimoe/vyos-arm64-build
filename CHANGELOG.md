## vyos-1x
- https: T9559: fix bogus port conflict with "vrf default"
   - PR: vyos/vyos-1x#5631
- tunnel: T9193: honor remote and source-interface in GRE key uniqueness check
   - PR: vyos/vyos-1x#5392
- utils: T9322: validate the address is_intf_addr_assigned() is given
   - PR: vyos/vyos-1x#5477
- nhrp: T9585: Fix verify() never validating NHRP tunnels
   - PR: vyos/vyos-1x#5633
- http-api: T9588: Keep config strings out of world-readable /tmp
   - PR: vyos/vyos-1x#5634
- T9582: Fix OpenConnect RADIUS accounting server missing from radius_servers
   - PR: vyos/vyos-1x#5632
- telegraf: T9569: Pass InfluxDB token via a root-only environment file
   - PR: vyos/vyos-1x#5629
- wwan: T9388: apply a static bearer's address/gateway/DNS directly instead of DHCP(v6)/SLAAC
   - PR: vyos/vyos-1x#5526
- debian: T9587: restore SUID bit on vyos-op-run
   - PR: vyos/vyos-1x#5638
- telegraf: T9601: Pass Azure Data Explorer credentials via the environment file
   - PR: vyos/vyos-1x#5640
- T9590: fix order of set perms/ownership and first write in utils write_file
   - PR: vyos/vyos-1x#5636
- T9607: Synchronize the list of branches across all scripts
   - PR: vyos/vyos-1x#5644


## vyos-build
- github: T9579: trigger wide-dhcpv6 build from its own path filter
   - PR: vyos/vyos-build#1345
- Kernel: T9591: add VyOS internal revision to the kernel release string
   - PR: vyos/vyos-build#1347
- Kernel: T9598: Update Linux Kernel to 6.18.62
   - PR: vyos/vyos-build#1349
- smoketest: T9402: more robust GRUB menu selection
   - PR: vyos/vyos-build#1333
- T9609: openssl: bump to 3.0.22-1~deb12u2
   - PR: vyos/vyos-build#1352
- pdns-recursor: T9608: use a VyOS version suffix for the rebuild
   - PR: vyos/vyos-build#1351
- T9607: Synchronize the list of branches across all scripts [vyos-build]
   - PR: vyos/vyos-build#1354
- Kernel: T9595: replace deprecated MLNX_OFED with DOCA-OFED
   - PR: vyos/vyos-build#1348
- frr: T9451: Remove extra processing on router bgp
   - PR: vyos/vyos-build#1353
- Kernel: T9580: unify kexec/kdump and PPP options in common config fragments
   - PR: vyos/vyos-build#1346
- frr: T9606: update commit hash which includes ospf_auth_check_md5_digest fix
   - PR: vyos/vyos-build#1355


