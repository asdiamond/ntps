import importlib.util
from src.HookSubsystem.Hook import Hook
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from scapy.all import *
import binascii

class HookManager:

    def __init__(self):
        self.hooks = []
        self.hookModel = None

    # Remove hook from every collection and then from the system
    def remove_hook(self, hook: Hook, collection_manager):
        collection_manager.remove_hook_from_collections(hook)
        self.hooks.remove(hook)
        del hook

    # Add a hook to the system and keep track of it
    def add_hook(self, path: str, name: str, description: str):
        hook_to_add = Hook(path, name, description)
        self.hooks.append(hook_to_add)

    # Run a hook
    @staticmethod
    def run_hook(hook: Hook, parameter):
        spec = importlib.util.spec_from_file_location(hook.get_name(), hook.get_path())
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.apply(parameter)


    def createHookModel(self):
        hookModel = QtGui.QStandardItemModel()
        for hook in self.hooks:
            hookModel.appendRow(QtGui.QStandardItem(hook.get_name()))
        return hookModel





