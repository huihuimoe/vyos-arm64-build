## vyos-1x
- Smoketest: T8879: add missing Kernel config tests for hypervisor platforms
   - PR: vyos/vyos-1x#5203
- vyos.commit: T8781: move from O(n) to O(1) for commit_in_progress() checks
   - PR: vyos/vyos-1x#5200
- vyos-netlinkd: T8781: try IPRoute.bind() RTNL subscription first
   - PR: vyos/vyos-1x#5207
- high-availability: T7059: Allow disabling persistent connections for virtual-server
   - PR: vyos/vyos-1x#5205
- T6933: fix "system option performance" overwrites sysctl parameters from firewall
   - PR: vyos/vyos-1x#5206
- T7880: Add NTP hardware timestamp receive-filter compatibility check
   - PR: vyos/vyos-1x#5160
- load-balancing: T7928: Fix port conflict check to respect 
   - PR: vyos/vyos-1x#5186
- wireless: T8528: Add module config code for mt7916 based cards
   - PR: vyos/vyos-1x#5135
- wireguard: T8509: Add fwmark ip rules for VRF-bound interfaces
   - PR: vyos/vyos-1x#5175
- T8822: Add BFD strict mode for BGP
   - PR: vyos/vyos-1x#5210
- ntp: T8601: add local stratum option
   - PR: vyos/vyos-1x#5166


## vyos-build
- Kernel: T8871: add a patch for the ptrace vulnerability that allows unprivileged users to read files owned by any other user
   - PR: vyos/vyos-build#1191
- Kernel: T8871: Update Linux Kernel to 6.18.31
   - PR: vyos/vyos-build#1192
- Kernel: T8879: add missing Hyper-V drivers after 6.18 upgrade
   - PR: vyos/vyos-build#1193
- Kernel: T8880: reduce size of Kernel source TAR
   - PR: vyos/vyos-build#1194


