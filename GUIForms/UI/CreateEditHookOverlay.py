# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/CreateEditHookOverlay.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.hookPathLineEdit = QtWidgets.QLineEdit(Form)
        self.hookPathLineEdit.setObjectName("hookPathLineEdit")
        self.gridLayout.addWidget(self.hookPathLineEdit, 2, 1, 1, 1)
        self.hookNameLineEdit = QtWidgets.QLineEdit(Form)
        self.hookNameLineEdit.setObjectName("hookNameLineEdit")
        self.gridLayout.addWidget(self.hookNameLineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.descriptionLineEdit = QtWidgets.QLineEdit(Form)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.gridLayout.addWidget(self.descriptionLineEdit, 1, 1, 1, 1)
        self.browsePushButton = QtWidgets.QPushButton(Form)
        self.browsePushButton.setObjectName("browsePushButton")
        self.gridLayout.addWidget(self.browsePushButton, 2, 2, 1, 1)
        self.savePushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout.addWidget(self.savePushButton, 3, 1, 1, 1)
        self.canelPushButton = QtWidgets.QPushButton(Form)
        self.canelPushButton.setObjectName("canelPushButton")
        self.gridLayout.addWidget(self.canelPushButton, 3, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hook Name"))
        self.label_3.setText(_translate("Form", "Hook Path"))
        self.label_2.setText(_translate("Form", "Description"))
        self.browsePushButton.setText(_translate("Form", "Browse"))
        self.savePushButton.setText(_translate("Form", "Save"))
        self.canelPushButton.setText(_translate("Form", "Cancel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
