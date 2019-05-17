# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/CreateEditHookCollectionOverlay.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_Form(QObject):
    def setupUi(self, Form):
    #The following is setting up the GUI, the widgets, their positioning, etc
        Form.setObjectName("Form")
        Form.resize(497, 402)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.hookCollectionNameLineEdit = QtWidgets.QLineEdit(Form)
        self.hookCollectionNameLineEdit.setObjectName("hookCollectionNameLineEdit")
        self.gridLayout.addWidget(self.hookCollectionNameLineEdit, 0, 1, 1, 3)
        self.executionSequenceLineEdit = QtWidgets.QLineEdit(Form)
        self.executionSequenceLineEdit.setObjectName("executionSequenceLineEdit")
        self.gridLayout.addWidget(self.executionSequenceLineEdit, 4, 1, 1, 3)
        self.descriptionLineEdit = QtWidgets.QLineEdit(Form)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.gridLayout.addWidget(self.descriptionLineEdit, 2, 1, 1, 3)
        self.statusComboBox = QtWidgets.QComboBox(Form)
        self.statusComboBox.setObjectName("statusComboBox")
        self.gridLayout.addWidget(self.statusComboBox, 3, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.cancelPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelPushButton.sizePolicy().hasHeightForWidth())
        self.cancelPushButton.setSizePolicy(sizePolicy)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.gridLayout.addWidget(self.cancelPushButton, 7, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hookCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.hookCheckBox.setObjectName("hookCheckBox")
        self.verticalLayout.addWidget(self.hookCheckBox)
        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 1)
        self.savePushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout.addWidget(self.savePushButton, 7, 4, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hookStatusComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.hookStatusComboBox.setObjectName("hookStatusComboBox")
        self.verticalLayout_2.addWidget(self.hookStatusComboBox)
        self.gridLayout.addWidget(self.groupBox_2, 5, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hookExecutionSequenceLineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.hookExecutionSequenceLineEdit.setObjectName("hookExecutionSequenceLineEdit")
        self.verticalLayout_3.addWidget(self.hookExecutionSequenceLineEdit)
        self.gridLayout.addWidget(self.groupBox_3, 5, 2, 1, 3)

        self.retranslateUi(Form)

    #set up the event listeners for each  widget
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
        self.savePushButton.clicked.connect(self.savePushButtonClicked)

        self.hookCollectionNameLineEdit.textEdited.connect(self.hookCollectionNameLineEdited)
        self.executionSequenceLineEdit.textEdited.connect(self.executionSequenceLineEdited)
        self.descriptionLineEdit.textEdited.connect(self.descriptionLineEdited)
        self.hookExecutionSequenceLineEdit.textEdited.connect(self.hookExecutionSequenceLineEdited)

        self.statusComboBox.currentIndexChanged.connect(self.statusComboBoxIndexChanged)
        self.hookStatusComboBox.currentIndexChanged.connect(self.hookStatusComboBoxIndexChanged)

        self.hookCheckBox.stateChanged.connect(self.hookCheckBoxStateChanged)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Execution Sequence"))
        self.label_2.setText(_translate("Form", "Description"))
        self.cancelPushButton.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Hook Collection Name"))
        self.label_3.setText(_translate("Form", "Status"))
        self.groupBox.setTitle(_translate("Form", "Hook"))
        self.hookCheckBox.setText(_translate("Form", "Hook 1"))
        self.savePushButton.setText(_translate("Form", "Save"))
        self.groupBox_2.setTitle(_translate("Form", "Status"))
        self.groupBox_3.setTitle(_translate("Form", "Hook Execution Sequence"))

# Push button Slots
    @pyqtSlot( )
    def cancelPushButtonClicked( self ):
        self.label.setText("cancelPushButtonClicked")

    @pyqtSlot( )
    def savePushButtonClicked( self ):
        self.label.setText("savePushButtonClicked")

# line edit Slots
    @pyqtSlot(str)
    def hookCollectionNameLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def executionSequenceLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def descriptionLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def hookExecutionSequenceLineEdited( self, text ):
        self.label.setText(text)

# Combo Box Slots
    @pyqtSlot(int)
    def statusComboBoxIndexChanged( self, index ):
        self.label.setText(str(index))

    @pyqtSlot(int)
    def hookStatusComboBoxIndexChanged( self, index ):
        self.label.setText(str(index))

# Check Box Slots
    @pyqtSlot(int)
    def hookCheckBoxStateChanged( self, state ):
        self.label.setText(str(state))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
