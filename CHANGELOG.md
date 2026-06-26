## vyos-1x
- config: T8858: fix mutable default argument in config API methods
   - PR: vyos/vyos-1x#5075
- vpp: T8603: Expand ACL support to logical interfaces
   - PR: vyos/vyos-1x#5280
- qos: T7965:  Fix qos fails to reapply on dynamic interfaces after reconnection
   - PR: vyos/vyos-1x#5220
- pseudo-ethernet: T8540: Add anycast-gateway support for EVPN
   - PR: vyos/vyos-1x#5156
- T8990: bgp: fix VPNv4/VPNv6 leaked routes flapping on every commit
   - PR: vyos/vyos-1x#5287
- vpp: T8913: Skip bond teardown for non-structural config changes
   - PR: vyos/vyos-1x#5252
- T9009: op-mode: extend "monitor log" with filter level
   - PR: vyos/vyos-1x#5288
- haproxy: T8931: Improve WebSocket support for HAProxy
   - PR: vyos/vyos-1x#5226
- openvpn: T8998: fix ccd-exclusive without client-config-dir
   - PR: vyos/vyos-1x#5283
- T8099: strongswan: 6.0.6 + Post quantum options
   - PR: vyos/vyos-1x#5267
- ipsec: T8975: lock vti-up-down state DB to prevent lost updates under concurrent rekey
   - PR: vyos/vyos-1x#5264
- geoip: T5746: Add GeoIP ASN support
   - PR: vyos/vyos-1x#5155
- T8993: initialize ReferenceTree module from string not file
   - PR: vyos/vyos-1x#5291
- T9015: fix thread safety of configtree read/write_cache
   - PR: vyos/vyos-1x#5294
- bgp: T9013: Add BMP source-interface support
   - PR: vyos/vyos-1x#5290
- T9019: Update GitHub PR templates with AI tool usage policy
   - PR: vyos/vyos-1x#5292
- T8097: strongswan: add CLI for ESN
   - PR: vyos/vyos-1x#5284
- bgp: T5526: Fix BGP neighbor validation not raising when interface does not exist
   - PR: vyos/vyos-1x#5272
- T9011: enable proxy_ndp sysctl for static IPv6 neighbor proxy
   - PR: vyos/vyos-1x#5289


## vyos-build
- T8099: Update strongswan to 6.0.6
   - PR: vyos/vyos-build#1222
- T8599: Make source packages required and fix them
   - PR: vyos/vyos-build#1175
- T9010: Update Linux Kernel to 6.18.36 and re-fresh Intel OOT driver versions
   - PR: vyos/vyos-build#1224
- T9013: Add FRR patch to fix BMP connect source-interface deletion
   - PR: vyos/vyos-build#1225


