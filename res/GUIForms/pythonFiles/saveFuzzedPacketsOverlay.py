# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/saveFuzzedPacketsOverlay.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_Dialog(QObject):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 264)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.fuzzedPCAPNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.fuzzedPCAPNameLineEdit.setAutoFillBackground(True)
        self.fuzzedPCAPNameLineEdit.setStyleSheet("")
        self.fuzzedPCAPNameLineEdit.setObjectName("fuzzedPCAPNameLineEdit")
        self.gridLayout.addWidget(self.fuzzedPCAPNameLineEdit, 0, 2, 1, 2)
        self.savePushButton = QtWidgets.QPushButton(Dialog)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout.addWidget(self.savePushButton, 2, 3, 1, 1)
        self.descriptionLineEdit = QtWidgets.QLineEdit(Dialog)
        self.descriptionLineEdit.setAutoFillBackground(True)
        self.descriptionLineEdit.setStyleSheet("")
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.gridLayout.addWidget(self.descriptionLineEdit, 1, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cancelPushButton = QtWidgets.QPushButton(Dialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.gridLayout.addWidget(self.cancelPushButton, 2, 2, 1, 1)

        self.retranslateUi(Dialog)

        self.descriptionLineEdit.textEdited.connect(self.descriptionLineEdited)
        self.fuzzedPCAPNameLineEdit.textEdited.connect(self.fuzzedPCAPNameLineEdited)

        self.savePushButton.clicked.connect(self.savePushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)


        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.fuzzedPCAPNameLineEdit.setPlaceholderText(_translate("Dialog", "PCAP File"))
        self.savePushButton.setText(_translate("Dialog", "Save"))
        self.descriptionLineEdit.setPlaceholderText(_translate("Dialog", "Description"))
        self.label_2.setText(_translate("Dialog", "Description"))
        self.label.setText(_translate("Dialog", "Fuzzed PCAP \n"
" Name"))
        self.cancelPushButton.setText(_translate("Dialog", "Cancel"))

    @pyqtSlot(str)
    def descriptionLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def fuzzedPCAPNameLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot( )
    def savePushButtonClicked( self ):
        self.label.setText("savePushButtonClicked")

    @pyqtSlot( )
    def cancelPushButtonClicked( self ):
        self.label.setText("cancelPushButtonClicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
