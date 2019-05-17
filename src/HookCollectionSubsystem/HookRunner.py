from src.HookCollectionSubsystem import hookedq
from src.HookCollectionSubsystem.HookCollectionManager import HookCollectionManager
from src.HookSubsystem.HookManager import HookManager
from src.integration_test import testq
from src.intercept import intercepted

from threading import Thread
from scapy.all import *


class HookRunner(Thread):

    def __init__(self, manager: HookCollectionManager, ):
        self.__manager = manager
        # self.__packet_collection = packet_collection
        super(HookRunner, self).__init__()

    # if intercept is False, packets are accepted after
    # hooks are run on them
    def run(self, intercept=False):
        while True:
            packet = intercepted.get()
            #pkt = IP(packet.get_payload())
            modified_packet = self.__manager.run_hooks(packet)
            if modified_packet:
                #packet.set_payload(bytearray(str(modified_packet)))
                print("in hook runner")
                #print(modified_packet)
                if intercept:
                    # give to packet collection
                    hookedq.put(packet)
                else:
                    # nfq.accept the packet, so it goes to its destination
                    print('let my packet go')
                    packet.accept()
                    # print(modified_packet)


# for testing


def main():
    hook_collection_manager = HookCollectionManager()
    hook_manager = HookManager()

    collection = hook_collection_manager.add_collection(name='tester', description='for testing')

    hook = hook_manager.add_hook(path='/Users/aleksandr/ntps/res/Demo_Hooks/TCPHook.py',
                                 name='tcphook',
                                 description='testtcphook')

    collection.add_hook(hook)



    testq.fill()

    # place onto hookedq
    hooker = HookRunner(manager=hook_collection_manager)

    hooker.start()


#main()
