# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/LivePacketViewArea.ui'
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
        Form.resize(1258, 572)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.interceptionBehaviorComboBox = QtWidgets.QComboBox(Form)
        self.interceptionBehaviorComboBox.setObjectName("interceptionBehaviorComboBox")
        self.gridLayout.addWidget(self.interceptionBehaviorComboBox, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.proxyBehaviorComboBox = QtWidgets.QComboBox(Form)
        self.proxyBehaviorComboBox.setObjectName("proxyBehaviorComboBox")
        self.gridLayout.addWidget(self.proxyBehaviorComboBox, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.queueSizeLineEdit = QtWidgets.QLineEdit(Form)
        self.queueSizeLineEdit.setObjectName("queueSizeLineEdit")
        self.gridLayout.addWidget(self.queueSizeLineEdit, 0, 10, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.packetAreaTabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.packetAreaTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.packetAreaTabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.packetAreaTabWidget.setObjectName("packetAreaTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dissectedListWidget = QtWidgets.QListWidget(self.tab)
        self.dissectedListWidget.setObjectName("dissectedListWidget")
        item = QtWidgets.QListWidgetItem()
        self.dissectedListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.dissectedListWidget.addItem(item)
        self.horizontalLayout_2.addWidget(self.dissectedListWidget)
        self.packetAreaTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.binaryTextEdit = QtWidgets.QTextEdit(self.tab_2)
        self.binaryTextEdit.setObjectName("binaryTextEdit")
        self.verticalLayout.addWidget(self.binaryTextEdit)
        self.packetAreaTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hexTextEdit = QtWidgets.QTextEdit(self.tab_3)
        self.hexTextEdit.setObjectName("hexTextEdit")
        self.verticalLayout_3.addWidget(self.hexTextEdit)
        self.packetAreaTabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.packetAreaTabWidget)
        self.clearPacketAreaPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.clearPacketAreaPushButton.setObjectName("clearPacketAreaPushButton")
        self.horizontalLayout.addWidget(self.clearPacketAreaPushButton)
        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 10)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.forwardPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.forwardPushButton.setObjectName("forwardPushButton")
        self.gridLayout_3.addWidget(self.forwardPushButton, 1, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 0, 1, 2)
        self.saveModificationPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.saveModificationPushButton.setObjectName("saveModificationPushButton")
        self.gridLayout_3.addWidget(self.saveModificationPushButton, 1, 2, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.maskLabel = QtWidgets.QLabel(self.groupBox_7)
        self.maskLabel.setObjectName("maskLabel")
        self.verticalLayout_5.addWidget(self.maskLabel)
        self.gridLayout_3.addWidget(self.groupBox_7, 0, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.valueLineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.valueLineEdit.setObjectName("valueLineEdit")
        self.verticalLayout_4.addWidget(self.valueLineEdit)
        self.gridLayout_3.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.fieldLineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.fieldLineEdit.setObjectName("fieldLineEdit")
        self.gridLayout_5.addWidget(self.fieldLineEdit, 0, 1, 1, 1)
        self.fieldCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.fieldCheckBox.setText("")
        self.fieldCheckBox.setObjectName("fieldCheckBox")
        self.gridLayout_5.addWidget(self.fieldCheckBox, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.dropPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.dropPushButton.setObjectName("dropPushButton")
        self.gridLayout_3.addWidget(self.dropPushButton, 1, 4, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.displayFormatComboBox = QtWidgets.QComboBox(self.groupBox_8)
        self.displayFormatComboBox.setObjectName("displayFormatComboBox")
        self.verticalLayout_6.addWidget(self.displayFormatComboBox)
        self.gridLayout_3.addWidget(self.groupBox_8, 0, 3, 1, 2)
        self.gridLayout.addWidget(self.groupBox_3, 3, 1, 1, 5)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.captureFilterLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.captureFilterLineEdit.setObjectName("captureFilterLineEdit")
        self.gridLayout_2.addWidget(self.captureFilterLineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.clearFilterPushButton = QtWidgets.QPushButton(self.groupBox)
        self.clearFilterPushButton.setObjectName("clearFilterPushButton")
        self.gridLayout_2.addWidget(self.clearFilterPushButton, 0, 4, 1, 1)
        self.applyFilterPushButton = QtWidgets.QPushButton(self.groupBox)
        self.applyFilterPushButton.setObjectName("applyFilterPushButton")
        self.gridLayout_2.addWidget(self.applyFilterPushButton, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 10)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addPushButton = QtWidgets.QPushButton(self.widget)
        self.addPushButton.setObjectName("addPushButton")
        self.verticalLayout_2.addWidget(self.addPushButton)
        self.removePushButton = QtWidgets.QPushButton(self.widget)
        self.removePushButton.setObjectName("removePushButton")
        self.verticalLayout_2.addWidget(self.removePushButton)
        self.gridLayout.addWidget(self.widget, 3, 6, 1, 4)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.minimumLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.minimumLineEdit.setObjectName("minimumLineEdit")
        self.gridLayout_4.addWidget(self.minimumLineEdit, 3, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)
        self.maximumLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.maximumLineEdit.setObjectName("maximumLineEdit")
        self.gridLayout_4.addWidget(self.maximumLineEdit, 4, 1, 1, 2)
        self.stopFuzzPushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.stopFuzzPushButton.setObjectName("stopFuzzPushButton")
        self.gridLayout_4.addWidget(self.stopFuzzPushButton, 5, 2, 1, 1)
        self.fuzzPushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.fuzzPushButton.setObjectName("fuzzPushButton")
        self.gridLayout_4.addWidget(self.fuzzPushButton, 5, 1, 1, 1)
        self.expectedReturnTypeLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.expectedReturnTypeLineEdit.setObjectName("expectedReturnTypeLineEdit")
        self.gridLayout_4.addWidget(self.expectedReturnTypeLineEdit, 2, 1, 1, 2)
        self.selectedFieldNameLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.selectedFieldNameLineEdit.setObjectName("selectedFieldNameLineEdit")
        self.gridLayout_4.addWidget(self.selectedFieldNameLineEdit, 1, 1, 1, 2)
        self.selectedPacketNameLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.selectedPacketNameLineEdit.setObjectName("selectedPacketNameLineEdit")
        self.gridLayout_4.addWidget(self.selectedPacketNameLineEdit, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox_4, 3, 10, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 9, 1, 1)

        self.retranslateUi(Form)

    #set up the event listeners for each  widget

        self.clearPacketAreaPushButton.clicked.connect(self.clearPacketAreaPushButtonClicked)
        self.saveModificationPushButton.clicked.connect(self.saveModificationPushButtonClicked)
        self.dropPushButton.clicked.connect(self.dropPushButtonClicked)
        self.clearFilterPushButton.clicked.connect(self.clearFilterPushButtonClicked)
        self.applyFilterPushButton.clicked.connect(self.applyFilterPushButtonClicked)
        self.addPushButton.clicked.connect(self.addPushButtonClicked)
        self.removePushButton.clicked.connect(self.removePushButtonClicked)
        self.stopFuzzPushButton.clicked.connect(self.stopFuzzPushButtonClicked)
        self.fuzzPushButton.clicked.connect(self.fuzzPushButtonClicked)
        self.forwardPushButton.clicked.connect(self.forwardPushButtonClicked)

        self.queueSizeLineEdit.textEdited.connect(self.queueSizeLineEdited)
        self.valueLineEdit.textEdited.connect(self.valueLineEdited)
        self.fieldLineEdit.textEdited.connect(self.fieldLineEdited)
        self.captureFilterLineEdit.textEdited.connect(self.captureFilterLineEdited)
        self.minimumLineEdit.textEdited.connect(self.minimumLineEdited)
        self.maximumLineEdit.textEdited.connect(self.maximumLineEdited)
        self.expectedReturnTypeLineEdit.textEdited.connect(self.expectedReturnTypeLineEdited)
        self.selectedFieldNameLineEdit.textEdited.connect(self.selectedFieldNameLineEdited)
        self.selectedPacketNameLineEdit.textEdited.connect(self.selectedPacketNameLineEdited)

        self.interceptionBehaviorComboBox.currentIndexChanged.connect(self.interceptionBehaviorComboBoxIndexChanged)
        self.proxyBehaviorComboBox.currentIndexChanged.connect(self.proxyBehaviorComboBoxIndexChanged)
        self.displayFormatComboBox.currentIndexChanged.connect(self.displayFormatComboBoxIndexChanged)

        self.fieldCheckBox.stateChanged.connect(self.fieldCheckBoxStateChanged)

        self.binaryTextEdit.textChanged.connect(self.binaryTextEditChanged)
        self.hexTextEdit.textChanged.connect(self.hexTextEditChanged)

        self.packetAreaTabWidget.currentChanged.connect(self.packetAreaTabWidgetChanged)

        self.dissectedListWidget.itemClicked.connect(self.dissectedListWidgetItemClicked)


        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Interception Behavior"))
        self.label.setText(_translate("Form", "Proxy Behavior"))
        self.groupBox_2.setTitle(_translate("Form", "Packet Area"))
        __sortingEnabled = self.dissectedListWidget.isSortingEnabled()
        self.dissectedListWidget.setSortingEnabled(False)
        item = self.dissectedListWidget.item(0)
        item.setText(_translate("Form", "Frame 718: frame, eth, ip, tcp"))
        item = self.dissectedListWidget.item(1)
        item.setText(_translate("Form", "Frame 767: frame, eth, ip, tcp"))
        self.dissectedListWidget.setSortingEnabled(__sortingEnabled)
        self.packetAreaTabWidget.setTabText(self.packetAreaTabWidget.indexOf(self.tab), _translate("Form", "Dissected"))
        self.binaryTextEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\\x00\\x02\\x157\\xa2D\\x00\\xae\\fx3R\\xaa\\xd1\\x08\\x00E\\x00\\x01\\x00\\x00@\\x06&lt;\\xc0</p></body></html>"))
        self.packetAreaTabWidget.setTabText(self.packetAreaTabWidget.indexOf(self.tab_2), _translate("Form", "Binary"))
        self.hexTextEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00 02 15 37 A2 44 AE F3 52 AA D1 08 00 45 00 ...7.D...R...E</p></body></html>"))
        self.packetAreaTabWidget.setTabText(self.packetAreaTabWidget.indexOf(self.tab_3), _translate("Form", "HEX"))
        self.clearPacketAreaPushButton.setText(_translate("Form", "Clear"))
        self.groupBox_3.setTitle(_translate("Form", "Field Area"))
        self.forwardPushButton.setText(_translate("Form", "Forward"))
        self.label_20.setText(_translate("Form", "Field Name, value, and display format are editable fields"))
        self.saveModificationPushButton.setText(_translate("Form", "Save Modification"))
        self.groupBox_7.setTitle(_translate("Form", "Mask"))
        self.maskLabel.setText(_translate("Form", "0"))
        self.groupBox_6.setTitle(_translate("Form", "Value"))
        self.valueLineEdit.setText(_translate("Form", "08"))
        self.groupBox_5.setTitle(_translate("Form", "FieldName"))
        self.fieldLineEdit.setText(_translate("Form", "icmp.type"))
        self.dropPushButton.setText(_translate("Form", "Drop"))
        self.groupBox_8.setTitle(_translate("Form", "Display Format"))
        self.groupBox.setTitle(_translate("Form", "Capture Filter"))
        self.label_4.setText(_translate("Form", "FIlter"))
        self.clearFilterPushButton.setText(_translate("Form", "Clear"))
        self.applyFilterPushButton.setText(_translate("Form", "Apply"))
        self.addPushButton.setText(_translate("Form", "+"))
        self.removePushButton.setText(_translate("Form", "-"))
        self.groupBox_4.setTitle(_translate("Form", "Fuzzing Area"))
        self.label_7.setText(_translate("Form", "Expected Return Type"))
        self.label_5.setText(_translate("Form", "Selected Packet Name"))
        self.label_6.setText(_translate("Form", "Selected Field Name"))
        self.label_9.setText(_translate("Form", "Maximum"))
        self.label_8.setText(_translate("Form", "Minimum"))
        self.stopFuzzPushButton.setText(_translate("Form", "Stop"))
        self.fuzzPushButton.setText(_translate("Form", "Fuzz"))
        self.label_3.setText(_translate("Form", "Queue Size"))

# Push button slots
    @pyqtSlot( )
    def clearPacketAreaPushButtonClicked( self ):
        self.label.setText("clearPacketAreaPushButtonClicked")

    @pyqtSlot( )
    def saveModificationPushButtonClicked( self ):
        self.label.setText("saveModificationPushButtonClicked")

    @pyqtSlot( )
    def dropPushButtonClicked( self ):
        self.label.setText("dropPushButtonClicked")

    @pyqtSlot( )
    def clearFilterPushButtonClicked( self ):
        self.label.setText("clearFilterPushButtonClicked")

    @pyqtSlot( )
    def applyFilterPushButtonClicked( self ):
        self.label.setText("applyFilterPushButtonClicked")

    @pyqtSlot( )
    def addPushButtonClicked( self ):
        self.label.setText("addPushButtonClicked")

    @pyqtSlot( )
    def removePushButtonClicked( self ):
        self.label.setText("cancelPushButtonClicked")

    @pyqtSlot( )
    def stopFuzzPushButtonClicked( self ):
        self.label.setText("stopFuzzPushButtonClicked")

    @pyqtSlot( )
    def fuzzPushButtonClicked( self ):
        self.label.setText("fuzzPushButtonClicked")

    @pyqtSlot( )
    def forwardPushButtonClicked( self ):
        self.label.setText("forwardPushButtonClicked")

# Line Edit Slots
    @pyqtSlot(str)
    def queueSizeLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def valueLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def captureFilterLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def fieldLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def minimumLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def maximumLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def expectedReturnTypeLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def selectedFieldNameLineEdited( self, text ):
        self.label.setText(text)

    @pyqtSlot(str)
    def selectedPacketNameLineEdited( self, text ):
        self.label.setText(text)

# Combo Box Slots
    @pyqtSlot(int)
    def interceptionBehaviorComboBoxIndexChanged( self, index ):
        self.label.setText(str(index))

    @pyqtSlot(int)
    def proxyBehaviorComboBoxIndexChanged( self, index ):
        self.label.setText(str(index))

    @pyqtSlot(int)
    def displayFormatComboBoxIndexChanged( self, index ):
        self.label.setText(str(index))

# Check Box Slots
    @pyqtSlot(int)
    def fieldCheckBoxStateChanged( self, state ):
        self.label.setText(str(state))

# Text Edit Slots
    @pyqtSlot( )
    def binaryTextEditChanged( self ):
        self.label.setText(self.binaryTextEdit.toPlainText())

    @pyqtSlot( )
    def hexTextEditChanged( self ):
        self.label.setText(self.hexTextEdit.toPlainText())

# Tab Widget Slots
    @pyqtSlot(int)
    def packetAreaTabWidgetChanged( self, index ):
        self.label.setText(str(index))

# List Widget Slots
    @pyqtSlot()
    def dissectedListWidgetItemClicked( self ):
        self.label.setText("dissectedListWidgetItemClicked")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
