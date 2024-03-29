from src.HookSubsystem import Hook
from src.HookCollectionSubsystem.HookCollection import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from scapy.all import *
import binascii

def exec_number(elem):
        return elem.get_execution_number()

class HookCollectionManager:
    hook_collection_list: list

    def __init__(self):
        self.hook_collection_list = []
        self.__num_collections = 0

    # Update hook collection's execution seq number
    def update_collection_seq_number(self, hook_collection, sequence_number: int):
        hook_collection.set_execution_number(sequence_number)

    # Update hook collection's name
    def update_colllection_name(self, hook_collection, name: str):
        hook_collection.set_name(name)

    # Update hook collection's description
    def update_collection_description(self, hook_collection, description: str):
        hook_collection.set_description(description)

    # Add a hook collection
    def add_collection(self, name: str, description: str, hookList, status: bool, execution_number: int):
        collection = HookCollection(name,description, status, execution_number)
        self.hook_collection_list.append(collection)
        for hook in hookList:
            collection.add_hook(hook)
        self.__num_collections += 1

    # Delete a hook collection
    def del_hook_collection(self, hook_collection):
        for hook in hook_collection.get_list():
            hook_collection.remove_hook(hook)
        self.hook_collection_list.remove(hook_collection)
        del hook_collection
        self.__num_collections -= 1

    # Search a hook collection
    def search(self, query, n):
        pass

    # Method to remove a hook from all collections
    def remove_hook_from_collections(self, hook: Hook):
        for collection in self.hook_collection_list:
            collection.remove_hook(hook)

    # Run all enabled collections
    def run_hooks(self, parameter):
        modified_parameter = parameter
        sortedCollection = self.hook_collection_list.sort(key = exec_number)
        for collection in sortedCollection:
            if collection.get_status():
                modified_parameter = collection.run_collection(modified_parameter)
        return modified_parameter

    def createHookCollectionModel(self):
        hookCollectionModel = QtGui.QStandardItemModel()
        for hookCollection in self.hook_collection_list:
            hcString = hookCollection.get_name() + '\t'
            hcString += hookCollection.get_execution_number() + '\t'
            hcString += hookCollection.get_status() + '\t'
            for hook in hookCollection.get_list():
                hcString += hook.get_name() + ', '
            hcString += '\t'
            hookCollectionModel.appendRow(QtGui.QStandardItem(hcString))
        return hookCollectionModel


   
