from HookCollectionSubsystem.HookCollectionManager import HookCollectionManager
from src.intercept import intercepted

class HookRunner:

    def __init__(self, manager: HookCollectionManager, packet_collection):
        self.__manager = manager
        self.__packet_collection = packet_collection
        self.run()

    def run(self):
        while True:
            packet = intercepted.get()
            modified_packet = self.__manager.run_hooks(packet)
            if modified_packet:
                self.__packet_collection.put(modified_packet)

