import sys
sys.path.extend(['/root/ntps/'])

from netfilterqueue import NetfilterQueue
import subprocess

# the function to put intercepted packets on the blocking queue
# from intercepted import put
from src.intercept import intercepted
from scapy.all import *

off = False

def turn_off():
    global off
    off = True

def produce(pkt):
    print('in proxy')
    #print(pkt)
    if off:
        intercepted.put(-1)
        return
    intercepted.put(pkt)


def interception():
    # save previous iptables config to `previous_configs/fname`
    # by calling the save.sh script
    fname = "previous_config.txt"
    #subprocess.call(["/root/ntps/src/intercept/save.sh", fname])

    # change iptables rule to forward traffic into nfqueue
    #subprocess.call("/root/ntps/src/intercept/intercept.sh")

    # bind nfque, and call produce method on new packets intercepted
    nfq = NetfilterQueue()
    nfq.bind(1, produce)

    try:
        nfq.run()
    except KeyboardInterrupt:
        subprocess.call(['/root/ntps/src/intercept/restore.sh', fname])
        nfq.unbind()
        print('Goodbye!')


from threading import Thread
from src.HookCollectionSubsystem import HookRunner

from src.HookCollectionSubsystem import hookedq
from src.HookCollectionSubsystem.HookCollectionManager import HookCollectionManager
from src.HookSubsystem.HookManager import HookManager
from src.integration_test import testq
from src.intercept import intercepted


def main():
    hook_collection_manager = HookCollectionManager()
    hook_manager = HookManager()

    collection = hook_collection_manager.add_collection(name='tester', description='for testing')

    hook = hook_manager.add_hook(path='/root/ntps/res/Demo_Hooks/TCPHook.py',
                                 name='tcphook',
                                 description='testtcphook')

    collection.add_hook(hook)



    #testq.fill()
    proxy = Thread(target=interception)

    # place onto hookedq
    hooker = HookRunner.HookRunner(manager=hook_collection_manager)

    hooker.start()
    proxy.start()


