import os

class Hook:
    __name: str
    __description: str
    __path: str
    __status: bool
    __collection_association_number: int

    # Initializer
    def __init__(self, path: str, name: str, description: str):
        self.__path = path
        self.__name = name
        self.__description = description
        self.__status = True
        self.__collection_association_number = 0

    # Returns a dictionary with the display information of the hook
    def get_display_info(self):
        return {'description' : self.__description, 'num_collections' : self.__collection_association_number}

    # Returns a string representing the absolute path of the hook
    def get_path(self):
        return self.__path

    # Returns a string representing the name of the hook
    def get_name(self):
        return self.__name

    # Returns a string representing the status of the hook
    def get_status(self):
        return self.__status

    # Sets the number of associations to a new number
    def set_collection_association_number(self, new_number: int):
        self.__collection_association_number = new_number

    # Toggles the status of the hook
    def hook_toggle(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    # Edits the hook name.
    def edit_name(self, name: str):
        self.__name = name

    # Edits the hook description.
    def edit_description(self, description: str):
        self.__description = description

    # Edits the hook path.
    def edit_path(self, path: str):
        if os.path.exists(path) and os.path.isabs(path) and os.path.isfile(path):
            self.__path = path