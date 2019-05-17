from queue import Queue
from scapy.all import *
from threading import Thread

from scapy.layers.inet import IP, TCP
from time import sleep

q = Queue()

off = False


def produce():
    while True:
        if off:
            print('putting -1')
            q.put(-1)
            return
        # craft a packet
        i = 1
        pkt = IP()/TCP()
        # pkt.src = i * 100
        # pkt.dst = i * 200
        # if you modify something, call show2 to recalculate everything

        pkt.show2()


        q.put(pkt)

        sleep(.5)


def get():
    return q.get()


def put(pkt):
    q.put(pkt)


def turn_off():
    global off
    off = True


def fill():
    global off
    off = False
    filler = Thread(target=produce)
    filler.start()

