from HookCollectionSubsystem.HookCollection import HookCollection
from HookSubsystem import Hook


class HookCollectionManager:
    __hook_collection_list: list

    def __init__(self):
        self.__hook_collection_list = []
        self.__num_collections = 0

    # Update hook collection's execution seq number
    def update(self, hook_collection: HookCollection, sequence_number: int):
        hook_collection.set_execution_number(sequence_number)

    # Update hook collection's name
    def update(self, hook_collection: HookCollection, name: str):
        hook_collection.set_name(name)

    # Update hook collection's description
    def update(self, hook_collection: HookCollection, description: str):
        hook_collection.set_description(description)

    # Add a hook collection
    def add_collection(self, name: str, description: str):
        collection = HookCollection(name,description, self.__num_collections)
        self.__hook_collection_list.append(collection)
        self.__num_collections += 1

    # Delete a hook collection
    def del_hook_collection(self, hook_collection: HookCollection):
        for hook in hook_collection.get_list():
            hook_collection.remove_hook(hook)
        self.__hook_collection_list.remove(hook_collection)
        del hook_collection
        self.__num_collections -= 1

    # Search a hook collection
    def search(self, query, n):
        pass

    # Method to remove a hook from all collections
    def remove_hook_from_collections(self, hook: Hook):
        for collection in self.__hook_collection_list:
            collection.remove_hook(hook)