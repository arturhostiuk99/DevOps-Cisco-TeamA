# DevOps-Cisco-TeamA
DC1:
- Configure the IP address 11.11.0.0.24 (the 30th mask between the routers)
- PC1, PC2 in a private network
- Configure OSPF
- IPSEC from VPN1-1 to VPN2-1
- Configure OSPF in the middle of IPSEC

DC2:
- Configure HSRP between (RTR2-1 and RTR2-2)
- Configure the IP address 11.11.0.0.24 (the 30th mask between the routers)
- FW route by default via Virtual Router (without OSPF)
- FW configure NAT
- Configure OSPF
- PC1, PC2 in a private network
- IPSEC from VPN1-2 to VPN2-2

ISP1:
- configure BGP

ISP2:
- configure BGP


!!! Private networks must be accessible through a tunnel (IPSEC)
!!! ISP1 and ISP2 do not have to have these routes in the routing table
