# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/Layout.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 707)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.contentListView = QtWidgets.QListView(Form)
        self.contentListView.setObjectName("contentListView")
        self.gridLayout.addWidget(self.contentListView, 3, 1, 1, 1)
        self.optionListView = QtWidgets.QListView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionListView.sizePolicy().hasHeightForWidth())
        self.optionListView.setSizePolicy(sizePolicy)
        self.optionListView.setObjectName("optionListView")
        self.gridLayout.addWidget(self.optionListView, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.retranslateUi(Form)


        # self.contentListView has no signals to connect to, TODO implement Tableview
        # self.optionListView has no signals to connect to, TODO implement Tableview


        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Content View"))
        self.label.setText(_translate("Form", "Option View"))
        self.label_3.setText(_translate("Form", "Network Traffic Proxy System"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
