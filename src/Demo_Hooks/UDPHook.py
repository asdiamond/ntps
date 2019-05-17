from scapy.all import *

def apply(pkt):
	if(pkt.haslayer(TCP)):
		del pkt
		return None
	else:
		return pkt