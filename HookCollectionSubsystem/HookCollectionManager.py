from HookCollectionSubsystem.HookCollection import HookCollection


class HookCollectionManager:
    __hook_collection_list: list

    def __init__(self):
        self.__hook_collection_list = []

    # Update hook collection's execution seq number
    def update(self, hook_collection, sequence_number: int):
        


    # Add a hook collection
    def add_collection(self, name: str, description: str):
        pass

    # Delete a hook collection
    def del_hook_collection(self, hook_collection: HookCollection):
        for hook in hook_collection.get_list():
            hook_collection.remove_hook(hook)
        del hook_collection

    # Search a hook collection
    def search(self, query, n):
        pass

    # Method to remove a hook from all collections
    def remove_hook_from_collections(self, hook):
        for collection in self.__hook_collection_list:
            collection.remove_hook(hook)
