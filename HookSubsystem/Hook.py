import os
class Hook:
    name: str
    description: str
    path: str
    status: bool
    collection_association_number: int

    # Initializer
    def __init__(self, path: str, name: str, description: str):
        self.path = path
        self.name = name
        self.description = description
        self.status = True
        self.collection_association_number = 0

    # Returns a dictionary with the display information of the hook
    def get_display_info(self):
        return {'description' : self.description, 'num_collections' : self.collection_association_number}

    # Returns a string representing the absolute path of the hook
    def get_path(self):
        return self.path

    # Sets the number of associations to a new number
    def set_collection_association_number(self, newNumber: int):
        self.collection_association_number = newNumber

    # Toggles the status of the hook
    def hook_toggle(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    # Edits the hook name.
    def edit_name(self, name: str):
        self.name = name

    # Edits the hook description.
    def edit_description(self, description: str):
        self.description = description

    # Edits the hook path.
    def edit_path(self, path: str):
        if os.path.exists(path) and os.path.isabs(path) and os.path.isfile(path):
            self.path = path