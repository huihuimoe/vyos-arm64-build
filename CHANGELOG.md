## vyos-1x
- geoip: T8987: Support updates via source-address/vrf
   - PR: vyos/vyos-1x#5282
- bgp: T8865: Reject  sub-block in VRF l2vpn-evpn when  is globally active
   - PR: vyos/vyos-1x#5297
- utils: T9003: add list-argument variant of cmd() for safer subprocess execution
   - PR: vyos/vyos-1x#5285
- ci: T8490: fix typos in comments, strings, and local identifiers
   - PR: vyos/vyos-1x#5298
- ci: T8490: drop legacy per-repo typos caller (now org-ruleset)
   - PR: vyos/vyos-1x#5302
- bgp: T6573: add input/output queue limit CLI commands 
   - PR: vyos/vyos-1x#5295
- https: T9022: serve the full CA certificate chain
   - PR: vyos/vyos-1x#5296
- ifconfig: T9008: refactor vyos.ifconfig to use cmdl() for safer subprocess execution
   - PR: vyos/vyos-1x#5286
- T9031: Fix updating pppoe server protocols
   - PR: vyos/vyos-1x#5303
- T8963: policy-route: trigger domain resolver for domain groups
   - PR: vyos/vyos-1x#5254
- vyos.utils: T8981: catch_broken_pipe() decorator must return func(*args, **kwargs)
   - PR: vyos/vyos-1x#5304
-  T9028: add .claude folder to .gitignore
   - PR: vyos/vyos-1x#5301
- op-mode: T8372: add "show log facility <name>" command
   - PR: vyos/vyos-1x#5300
- firewall: T8761: Reintroduce VRF-interface names in generated config
   - PR: vyos/vyos-1x#5167
- op-mode: T9009: add "show log priority <level>" command
   - PR: vyos/vyos-1x#5299


## vyos-build
- Kernel: T8605: net/l2tp: allow unmanaged tunnel setup without route to peer
   - PR: vyos/vyos-build#1189
- Kernel: T8914: add support for 2.5G pluggables on BCM57810S
   - PR: vyos/vyos-build#1227
- ci: T8490: fix typo in grub live-theme (icon_heigh -> icon_height)
   - PR: vyos/vyos-build#1229
- T9029: Switch default branch for CI workflows
   - PR: vyos/vyos-build#1231
- T9028: add .claude folder to .gitignore
   - PR: vyos/vyos-build#1230
- podman: T9024: package upgrade from v4.9.5 to v5.8.4
   - PR: vyos/vyos-build#1228
- accel-ppp-ng: T9039: update the commit hash
   - PR: vyos/vyos-build#1232
- T9040: Build FIPS-provider OpenSSL version
   - PR: vyos/vyos-build#1233
- ci: T9047: grant issues: write to stale workflow token
   - PR: vyos/vyos-build#1234
- ci: T9047: dispatch docker-image rebuild against production ref
   - PR: vyos/vyos-build#1235
- kernel: T8940: disable HYPERV_VTL_MODE and restore Hyper-V vPCI driver
   - PR: vyos/vyos-build#1236


