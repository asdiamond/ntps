from scapy.all import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class PacketFromPCAPModel(QStandardItemModel):
	def __init__(self, listView, filePath):
		super(PacketFromPCAPModel, self).__init__(listView)
		packets = rdpcap(filePath)
		items = []
		for p in packets:
			items.append(p.summary())
			self.appendRow(QStandardItem(items[-1]))
