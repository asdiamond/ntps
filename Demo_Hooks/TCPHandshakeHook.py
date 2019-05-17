from scapy.all import *

FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80

def apply(pkt):
    if pkt.haslayer(TCP):
        
        s = pkt.flags
        
        if pkt and pkt.haslayer(IP):
            if s & 0x3f == 0x12: #SYN+ACK
                logger.info("RCV: SYN+ACK")
                return self.send_synack_ack(pkt)
        
        elif s & SYN:
            
            seq1=random.randrange(0,2**32)            
            
            ip = IP(src = pkt.dst,dst= pkt.src)
            syn = TCP(sport= pkt.sport,dport=443,flags='S',seq=seq1)
            SYNACK=sr1(ip/syn)

            ack=TCP(sport=pkt.sport, dport=443, flags='A', seq=SYNACK.ack + 1, ack=SYNACK.seq + 1) #SYN-ACK
            send(ip/ack)
            
    pkt.show2() 