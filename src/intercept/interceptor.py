from netfilterqueue import NetfilterQueue

def produce(pkt):
    print(pkt)

    #pkt.accept()
    
def start_interception():
    nfq = NetfilterQueue()
    nfq.bind(1, produce)

    try:
        nfq.run()
    except KeyboardInterrupt:
        print('Goodbye!')

    nfq.unbind()
