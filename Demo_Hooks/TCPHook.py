from scapy.all import *

def apply(pkt):
	if(packet.haslayer(TCP)):
		pkt[TCP].sport = 55555
		del pkt.chksum
		del pkt.len
		del pkt[TCP].chksum
		
	pkt.show2(dump=True)
	return pkt