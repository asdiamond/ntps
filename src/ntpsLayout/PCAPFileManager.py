from PyQt5 import QtCore, QtGui, QtWidgets
from scapy.all import *
import binascii

from scapy.layers.inet import IP

from src.HookCollectionSubsystem import hookedq


class PacketFileManager():
    def __init__(self):
        self.dissectedModel = self.createDissectedModel()
        self.binaryModel = self.createBinaryModel()
        self.HEXModel = self.createHEXModel()

    def getFieldDict(self, packetIndex, layerName):
        return self.packets[packetIndex][layerName].fields

    def createDissectedModel(self):
        dissectedModel = QtGui.QStandardItemModel()
        displayPackets = {}
        i = 0
        for p in self.packets:
            layers = []
            summary = p.summary().split(' / ')
            for s in summary:
                layer = s.split(' ')
                layers.append(layer)

            displayPackets['Frame ' + str(i) + ': ' + p.summary()] = layers
            i += 1
        for group, layers in displayPackets.items():
            group_item = self.add_group(dissectedModel, group)
            for layer in layers:
                self.append_element_to_group(dissectedModel, group_item, layer)
        return dissectedModel

    def createBinaryModel(self):
        binaryModel = QtGui.QStandardItemModel()
        for p in self.packets:
            binaryModel.appendRow(QtGui.QStandardItem(str(raw(p))[2:-1]))
        return binaryModel

    def createHEXModel(self):
        HEXModel = QtGui.QStandardItemModel()
        for p in self.packets:
            x = b" ".join(re.findall(b'..', binascii.hexlify(raw(p))))
            HEXModel.appendRow(QtGui.QStandardItem(str(x)[2:-1]))
        return HEXModel

    def add_group(self, dissectedModel, group_name):
        item_root = QtGui.QStandardItem()
        item_root.setEditable(False)
        item = QtGui.QStandardItem(group_name)
        item.setEditable(False)
        ii = dissectedModel.invisibleRootItem()
        i = ii.rowCount()
        for j, it in enumerate((item_root, item)):
            ii.setChild(i, j, it)
            ii.setEditable(False)
        for j in range(dissectedModel.columnCount()):
            it = ii.child(i, j)
            if it is None:
                it = QtGui.QStandardItem()
                ii.setChild(i, j, it)
        return item_root

    def append_element_to_group(self, dissectedModel, group_item, texts):
        j = group_item.rowCount()
        item_icon = QtGui.QStandardItem()
        item_icon.setEditable(False)
        group_item.setChild(j, 0, item_icon)
        for i, text in enumerate(texts):
            item = QtGui.QStandardItem(text)
            item.setEditable(False)
            group_item.setChild(j, i + 1, item)

    def modifyPacket(self, index, layer, modifications):
        self.packets[index][layer].fields = modifications


from threading import Thread
from src.integration_test import testq

from scapy.all import *


class LiveTrafficPacketFileManager(PacketFileManager):
    def __init__(self, ):
        self.packets = []
        super(LiveTrafficPacketFileManager, self).__init__()
        self.get_pkts()

    def get_pkts(self):
        t = Thread(target=self.producer)
        t.start()

    def producer(self, ):
        while True:
            pkt = hookedq.get()
            if pkt is -1:
                print('got -1')
                return
            else:  # we got the signal to stop
                self.put(pkt)

    def put(self, packet):
        # Use packet to update the view
        self.packets.append(packet)
        x = b" ".join(re.findall(b'..', binascii.hexlify(raw(packet))))
        self.dissectedModel.appendRow(QtGui.QStandardItem(str(x)[2:-1]))
        # self.dissectedModel = self.createDissectedModel()
        # self.binaryModel = self.createBinaryModel()
        # self.HEXModel = self.createHEXModel()


class PCAPFileManager(PacketFileManager):
    def __init__(self, filename):
        self.filename = filename
        self.packets = rdpcap(self.filename)
        super(PCAPFileManager, self).__init__()
