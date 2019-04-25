# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/optionView.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(209, 718)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hookPushButton = QtWidgets.QPushButton(Dialog)
        self.hookPushButton.setObjectName("hookPushButton")
        self.verticalLayout.addWidget(self.hookPushButton)
        self.hookCollectionPushButton = QtWidgets.QPushButton(Dialog)
        self.hookCollectionPushButton.setObjectName("hookCollectionPushButton")
        self.verticalLayout.addWidget(self.hookCollectionPushButton)
        self.livePacketPushButton = QtWidgets.QPushButton(Dialog)
        self.livePacketPushButton.setObjectName("livePacketPushButton")
        self.verticalLayout.addWidget(self.livePacketPushButton)
        self.packetFromPCAPPushButton = QtWidgets.QPushButton(Dialog)
        self.packetFromPCAPPushButton.setObjectName("packetFromPCAPPushButton")
        self.verticalLayout.addWidget(self.packetFromPCAPPushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.hookPushButton.setText(_translate("Dialog", "Hook"))
        self.hookCollectionPushButton.setText(_translate("Dialog", "Hook Collection"))
        self.livePacketPushButton.setText(_translate("Dialog", "Live Packet"))
        self.packetFromPCAPPushButton.setText(_translate("Dialog", "Packet from PCAP"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
