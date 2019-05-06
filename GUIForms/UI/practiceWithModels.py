from PyQt5 import QtCore, QtGui, QtWidgets
from scapy.all import *


class GroupDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(GroupDelegate, self).__init__(parent)
        self._plus_icon = QtGui.QIcon("plus.png")
        self._minus_icon = QtGui.QIcon("minus.png")

    def initStyleOption(self, option, index):
        super(GroupDelegate, self).initStyleOption(option, index)
        if not index.parent().isValid():
            is_open = bool(option.state & QtWidgets.QStyle.State_Open)
            option.features |= QtWidgets.QStyleOptionViewItem.HasDecoration
            option.icon = self._minus_icon if is_open else self._plus_icon

class GroupView(QtWidgets.QTreeView):
    def __init__(self, model, parent=None):
        super(GroupView, self).__init__(parent)
        self.setIndentation(0)
        self.setExpandsOnDoubleClick(False)
        self.clicked.connect(self.on_clicked)
        delegate = GroupDelegate(self)
        self.setItemDelegateForColumn(0, delegate)
        self.setModel(model)
        self.setHeaderHidden(True)
        # self.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_clicked(self, index):
        if not index.parent().isValid() and index.column() == 0:
            self.setExpanded(index, not self.isExpanded(index))


class GroupModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(GroupModel, self).__init__(parent)
        packets = rdpcap('example.pcap')
        displayPackets = {}
        i = 0
        for p in packets:
            layers = []
            summary = p.summary().split(' / ')
            for s in summary:
                layer = s.split(' ')[0]
                print(layer)
                if layer is 'Ether':
                    layer = 'Ethernet: Src: ' + p['Ether'].src + ', Dst: ' + p['Ether'].dst
                elif layer is 'IP':
                    layer = 'Internet Protocol Version ' + p.version + ', Src: ' + p['IP'].src + ', Dst: ' + p['IP'].dst
                elif layer is 'TCP':
                    layer = 'Transmission Controll Protocol, Src Port: ' + p['TCP'].sport + ', Dst Port: ' + p['TCP'].dport + ', Seq: ' + p['TCP'].seq + ', Ack: ' + p['TCP'].ack
                layers.append(layer)

            displayPackets['Frame ' + str(i) + ': ' + p.summary()] = layers
            i+=1
            
        # datas = {
        #     "Category 1": [
        #         ("New Game 2", "Playnite", "", "", "Never", "Not Played", ""),
        #         ("New Game 3", "Playnite", "", "", "Never", "Not Played", ""),
        #     ],
        #     "No Category": [
        #         ("New Game", "Playnite", "", "", "Never", "Not Plated", ""),
        #     ]
        # }
        for group, layers in displayPackets.items():
            group_item = self.add_group(group)
            self.append_element_to_group(group_item, layer)

    def add_group(self, group_name):
        item_root = QtGui.QStandardItem()
        item_root.setEditable(False)
        item = QtGui.QStandardItem(group_name)
        item.setEditable(False)
        ii = self.invisibleRootItem()
        i = ii.rowCount()
        for j, it in enumerate((item_root, item)):
            ii.setChild(i, j, it)
            ii.setEditable(False)
        for j in range(self.columnCount()):
            it = ii.child(i, j)
            if it is None:
                it = QtGui.QStandardItem()
                ii.setChild(i, j, it)
        return item_root

    def append_element_to_group(self, group_item, texts):
        j = group_item.rowCount()
        item_icon = QtGui.QStandardItem()
        item_icon.setEditable(False)
        item_icon.setIcon(QtGui.QIcon("game.png"))
        group_item.setChild(j, 0, item_icon)
        for i, text in enumerate(texts):
            item = QtGui.QStandardItem(text)
            item.setEditable(False)
            group_item.setChild(j, i+1, item)





