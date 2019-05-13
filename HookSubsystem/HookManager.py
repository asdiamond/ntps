import runpy
from HookCollectionSubsystem.HookCollectionManager import HookCollectionManager
from HookSubsystem.Hook import Hook


class HookManager:

    def __init__(self):
        self.__hook_list = []

    # Remove hook from every collection and then from the system
    def remove_hook(self, hook: Hook, collection_manager: HookCollectionManager):
        collection_manager.remove_hook_from_collections(hook)
        self.__hook_list.remove(hook)
        del hook

    # Add a hook to the system and keep track of it
    def add_hook(self, path: str, name: str, description: str):
        hook_to_add = Hook(path, name, description)
        self.__hook_list.append(hook_to_add)

    # Run a hook
    def run_hook(self, hook: Hook):
        runpy.run_path(hook.get_path())
