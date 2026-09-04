## vyos-1x
- http-api: T9224: add ping endpoint to REST API
   - PR: vyos/vyos-1x#5415
- http-api: T9223: add VRF option to traceroute REST API endpoint
   - PR: vyos/vyos-1x#5414
- firewall: T9242: Add mac-address-mask support
   - PR: vyos/vyos-1x#5425
- wan-load-balance: T9145: add health script interface env
   - PR: vyos/vyos-1x#5399
- nat: T9162: fix KeyError when show nat rules has no inbound-interface
   - PR: vyos/vyos-1x#5375
- T9244: fix regression in setting console type on install
   - PR: vyos/vyos-1x#5428
- T9240: container: Allow sharing host's cgroup namespace with container
   - PR: vyos/vyos-1x#5423
- T9146: add initial set/call_dependents as exempt from possible cycle
   - PR: vyos/vyos-1x#5427
- ha: T9166: add IPv6 support for HA peer links
   - PR: vyos/vyos-1x#5408
- T9258: Improve blackbox-exporter ICMP smoketest for VRF binding
   - PR: vyos/vyos-1x#5432
- podman: T9129: Use systemd quadlet for containers and networks
   - PR: vyos/vyos-1x#5426
- vrf: T6097: add the nat anchor conntrack zoning needs
   - PR: vyos/vyos-1x#5431
- smoketest: T9014: guard architecture specific smoketests
   - PR: vyos/vyos-1x#5433
- pki: T9225: Support ED25519 and ED448 signatures on public keys in PKI
   - PR: vyos/vyos-1x#5418


## vyos-build
- podman: T9129: Fix podman prefix directory
   - PR: vyos/vyos-build#1277
- Kernel: T9259: Update Linux Kernel to 6.18.48
   - PR: vyos/vyos-build#1279
- oci: T9265: add support for ARM64 container image generation
   - PR: vyos/vyos-build#1282
- oci: T9265: add CPU architecture (fallback amd64) to image filename
   - PR: vyos/vyos-build#1284
- oci: T9269: compress OCI image and minor fixes to container runtime
   - PR: vyos/vyos-build#1286
- Kernel: T9272: update Intel out-of-tree IXGBE and ICE drivers
   - PR: vyos/vyos-build#1287


