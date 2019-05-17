from scapy.all import *


def apply(pkt):
    if pkt.haslayer(TCP):
        pkt[TCP].sport = 55555
        del pkt.chksum
        del pkt.len
        del pkt[TCP].chksum

    pkt.show2()
    # pkt = pkt.__class__(str(packet))
    return pkt
