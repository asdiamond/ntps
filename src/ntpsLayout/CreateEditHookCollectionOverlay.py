# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/CreateEditHookCollectionOverlay.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Hook_Collection_Ui_Form(QObject):
    def setupUi(self, Form, hooks):
    #The following is setting up the GUI, the widgets, their positioning, etc
        self.hookCollectionData = None
        self.hooks = hooks
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
        self.statusComboBox.addItems(["Enabled", "Disabled"])
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

        self.hookGroupBox = QtWidgets.QGroupBox(Form)
        self.hookGridLayout = QtWidgets.QGridLayout(self.hookGroupBox)
        


        self.gridLayout.addWidget(self.hookGroupBox, 5, 0, 1, 1)
        self.savePushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.savePushButton, 7, 4, 1, 1)

        self.statusGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.statusGroupBox)

        
        self.gridLayout.addWidget(self.statusGroupBox, 5, 1, 1, 1)
        self.executionSequenceGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.executionSequenceGroupBox)

        
        self.gridLayout.addWidget(self.executionSequenceGroupBox, 5, 2, 1, 3)
        self.retranslateUi(Form)

        #create widgets for each hook in the system
        self.hookCheckBoxList = []
        self.hookStatusComboBoxList = []
        self.hookExecutionSequenceLineEditList = []
        i = 0
        for hook in hooks:
            self.hookCheckBox = QtWidgets.QCheckBox(self.hookGroupBox)
            self.hookCheckBoxList.append(self.hookCheckBox)
            self.hookLabel = QtWidgets.QLabel(self.hookGroupBox)
            self.hookLabel.setText(hook.get_name())
            self.hookGridLayout.addWidget(self.hookCheckBox, i, 0, 1, 1)
            self.hookGridLayout.addWidget(self.hookLabel, i, 1, 1, 1)

            self.hookStatusComboBox = QtWidgets.QComboBox(self.statusGroupBox)
            self.hookStatusComboBox.addItems(["Enabled", "Disabled"])
            self.hookStatusComboBoxList.append(self.hookStatusComboBox)
            self.verticalLayout_2.addWidget(self.hookStatusComboBox)

            self.hookExecutionSequenceLineEdit = QtWidgets.QLineEdit(self.executionSequenceGroupBox)
            self.hookExecutionSequenceLineEditList.append(self.hookExecutionSequenceLineEdit)
            self.verticalLayout_3.addWidget(self.hookExecutionSequenceLineEdit)
            i+=1



    #set up the event listeners for each  widget
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
        self.savePushButton.clicked.connect(self.savePushButtonClicked)

        self.hookCollectionNameLineEdit.textEdited.connect(self.hookCollectionNameLineEdited)
        self.executionSequenceLineEdit.textEdited.connect(self.executionSequenceLineEdited)
        self.descriptionLineEdit.textEdited.connect(self.descriptionLineEdited)
        self.hookExecutionSequenceLineEdit.textEdited.connect(self.hookExecutionSequenceLineEdited)

        self.statusComboBox.currentIndexChanged.connect(self.statusComboBoxIndexChanged)
        self.hookStatusComboBox.currentIndexChanged.connect(self.hookStatusComboBoxIndexChanged)


        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Execution Sequence"))
        self.label_2.setText(_translate("Form", "Description"))
        self.cancelPushButton.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Hook Collection Name"))
        self.label_3.setText(_translate("Form", "Status"))
        self.hookGroupBox.setTitle(_translate("Form", "Hook"))
        self.savePushButton.setText(_translate("Form", "Save"))
        self.statusGroupBox.setTitle(_translate("Form", "Status"))
        self.executionSequenceGroupBox.setTitle(_translate("Form", "Hook Execution Sequence"))

# Push button Slots
    @pyqtSlot( )
    def cancelPushButtonClicked( self ):
        self.label.setText("cancelPushButtonClicked")

    @pyqtSlot( )
    def savePushButtonClicked( self ):
        name = self.hookCollectionNameLineEdit.text()
        description = self.descriptionLineEdit.text()
        hooks = []
        i = 0
        for checkBox in self.hookCheckBoxList:
            if checkBox.isChecked():
                hooks.append(self.hooks[i])
            i+=1
        status = str(self.statusComboBox.currentText())
        executionSequence = self.executionSequenceLineEdit.text()
        self.hookCollectionData = [name, description, hooks, status, executionSequence]
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Hook_Collection_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
