from src.HookSubsystem.Hook import Hook
from src.HookSubsystem.HookManager import HookManager


class HookCollection:
    __name: str
    __description: str
    __execution_number: int
    __status: bool
    __num_hooks: int

    # Initializer

    def __init__(self, name: str, description: str, status: bool, execution_number: int):
        self.__hook_list = []
        self.__name = name
        self.__description = description
        self.__execution_number = execution_number
        self.__status = status
        self.__num_hooks = 0

    # Getter for hook collection description
    def get_description(self):
        return self.__description

    # Getter for hook collection status
    def get_status(self):
        return self.__status

    # Getter for hook collection name
    def get_name(self):
        return self.__name

    # Getter for hook collection execution number
    def get_execution_number(self):
        return self.__execution_number

    # Getter for hook collection's number or hooks
    # / length of the collection
    def len(self):
        return self.__num_hooks

    # Getter for hook list
    def get_list(self):
        return self.__hook_list

    # Setter for hook collection's execution sequence number
    def set_execution_number(self, execution_number: int):
        self.__execution_number = execution_number

    # Setter for hook collection's name
    def set_name(self, name: str):
        self.__name = name

    # Setter for hook collection's description
    def set_description(self, description: str):
        self.__description = description

    # Toggles the status of the hook collection
    def hook_collection_toggle(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    # Add hook to the hook collection
    def add_hook(self, hook: Hook):
        self.__hook_list.append(hook)
        self.__num_hooks += 1
        hook.set_collection_association_number(hook.get_display_info()['num_collections'] + 1)

    # Remove hook from a collection
    def remove_hook(self, hook: Hook):
        self.__hook_list.remove(hook)
        self.__num_hooks -= 1
        hook.set_collection_association_number(hook.get_display_info()['num_collections'] - 1)

    def run_collection(self, parameter):
        parameter_mod = parameter
        for hook in self.__hook_list:
            if hook.get_status():
                if parameter_mod:
                    parameter_mod = HookManager.run_hook(hook, parameter_mod)
        return parameter_mod
