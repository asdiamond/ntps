from queue import Queue
from scapy.all import *

q = Queue()


def get():
    return q.get()

def put(pkt):
    q.put(pkt)
