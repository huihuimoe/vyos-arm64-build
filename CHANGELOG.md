## vyos-1x
- configverify: T8413: fix issue in duplex shaping (redirect to input interface)
   - PR: vyos/vyos-1x#5073
- dhcpv6: T8414: missing prefix-delegation interface constraint
   - PR: vyos/vyos-1x#5076
- validators: T8384: ipv6-eui64-prefix: unhandled exception on eui-64 address validation
   - PR: vyos/vyos-1x#5070
- T8399: dhcpv6-server: move connectivity/overlap checks inside subnet loop
   - PR: vyos/vyos-1x#5062
- T8418: adjust permissions setting of config.boot for case of cloud-init
   - PR: vyos/vyos-1x#5079
- login: T8415: show Warning() if default password is used when adding user
   - PR: vyos/vyos-1x#5077
- T8188: Preserve static IPv4 addresses flushed by dhclient
   - PR: vyos/vyos-1x#4968
- vpp: T8355: Set MTU for vpp interfaces
   - PR: vyos/vyos-1x#5039
- T8405: fix noipv6 emitted when dhcpv6-options configured without ipv6 node
   - PR: vyos/vyos-1x#5071
- T8405: fix pppoe peer template - remove superfluous +
   - PR: vyos/vyos-1x#5084
- firewall: T8277: Resolve migration issue when using  with protocol 
   - PR: vyos/vyos-1x#5087
- vpp: T8422: Resolve inconsistent behavior with  configuration option
   - PR: vyos/vyos-1x#5085
- T8410: Fix typos and mistakes for operational and configuration commands
   - PR: vyos/vyos-1x#5082
- T8379: PBR commit fail with traceback if non-existing VRF added
   - PR: vyos/vyos-1x#5078
- vpp: T8432: Fix AttributeError for enabling vpp interface
   - PR: vyos/vyos-1x#5088
- vpp: T8286: Uninitialized interfaces raise errors when added to VPP
   - PR: vyos/vyos-1x#5069
- vpp: T8416: Prevent interfaces from being assigned to xconnect and bridge/bonding at the same time
   - PR: vyos/vyos-1x#5080
- T8404: pppoe: fix TypeError when ipv6 address node exists without autoconf
   - PR: vyos/vyos-1x#5067
- pseudo-ethernet: T8434: source-interface does not show bridge or bond interfaces
   - PR: vyos/vyos-1x#5090


## vyos-build
- T8273: FRR ospfv3: fix LSA when no new BDR elected + remove already merged patch
   - PR: vyos/vyos-build#1145
- kea: T8424: Update Kea to 3.0.3
   - PR: vyos/vyos-build#1147
- Kernel: T8427: Update Linux Kernel to 6.6.130
   - PR: vyos/vyos-build#1148
- T8410: Fix typos and mistakes in scripts and comments
   - PR: vyos/vyos-build#1146


