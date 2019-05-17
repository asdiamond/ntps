import importlib.util
from src.HookCollectionSubsystem import HookCollectionManager
from src.HookSubsystem.Hook import Hook


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
        # TODO added for testing
        return hook_to_add

    # Run a hook
    @staticmethod
    def run_hook(hook: Hook, parameter):
        spec = importlib.util.spec_from_file_location(hook.get_name(), hook.get_path())
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.apply(parameter)
