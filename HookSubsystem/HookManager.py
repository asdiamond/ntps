from HookSubsystem import Hook


class HookManager:
    
    def __init__(self):
        self.__hook_list = []

    #Remove hook from every collection and then from the system
    def remove_hook(self, hook: Hook):
        pass

    #Add a hook to the system and keep track of it
    def add_hook(self, path: str, name: str, description: str):
        hook_to_add = Hook(path,name,description)
        self.__hook_list.append(hook_to_add)

    def run_hook(self, hook: Hook):        pass
