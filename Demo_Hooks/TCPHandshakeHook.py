from scapy.all import *

FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80

def run(packet):
    if packet.haslayer(TCP):
        
        s = packet.flags
        
        if packet and packet.haslayer(IP):
            if s & 0x3f == 0x12:#SYN+ACK
                logger.info("RCV: SYN+ACK")
                return self.send_synack_ack(pkt)
        
        elif s & SYN:
            
            seq1=random.randrange(0,2**32)            
            
            ip = IP(src = packet.dst,dst= packet.src)
            syn = TCP(sport= packet.dport,dport=packet.sport,flags='S',seq=seq1)
            SYNACK=sr1(ip/syn)

            ack=TCP(sport=packet.dport, dport=packet.sport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)# SYN-ACK
            send(ip/ack)
            
    pkt.show2() 