# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/HookCollectionMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(665, 510)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.addHookCollectionPushButton = QtWidgets.QPushButton(Form)
        self.addHookCollectionPushButton.setObjectName("addHookCollectionPushButton")
        self.gridLayout.addWidget(self.addHookCollectionPushButton, 0, 0, 1, 1)
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
        self.hookCollectionPropertiesTableView = QtWidgets.QTableView(self.groupBox)
        self.hookCollectionPropertiesTableView.setObjectName("hookCollectionPropertiesTableView")
        self.verticalLayout.addWidget(self.hookCollectionPropertiesTableView)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Search"))
        self.addHookCollectionPushButton.setText(_translate("Form", "+Hook Collection"))
        self.editPushButton.setText(_translate("Form", "Edit"))
        self.deletePushButton.setText(_translate("Form", "Delete"))
        self.groupBox.setTitle(_translate("Form", "Hook Collection Properties"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
