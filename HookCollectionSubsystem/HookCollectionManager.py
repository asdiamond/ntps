from HookCollectionSubsystem import HookCollection


class HookCollectionManager:
    __hook_collection_list: list

    def __init__(self):
        self.__hook_collection_list = []

    #Update hook collections
    def update(self, hook, sequence_number: int, name: str, description: str):
        pass

    #Add a hook collection
    def add_collection(self, name: str, description: str):
        pass

    #Delete a hook collection
    def del_hook_collection(self, hook_collection: HookCollection):
        pass

    #Search a hook collection
    def search(self, query, n):
        pass