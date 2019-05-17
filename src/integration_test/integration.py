from queue import Queue
from threading import Thread
import time
from scapy.all import *
from scapy.layers.inet import IP

q = Queue()
def int_test():
    producer = Thread(target=start_interception_test)
    consumer = Thread(target=consume)

    # producer.start()
    # consumer.start()
    # start_interception_test()



# producer
def start_interception_test():
    pckts = []
    pl = b'deadbeef'
    for i in range(20):
        pkt = IP()
        pkt.src = i * 100
        pkt.dst = i * 200
        # pkt.payload = pl

        pckts.append(pkt)

    for i in range(len(pckts)):
        time.sleep(.5)
        q.put(pckts[i])

    q.put(-1)

# from src.ntpsLayout import PCAPFileManager
# gui = PCAPFileManager.LiveTrafficPacketFileManager()

def consume():
    while True:
        pkt = q.get()
        if pkt is -1:
            return

        print(pkt)
        gui.put(pkt)
