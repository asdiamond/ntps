# holds packets that have been intercepted


# return a packet from the queue
# will block your thread if there are none
def get():
    return


# for the interceptor to call
# will block thread if the queue is full
def put(packet):
    return