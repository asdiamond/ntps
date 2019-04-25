# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/HookView.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(665, 510)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.addHookPushButton = QtWidgets.QPushButton(Form)
        self.addHookPushButton.setObjectName("addHookPushButton")
        self.gridLayout.addWidget(self.addHookPushButton, 0, 0, 1, 1)
        self.editPushButton = QtWidgets.QPushButton(Form)
        self.editPushButton.setObjectName("editPushButton")
        self.gridLayout.addWidget(self.editPushButton, 0, 1, 1, 1)
        self.searchLineEdit = QtWidgets.QLineEdit(Form)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.gridLayout.addWidget(self.searchLineEdit, 0, 4, 1, 1)
        self.deletePushButton = QtWidgets.QPushButton(Form)
        self.deletePushButton.setObjectName("deletePushButton")
        self.gridLayout.addWidget(self.deletePushButton, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hookPropertiesTableView = QtWidgets.QTableView(self.groupBox)
        self.hookPropertiesTableView.setObjectName("hookPropertiesTableView")
        self.verticalLayout.addWidget(self.hookPropertiesTableView)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 5)

        self.retranslateUi(Form)

        self.addHookPushButton.clicked.connect(self.addHookPushButtonClicked)
        self.editPushButton.clicked.connect(self.editPushButtonClicked)
        self.searchLineEdit.textEdited.connect(self.searchLineEdited)
        self.deletePushButton.clicked.connect(self.deletePushButtonClicked)
        # self.hookPropertiesTableView has no signals to connect to, TODO implement Tableview
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Search"))
        self.addHookPushButton.setText(_translate("Form", "+Hook"))
        self.editPushButton.setText(_translate("Form", "Edit"))
        self.deletePushButton.setText(_translate("Form", "Delete"))
        self.groupBox.setTitle(_translate("Form", "Hook Properties"))

    @pyqtSlot( )
    def addHookPushButtonClicked( self ):
        self.label.setText("addHookPushButtonClicked")
    
    @pyqtSlot( )
    def editPushButtonClicked( self ):
        self.label.setText("editPushButtonClicked")
    
    @pyqtSlot( )
    def deletePushButtonClicked( self ):
        self.label.setText("deletePushButtonClicked")

    @pyqtSlot(str)
    def searchLineEdited( self, text ):
        self.label.setText(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
