from scapy.all import *

def apply(pkt):
	if(packet.haslayer(DNS)):
		pkt[UDP].sport = 44444
		del pkt.chksum
		del pkt.len
		del pkt[TCP].chksum
		
	pkt.show2(dump=True)
	return pkt