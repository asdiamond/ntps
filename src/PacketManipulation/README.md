Packet Manipulation 

To capture packets, use the sniff() function. It has many different options
such as: sniff(iface='dummy0', filter='udp')
use _.summary()

pkts = sniff(count=10) will capture 10 packets into pkts (array)
pkts[0].summary()
'Ether / IP / ICMP 172.16.20.10 > 4.2.2.1 echo-request 0 / Raw'
pkts[3].show() will show the contents of the 4th packet.

To access packets by layer:
The packets themselves are arrays of layers which can be accessed as so:
example: pkts[3][ICMP].summary() will show the summary of the icmp layer in the 4th packet

To access a packet by field:
pkts[3][IP].ttl

Packet Layers:
	Ethernet
		with: src, dst, type
	IP
		with: version, ihl, tos, len, id, flags, frag, ttl, proto, chksum, src, dst
	ICMP
		with: type, code, chksum, id, seq
		
All this layer attributes can be modified by just calling _.[<layer>].attribute 
where _ is the current packet, <layer> is the specified layer, and attribute is 
a layer value valid to that layer. 

To build a packet:
example to build an arp packet

pkt = Ether()/ARP()
pkt[ARP].hwsrc = "00:11:22:aa:bb:cc"
pkt[ARP].pdst = "123.45.67.8"
pkt[Ether].dst = "ff:ff:ff:ff:ff:ff"

