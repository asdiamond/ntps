# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/HookExecutionSequenceErrorOverlay.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 317)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.yesPushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yesPushButton.sizePolicy().hasHeightForWidth())
        self.yesPushButton.setSizePolicy(sizePolicy)
        self.yesPushButton.setObjectName("yesPushButton")
        self.gridLayout.addWidget(self.yesPushButton, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.noPushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noPushButton.sizePolicy().hasHeightForWidth())
        self.noPushButton.setSizePolicy(sizePolicy)
        self.noPushButton.setObjectName("noPushButton")
        self.gridLayout.addWidget(self.noPushButton, 4, 2, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)


        self.yesPushButton.clicked.connect(self.yesPushButtonClicked)
        self.noPushButton.clicked.connect(self.noPushButtonClicked)



        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Hook Execution Sequence Error"))
        self.yesPushButton.setText(_translate("Form", "Yes"))
        self.label.setText(_translate("Form", "There is another hook with that sequence number. Would you \n"
"like to override the sequence number and update the \n"
"sequencing for the reset of hooks within this hook collection?"))
        self.noPushButton.setText(_translate("Form", "No"))

    @pyqtSlot( )
    def yesPushButtonClicked( self ):
        self.label.setText("yesPushButtonClicked")

    @pyqtSlot( )
    def noPushButtonClicked( self ):
        self.label.setText("noPushButtonClicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
