from HookSubsystem import Hook


class HookCollection:

    __name: str
    __description: str
    __execution_number: int
    __status: bool
    __num_hooks: int

    #Initializer
    def __init__(self, name: str,description: str,execution_number: int):
        self.hook_list = []
        self.__name = name
        self.__description = description
        self.__execution_number = execution_number
        self.__status = False
        self.__num_hooks = 0

    #Gettter for hook collection description
    def get_description(self):
        return self.__description

    #Getter for hook collection status
    def get_status(self):
        return self.__status

    #Getter for hook collection name
    def get_name(self):
        return self.__name

    # Getter for hook collection execution number
    def get_execution_number(self):
        return self.__execution_number

    # Getter for hook collection's number or hooks
    # / length of the colleciotn
    def len(self):
        return self.__num_hooks

    def add_hook(self, hook: Hook):
        self.hook_list.append(hook)
        hook.set_collection_association_number(hook.get_display_info()['num_collections']+1)

    def remove_hook(self, hook: Hook):
        self.hook_list.remove(hook)
        hook.set_collection_association_number(hook.get_display_info()['num_collections']-1)