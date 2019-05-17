# holds packets that have been intercepted
from queue import Queue

q = Queue()  # will start off with effectively infinte q size, we can change as necessary for performance


# return a packet from the queue
# will block your thread if there are none
def get():
    # TODO this is where we will have to handle/send the signal to stop threads
    # TODO When interception is turned off
    pkt = q.get()
    # i'm unsure if I need to call task_done here...
    return pkt


pc = []
# for the interceptor to call
# will block thread if the queue is full
def put(packet):
    q.put(packet)
