# Network Layer
* Message:
* Segment:
* Packet:
* Frame:
## Packet Switching
* Data traffic is divided into packets
* Each packet contains a header with an address
* Packets travel separately through network
* Packet forwarding is based on header
* Destination reconstructs the message
## Best-Effort Packet Delivery
* Packets may be lost
* Packets may be corrupted
* Packets may be delivered out of order
## IP Datagram
* Datagram: basic transfer unit associated with a packet-switched network
* Typically structured in header and payload sections
* Provide a connectionless service across a packet-switched network
## IP Packet Header
* Version: IPv4, IPv6
* Header length (in 32-bit words)
* Type of Service (TOS)
* Packet length (in bytes)
* Fragmentation control firlds
* Time to live (TTL) --> traceroute
* Protocol
* Header checksum
* Source IP Address
* Destination IP Address
* Options
