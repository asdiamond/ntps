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
		
