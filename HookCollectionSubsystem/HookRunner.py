from HookCollectionSubsystem.HookCollectionManager import HookCollectionManager
from src.intercept import intercepted

class HookRunner:

    def __init__(self, manager: HookCollectionManager, packet_collection):
        self.__manager = manager
        self.__packet_collection = packet_collection
        self.run()

    def run(self):
        while True:
            packet_to_process = intercepted.get()
            modified_packet = self.__manager.run_hooks(packet_to_process)
            if modified_packet:
                #put into queue
