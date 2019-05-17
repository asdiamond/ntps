# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/adiaz/Documents/CS4311/ntps/GUIForms/UI/Layout.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys

sys.path.extend(['/root/ntps'])
from src.integration_test.integration import int_test
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QObject, pyqtSlot
from PCAPFileManager import *
from CreateEditHookOverlay import *
from CreateEditHookCollectionOverlay import *
from src.HookSubsystem.Hook import *
from src.HookSubsystem.HookManager import *
from src.HookCollectionSubsystem.HookCollectionManager import *


class Ui_Form(QObject):
    def setupUi(self, Form):
    # HOOKS
        self.hookManager = HookManager()
        self.hookCollectionManager = HookCollectionManager()
    # Create physical aspects of widgets
        self.form = Form
        self.PCAPDissectedModel = None
        self.PCAPBinaryModel = None
        self.PCAPHEXModel = None
        self.livePacketDissectedListView = None
        self.livePacketBinaryListView = None
        self.livePacketHEXListView = None

        Form.setObjectName("Form")
        Form.resize(1368, 707)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.contentViewTabWidget = QtWidgets.QTabWidget(Form)
        self.contentViewTabWidget.setObjectName("contentViewTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.groupBox_23 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_23.setObjectName("groupBox_23")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.groupBox_23)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.hookPropertiesTableView = QtWidgets.QTableView(self.groupBox_23)
        self.hookPropertiesTableView.setObjectName("hookPropertiesTableView")
        self.verticalLayout_16.addWidget(self.hookPropertiesTableView)
        self.gridLayout_18.addWidget(self.groupBox_23, 1, 1, 1, 6)
        self.hookSearchLineEdit = QtWidgets.QLineEdit(self.tab)
        self.hookSearchLineEdit.setObjectName("hookSearchLineEdit")
        self.gridLayout_18.addWidget(self.hookSearchLineEdit, 0, 6, 1, 1)
        self.hookDeletePushButton = QtWidgets.QPushButton(self.tab)
        self.hookDeletePushButton.setObjectName("hookDeletePushButton")
        self.gridLayout_18.addWidget(self.hookDeletePushButton, 0, 4, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setObjectName("label_33")
        self.gridLayout_18.addWidget(self.label_33, 0, 5, 1, 1)
        self.hookEditPushButton = QtWidgets.QPushButton(self.tab)
        self.hookEditPushButton.setObjectName("hookEditPushButton")
        self.gridLayout_18.addWidget(self.hookEditPushButton, 0, 3, 1, 1)
        self.hookAddPushButton = QtWidgets.QPushButton(self.tab)
        self.hookAddPushButton.setObjectName("hookAddPushButton")
        self.gridLayout_18.addWidget(self.hookAddPushButton, 0, 2, 1, 1)
        self.contentViewTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_24.setObjectName("groupBox_24")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_24)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.hookCollectionPropertiesTableView = QtWidgets.QTableView(self.groupBox_24)
        self.verticalLayout_17.addWidget(self.hookCollectionPropertiesTableView)
        self.gridLayout_19.addWidget(self.groupBox_24, 1, 1, 1, 6)
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setObjectName("label_34")
        self.gridLayout_19.addWidget(self.label_34, 0, 5, 1, 1)
        self.hookCollectionEditPushButton = QtWidgets.QPushButton(self.tab_2)
        self.hookCollectionEditPushButton.setObjectName("hookCollectionEditPushButton")
        self.gridLayout_19.addWidget(self.hookCollectionEditPushButton, 0, 3, 1, 1)
        self.hookCollectionDeletePushButton = QtWidgets.QPushButton(self.tab_2)
        self.hookCollectionDeletePushButton.setObjectName("hookCollectionDeletePushButton")
        self.gridLayout_19.addWidget(self.hookCollectionDeletePushButton, 0, 4, 1, 1)
        self.hookCollectionSearchLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.hookCollectionSearchLineEdit.setObjectName("hookCollectionSearchLineEdit")
        self.gridLayout_19.addWidget(self.hookCollectionSearchLineEdit, 0, 6, 1, 1)
        self.hookCollectionAddPushButton = QtWidgets.QPushButton(self.tab_2)
        self.hookCollectionAddPushButton.setObjectName("hookCollectionAddPushButton")
        self.gridLayout_19.addWidget(self.hookCollectionAddPushButton, 0, 2, 1, 1)
        self.contentViewTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_17.addWidget(self.label_24, 0, 0, 1, 1)
        self.livePacketProxyBehaviorComboBox = QtWidgets.QComboBox(self.tab_3)
        self.livePacketProxyBehaviorComboBox.setObjectName("livePacketProxyBehaviorComboBox")
        self.livePacketProxyBehaviorComboBox.addItems(["Off", "On"])
        self.gridLayout_17.addWidget(self.livePacketProxyBehaviorComboBox, 0, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_17.addWidget(self.label_26, 0, 2, 1, 1)
        self.livePacketInterceptionBehaviorComboBox = QtWidgets.QComboBox(self.tab_3)
        self.livePacketInterceptionBehaviorComboBox.setObjectName("livePacketInterceptionBehaviorComboBox")
        self.livePacketInterceptionBehaviorComboBox.addItems(["Off", "On"])
        self.livePacketInterceptionBehaviorComboBox.setEnabled(False)

        self.gridLayout_17.addWidget(self.livePacketInterceptionBehaviorComboBox, 0, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_17.addWidget(self.label_23, 0, 4, 1, 1)
        self.livePacketQueueSizeLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.livePacketQueueSizeLineEdit.setObjectName("livePacketQueueSizeLineEdit")
        self.livePacketQueueSizeLineEdit.setText('100')
        self.gridLayout_17.addWidget(self.livePacketQueueSizeLineEdit, 0, 5, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.livePacketCaptureFilterLineEdit = QtWidgets.QLineEdit(self.groupBox_14)
        self.livePacketCaptureFilterLineEdit.setObjectName("livePacketCaptureFilterLineEdit")
        self.gridLayout_13.addWidget(self.livePacketCaptureFilterLineEdit, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_14)
        self.label_25.setObjectName("label_25")
        self.gridLayout_13.addWidget(self.label_25, 0, 0, 1, 1)
        self.livePacketClearFilterPushButton = QtWidgets.QPushButton(self.groupBox_14)
        self.livePacketClearFilterPushButton.setObjectName("livePacketClearFilterPushButton")
        self.gridLayout_13.addWidget(self.livePacketClearFilterPushButton, 0, 4, 1, 1)
        self.livePacketApplyFilterPushButton = QtWidgets.QPushButton(self.groupBox_14)
        self.livePacketApplyFilterPushButton.setObjectName("livePacketApplyFilterPushButton")
        self.gridLayout_13.addWidget(self.livePacketApplyFilterPushButton, 0, 3, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_14, 1, 0, 1, 6)
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_15.setObjectName("groupBox_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.livePacketTabWidget = QtWidgets.QTabWidget(self.groupBox_15)
        self.livePacketTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.livePacketTabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.livePacketTabWidget.setObjectName("livePacketTabWidget")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.livePacketDissectedListView = QtWidgets.QListView(self.tab_11)
        self.livePacketDissectedListView.setObjectName("livePacketDissectedListView")

        self.horizontalLayout_10.addWidget(self.livePacketDissectedListView)
        self.livePacketTabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.livePacketBinaryListView = QtWidgets.QListView(self.tab_12)
        self.livePacketBinaryListView.setObjectName("livePacketBinaryListView")

        self.gridLayout_20.addWidget(self.livePacketBinaryListView, 0, 0, 1, 1)
        self.livePacketTabWidget.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.livePacketHEXListView = QtWidgets.QListView(self.tab_13)
        self.livePacketHEXListView.setObjectName("livePacketHEXListView")

        self.gridLayout_21.addWidget(self.livePacketHEXListView, 0, 0, 1, 1)
        self.livePacketTabWidget.addTab(self.tab_13, "")
        self.horizontalLayout_9.addWidget(self.livePacketTabWidget)
        self.livePacketClearAreaPushButton = QtWidgets.QPushButton(self.groupBox_15)
        self.livePacketClearAreaPushButton.setObjectName("livePacketClearAreaPushButton")
        self.horizontalLayout_9.addWidget(self.livePacketClearAreaPushButton)
        self.gridLayout_17.addWidget(self.groupBox_15, 2, 0, 1, 6)
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.livePacketForwardPushButton = QtWidgets.QPushButton(self.groupBox_17)
        self.livePacketForwardPushButton.setObjectName("livePacketForwardPushButton")
        self.gridLayout_15.addWidget(self.livePacketForwardPushButton, 1, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_17)
        self.label_32.setObjectName("label_32")
        self.gridLayout_15.addWidget(self.label_32, 1, 0, 1, 2)
        self.livePacketSaveModificationPushButton = QtWidgets.QPushButton(self.groupBox_17)
        self.livePacketSaveModificationPushButton.setObjectName("livePacketSaveModificationPushButton")
        self.gridLayout_15.addWidget(self.livePacketSaveModificationPushButton, 1, 2, 1, 1)
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_18.setObjectName("groupBox_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_18)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.maskLabel_3 = QtWidgets.QLabel(self.groupBox_18)
        self.maskLabel_3.setObjectName("maskLabel_3")
        self.verticalLayout_12.addWidget(self.maskLabel_3)
        self.gridLayout_15.addWidget(self.groupBox_18, 0, 2, 1, 1)

        self.livePacketDropPacketPushButton = QtWidgets.QPushButton(self.groupBox_17)
        self.livePacketDropPacketPushButton.setObjectName("livePacketDropPacketPushButton")
        self.gridLayout_15.addWidget(self.livePacketDropPacketPushButton, 1, 4, 1, 1)
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_21.setObjectName("groupBox_21")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_21)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.livePacketDisplayFormatComboBox = QtWidgets.QComboBox(self.groupBox_21)
        self.livePacketDisplayFormatComboBox.setObjectName("livePacketDisplayFormatComboBox")
        self.verticalLayout_14.addWidget(self.livePacketDisplayFormatComboBox)
        self.gridLayout_15.addWidget(self.groupBox_21, 0, 3, 1, 2)
        self.gridLayout_17.addWidget(self.groupBox_17, 3, 0, 1, 4)
        self.widget_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.livePacketAddFieldPushButton = QtWidgets.QPushButton(self.widget_2)
        self.livePacketAddFieldPushButton.setObjectName("livePacketAddFieldPushButton")
        self.verticalLayout_10.addWidget(self.livePacketAddFieldPushButton)
        self.livePacketRemoveFieldPushButton = QtWidgets.QPushButton(self.widget_2)
        self.livePacketRemoveFieldPushButton.setObjectName("livePacketRemoveFieldPushButton")
        self.verticalLayout_10.addWidget(self.livePacketRemoveFieldPushButton)
        self.gridLayout_17.addWidget(self.widget_2, 3, 4, 1, 1)
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_27 = QtWidgets.QLabel(self.groupBox_16)
        self.label_27.setObjectName("label_27")
        self.gridLayout_14.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_16)
        self.label_28.setObjectName("label_28")
        self.gridLayout_14.addWidget(self.label_28, 0, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_16)
        self.label_29.setObjectName("label_29")
        self.gridLayout_14.addWidget(self.label_29, 1, 0, 1, 1)
        self.livePacketMinimumLineEdit = QtWidgets.QLineEdit(self.groupBox_16)
        self.livePacketMinimumLineEdit.setObjectName("livePacketMinimumLineEdit")
        self.gridLayout_14.addWidget(self.livePacketMinimumLineEdit, 3, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.groupBox_16)
        self.label_30.setObjectName("label_30")
        self.gridLayout_14.addWidget(self.label_30, 4, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_16)
        self.label_31.setObjectName("label_31")
        self.gridLayout_14.addWidget(self.label_31, 3, 0, 1, 1)
        self.livePacketMaximumLineEdit = QtWidgets.QLineEdit(self.groupBox_16)
        self.livePacketMaximumLineEdit.setObjectName("livePacketMaximumLineEdit")
        self.gridLayout_14.addWidget(self.livePacketMaximumLineEdit, 4, 1, 1, 2)
        self.livePacketStopFuzzingPushButton = QtWidgets.QPushButton(self.groupBox_16)
        self.livePacketStopFuzzingPushButton.setObjectName("livePacketStopFuzzingPushButton")
        self.gridLayout_14.addWidget(self.livePacketStopFuzzingPushButton, 5, 2, 1, 1)
        self.livePacketFuzzPushButton = QtWidgets.QPushButton(self.groupBox_16)
        self.livePacketFuzzPushButton.setObjectName("livePacketFuzzPushButton")
        self.gridLayout_14.addWidget(self.livePacketFuzzPushButton, 5, 1, 1, 1)
        self.livePacketExpectedReturnTypeLineEdit = QtWidgets.QLineEdit(self.groupBox_16)
        self.livePacketExpectedReturnTypeLineEdit.setObjectName("livePacketExpectedReturnTypeLineEdit")
        self.gridLayout_14.addWidget(self.livePacketExpectedReturnTypeLineEdit, 2, 1, 1, 2)
        self.livePacketSelectedFieldNameLineEdit = QtWidgets.QLineEdit(self.groupBox_16)
        self.livePacketSelectedFieldNameLineEdit.setObjectName("livePacketSelectedFieldNameLineEdit")
        self.gridLayout_14.addWidget(self.livePacketSelectedFieldNameLineEdit, 1, 1, 1, 2)
        self.livePacketSelectedPacketNameLineEdit = QtWidgets.QLineEdit(self.groupBox_16)
        self.livePacketSelectedPacketNameLineEdit.setObjectName("livePacketSelectedPacketNameLineEdit")
        self.gridLayout_14.addWidget(self.livePacketSelectedPacketNameLineEdit, 0, 1, 1, 2)
        self.gridLayout_17.addWidget(self.groupBox_16, 3, 5, 1, 1)
        self.contentViewTabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1)
        self.packetFromPCAPProxyBehaviorComboBox = QtWidgets.QComboBox(self.tab_4)
        self.packetFromPCAPProxyBehaviorComboBox.setObjectName("packetFromPCAPProxyBehaviorComboBox")
        self.packetFromPCAPProxyBehaviorComboBox.addItems(["Off", "On"])
        self.gridLayout_12.addWidget(self.packetFromPCAPProxyBehaviorComboBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 0, 2, 1, 1)
        self.packetFromPCAPInterceptionBehaviorComboBox = QtWidgets.QComboBox(self.tab_4)
        self.packetFromPCAPInterceptionBehaviorComboBox.setObjectName("packetFromPCAPInterceptionBehaviorComboBox")
        self.packetFromPCAPInterceptionBehaviorComboBox.addItems(["Off", "On"])
        self.gridLayout_12.addWidget(self.packetFromPCAPInterceptionBehaviorComboBox, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 0, 4, 1, 1)
        self.packetFromPCAPQueueSizeLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.packetFromPCAPQueueSizeLineEdit.setObjectName("packetFromPCAPQueueSizeLineEdit")
        self.packetFromPCAPQueueSizeLineEdit.setText('100')
        self.gridLayout_12.addWidget(self.packetFromPCAPQueueSizeLineEdit, 0, 5, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.packetFromPCAPFileLineEdit = QtWidgets.QLineEdit(self.groupBox_9)
        self.packetFromPCAPFileLineEdit.setObjectName("packetFromPCAPFileLineEdit")
        self.gridLayout_8.addWidget(self.packetFromPCAPFileLineEdit, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_9)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 0, 0, 1, 1)
        self.packetFromPCAPOpenFilePushButton = QtWidgets.QPushButton(self.groupBox_9)
        self.packetFromPCAPOpenFilePushButton.setObjectName("packetFromPCAPOpenFilePushButton")
        self.gridLayout_8.addWidget(self.packetFromPCAPOpenFilePushButton, 0, 3, 1, 1)
        self.packetFromPCAPCancelFilePushButton = QtWidgets.QPushButton(self.groupBox_9)
        self.packetFromPCAPCancelFilePushButton.setObjectName("packetFromPCAPCancelFilePushButton")
        self.gridLayout_8.addWidget(self.packetFromPCAPCancelFilePushButton, 0, 4, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_9, 1, 0, 1, 6)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.packetFromPCAPCaptureFilterLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.packetFromPCAPCaptureFilterLineEdit.setObjectName("packetFromPCAPCaptureFilterLineEdit")
        self.gridLayout_11.addWidget(self.packetFromPCAPCaptureFilterLineEdit, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setObjectName("label_22")
        self.gridLayout_11.addWidget(self.label_22, 0, 0, 1, 1)
        self.packetFromPCAPApplyCaptureFilterPushButton = QtWidgets.QPushButton(self.groupBox)
        self.packetFromPCAPApplyCaptureFilterPushButton.setObjectName("packetFromPCAPApplyCaptureFilterPushButton")
        self.gridLayout_11.addWidget(self.packetFromPCAPApplyCaptureFilterPushButton, 0, 3, 1, 1)
        self.packetFromPCAPClearCaptureFilterPushButton = QtWidgets.QPushButton(self.groupBox)
        self.packetFromPCAPClearCaptureFilterPushButton.setObjectName("packetFromPCAPClearCaptureFilterPushButton")
        self.gridLayout_11.addWidget(self.packetFromPCAPClearCaptureFilterPushButton, 0, 4, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox, 2, 0, 1, 6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.packetFromPCAPTabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.packetFromPCAPTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.packetFromPCAPTabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.packetFromPCAPTabWidget.setObjectName("packetFromPCAPTabWidget")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_14)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.packetFromPCAPDissectedTreeView = QtWidgets.QTreeView(self.tab_14)
        self.packetFromPCAPDissectedTreeView.setObjectName("packetFromPCAPDissectedTreeView")
        self.horizontalLayout_11.addWidget(self.packetFromPCAPDissectedTreeView)
        self.packetFromPCAPTabWidget.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_15)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.packetFromPCAPBinaryListView = QtWidgets.QListView(self.tab_15)
        self.packetFromPCAPBinaryListView.setObjectName("packetFromPCAPBinaryListView")

        self.gridLayout_22.addWidget(self.packetFromPCAPBinaryListView, 0, 0, 1, 1)
        self.packetFromPCAPTabWidget.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.packetFromPCAPHEXListView = QtWidgets.QListView(self.tab_16)
        self.packetFromPCAPHEXListView.setObjectName("packetFromPCAPHEXListView")

        self.gridLayout_23.addWidget(self.packetFromPCAPHEXListView, 0, 0, 1, 1)
        self.packetFromPCAPTabWidget.addTab(self.tab_16, "")
        self.gridLayout_2.addWidget(self.packetFromPCAPTabWidget, 0, 1, 1, 1)
        self.packetFromPCAPClearPacketAreaPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.packetFromPCAPClearPacketAreaPushButton.setObjectName("packetFromPCAPClearPacketAreaPushButton")
        self.gridLayout_2.addWidget(self.packetFromPCAPClearPacketAreaPushButton, 0, 2, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_2, 3, 0, 1, 6)

        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setMaximumHeight(1000)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.packetFromPCAPForwardPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.packetFromPCAPForwardPushButton.setObjectName("packetFromPCAPForwardPushButton")
        self.gridLayout_6.addWidget(self.packetFromPCAPForwardPushButton, 1, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 1, 0, 1, 2)
        self.packetFromPCAPSaveModificationPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.packetFromPCAPSaveModificationPushButton.setObjectName("packetFromPCAPSaveModificationPushButton")
        self.gridLayout_6.addWidget(self.packetFromPCAPSaveModificationPushButton, 1, 2, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.maskLabel_2 = QtWidgets.QLabel(self.groupBox_10)
        self.maskLabel_2.setObjectName("maskLabel_2")
        self.verticalLayout_7.addWidget(self.maskLabel_2)
        self.gridLayout_6.addWidget(self.groupBox_10, 0, 2, 1, 1)






        #SECTION: Live Traffic Group box values
        self.liveTrafficValueGroupBox = QtWidgets.QGroupBox(self.groupBox_17)
        
        self.liveTrafficValueGridLayout = QtWidgets.QGridLayout()
        self.liveTrafficValueGroupBox.setLayout(self.liveTrafficValueGridLayout)

        self.liveTrafficValueScrollArea = QtWidgets.QScrollArea()
        self.liveTrafficValueScrollArea.setWidgetResizable(True)
        self.liveTrafficValueScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.liveTrafficValueGridLayout.addWidget(self.liveTrafficValueScrollArea)

        self.liveTrafficValueWidget = QtWidgets.QWidget()
        self.liveTrafficValueWidgetVerticalLayout = QtWidgets.QVBoxLayout()
        self.liveTrafficValueWidget.setLayout(self.liveTrafficValueWidgetVerticalLayout)

        self.liveTrafficValueScrollArea.setWidget(self.liveTrafficValueWidget)

        self.gridLayout_15.addWidget(self.liveTrafficValueGroupBox, 0, 1, 1, 1)


        #SECTION: Live Traffic Group box Field Names
        self.livePacketFieldNamesGroupBox = QtWidgets.QGroupBox(self.groupBox_17)
        self.livePacketFieldNamesGridLayout = QtWidgets.QGridLayout()
        self.livePacketFieldNamesGroupBox.setLayout(self.livePacketFieldNamesGridLayout)

        self.livePacketFieldNamesScrollArea = QtWidgets.QScrollArea()
        self.livePacketFieldNamesScrollArea.setWidgetResizable(True)
        self.livePacketFieldNamesScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)


        self.livePacketFieldNamesGridLayout.addWidget(self.livePacketFieldNamesScrollArea)

        self.livePacketFieldNamesWidget = QtWidgets.QWidget()
        self.livePacketFieldNamesWidgetGridLayout = QtWidgets.QGridLayout()
        self.livePacketFieldNamesWidget.setLayout(self.livePacketFieldNamesWidgetGridLayout)

        self.livePacketFieldNamesScrollArea.setWidget(self.livePacketFieldNamesWidget)
        self.gridLayout_15.addWidget(self.livePacketFieldNamesGroupBox, 0, 0, 1, 1)





        #SECTION: PCAP Group box values
        self.PCAPValueGroupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.PCAPValueGridLayout = QtWidgets.QGridLayout()
        self.PCAPValueGroupBox.setLayout(self.PCAPValueGridLayout)

        self.PCAPValueScrollArea = QtWidgets.QScrollArea()
        self.PCAPValueScrollArea.setWidgetResizable(True)
        self.PCAPValueScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)


        self.PCAPValueGridLayout.addWidget(self.PCAPValueScrollArea)

        self.PCAPValueWidget = QtWidgets.QWidget()
        self.PCAPValueWidgetVerticalLayout = QtWidgets.QVBoxLayout()
        self.PCAPValueWidget.setLayout(self.PCAPValueWidgetVerticalLayout)

        self.PCAPValueScrollArea.setWidget(self.PCAPValueWidget)

        self.gridLayout_6.addWidget(self.PCAPValueGroupBox, 0, 1, 1, 1)

        #SECTION: PCAP Group box Field Names
        self.PCAPFieldNamesGroupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.PCAPFieldNamesGridLayout = QtWidgets.QGridLayout()
        self.PCAPFieldNamesGroupBox.setLayout(self.PCAPFieldNamesGridLayout)

        self.PCAPFieldNamesScrollArea = QtWidgets.QScrollArea()
        self.PCAPFieldNamesScrollArea.setWidgetResizable(True)
        self.PCAPFieldNamesScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)


        self.PCAPFieldNamesGridLayout.addWidget(self.PCAPFieldNamesScrollArea)

        self.PCAPFieldNamesWidget = QtWidgets.QWidget()
        self.PCAPFieldNamesWidgetGridLayout = QtWidgets.QGridLayout()
        self.PCAPFieldNamesWidget.setLayout(self.PCAPFieldNamesWidgetGridLayout)

        self.PCAPFieldNamesScrollArea.setWidget(self.PCAPFieldNamesWidget)


        self.gridLayout_6.addWidget(self.PCAPFieldNamesGroupBox, 0, 0, 1, 1)
        self.packetFromPCAPDropPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.packetFromPCAPDropPushButton.setObjectName("packetFromPCAPDropPushButton")
        self.gridLayout_6.addWidget(self.packetFromPCAPDropPushButton, 1, 4, 1, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_13.setObjectName("groupBox_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_13)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.packetFromPCAPDisplayFormatComboBox = QtWidgets.QComboBox(self.groupBox_13)
        self.packetFromPCAPDisplayFormatComboBox.setObjectName("packetFromPCAPDisplayFormatComboBox")
        self.verticalLayout_9.addWidget(self.packetFromPCAPDisplayFormatComboBox)
        self.gridLayout_6.addWidget(self.groupBox_13, 0, 3, 1, 2)
        self.gridLayout_12.addWidget(self.groupBox_3, 4, 0, 1, 4)
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.packetFromPCAPAddPushButton = QtWidgets.QPushButton(self.widget)
        self.packetFromPCAPAddPushButton.setObjectName("packetFromPCAPAddPushButton")
        self.verticalLayout_3.addWidget(self.packetFromPCAPAddPushButton)
        self.packetFromPCAPRemovePushButton = QtWidgets.QPushButton(self.widget)
        self.packetFromPCAPRemovePushButton.setObjectName("packetFromPCAPRemovePushButton")
        self.verticalLayout_3.addWidget(self.packetFromPCAPRemovePushButton)
        self.gridLayout_12.addWidget(self.widget, 4, 4, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_10.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_10.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_10.addWidget(self.label_17, 1, 0, 1, 1)
        self.packetFromPCAPMinimumLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.packetFromPCAPMinimumLineEdit.setObjectName("packetFromPCAPMinimumLineEdit")
        self.gridLayout_10.addWidget(self.packetFromPCAPMinimumLineEdit, 3, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_10.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_10.addWidget(self.label_19, 3, 0, 1, 1)
        self.packetFromPCAPMaximumLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.packetFromPCAPMaximumLineEdit.setObjectName("packetFromPCAPMaximumLineEdit")
        self.gridLayout_10.addWidget(self.packetFromPCAPMaximumLineEdit, 4, 1, 1, 2)
        self.packetFromPCAPStopFuzzingPushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.packetFromPCAPStopFuzzingPushButton.setObjectName("packetFromPCAPStopFuzzingPushButton")
        self.gridLayout_10.addWidget(self.packetFromPCAPStopFuzzingPushButton, 5, 2, 1, 1)
        self.packetFromPCAPFuzzPushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.packetFromPCAPFuzzPushButton.setObjectName("packetFromPCAPFuzzPushButton")
        self.gridLayout_10.addWidget(self.packetFromPCAPFuzzPushButton, 5, 1, 1, 1)
        self.packetFromPCAPExpectedReturnTypeLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.packetFromPCAPExpectedReturnTypeLineEdit.setObjectName("packetFromPCAPExpectedReturnTypeLineEdit")
        self.gridLayout_10.addWidget(self.packetFromPCAPExpectedReturnTypeLineEdit, 2, 1, 1, 2)
        self.packetFromPCAPSelectedFieldNameLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.packetFromPCAPSelectedFieldNameLineEdit.setObjectName("packetFromPCAPSelectedFieldNameLineEdit")
        self.gridLayout_10.addWidget(self.packetFromPCAPSelectedFieldNameLineEdit, 1, 1, 1, 2)
        self.packetFromPCAPSelectedPacketNameLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.packetFromPCAPSelectedPacketNameLineEdit.setObjectName("packetFromPCAPSelectedPacketNameLineEdit")
        self.gridLayout_10.addWidget(self.packetFromPCAPSelectedPacketNameLineEdit, 0, 1, 1, 2)
        self.gridLayout_12.addWidget(self.groupBox_4, 4, 5, 1, 1)
        self.contentViewTabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.contentViewTabWidget, 3, 1, 1, 1)
        self.groupBox_22 = QtWidgets.QGroupBox(Form)
        self.groupBox_22.setTitle("")
        self.groupBox_22.setObjectName("groupBox_22")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox_22)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.hookPushButton = QtWidgets.QPushButton(self.groupBox_22)
        self.hookPushButton.setObjectName("hookPushButton")
        self.verticalLayout_15.addWidget(self.hookPushButton)
        self.hookCollectionPushButton = QtWidgets.QPushButton(self.groupBox_22)
        self.hookCollectionPushButton.setObjectName("hookCollectionPushButton")
        self.verticalLayout_15.addWidget(self.hookCollectionPushButton)
        self.livePacketPushButton = QtWidgets.QPushButton(self.groupBox_22)
        self.livePacketPushButton.setObjectName("livePacketPushButton")
        self.verticalLayout_15.addWidget(self.livePacketPushButton)
        self.packetFromPCAPPushButton = QtWidgets.QPushButton(self.groupBox_22)
        self.packetFromPCAPPushButton.setObjectName("packetFromPCAPPushButton")
        self.verticalLayout_15.addWidget(self.packetFromPCAPPushButton)
        self.gridLayout.addWidget(self.groupBox_22, 3, 0, 1, 1)



    #Option View Buttons - used to switch between tabs
        self.hookPushButton.clicked.connect(self.hookPushButtonClicked)
        self.hookCollectionPushButton.clicked.connect(self.hookCollectionPushButtonClicked)
        self.livePacketPushButton.clicked.connect(self.livePacketPushButtonClicked)
        self.packetFromPCAPPushButton.clicked.connect(self.packetFromPCAPPushButtonClicked)


    # Holds the Content View Tab widget that can be used to switch between hook, hook collection, live packet, and packet from PCAP views
        self.contentViewTabWidget.currentChanged.connect(self.contentViewTabWidgetChanged)

    # Every widget in the Hook View
        self.hookDeletePushButton.clicked.connect(self.hookDeletePushButtonClicked)
        self.hookEditPushButton.clicked.connect(self.hookEditPushButtonClicked)
        self.hookAddPushButton.clicked.connect(self.hookAddPushButtonClicked)

        self.hookSearchLineEdit.textEdited.connect(self.hookSearchLineEdited)

        # self.hookPropertiesTableView currently does not have events set up



    # Every Widget in the Hook Collection view
        self.hookCollectionAddPushButton.clicked.connect(self.hookCollectionAddPushButtonClicked)
        self.hookCollectionEditPushButton.clicked.connect(self.hookCollectionEditPushButtonClicked)
        self.hookCollectionDeletePushButton.clicked.connect(self.hookCollectionDeletePushButtonClicked)

        self.hookCollectionSearchLineEdit.textEdited.connect(self.hookCollectionSearchLineEdited)

        # self.hookCollectionPropertiesTableView currently does not have events set up



    # Every Widget in the Live Packet View
        self.livePacketClearFilterPushButton.clicked.connect(self.livePacketClearFilterPushButtonClicked)
        self.livePacketApplyFilterPushButton.clicked.connect(self.livePacketApplyFilterPushButtonClicked)
        self.livePacketClearAreaPushButton.clicked.connect(self.livePacketClearAreaPushButtonClicked)
        self.livePacketForwardPushButton.clicked.connect(self.livePacketForwardPushButtonClicked)
        self.livePacketSaveModificationPushButton.clicked.connect(self.livePacketSaveModificationPushButtonClicked)
        self.livePacketAddFieldPushButton.clicked.connect(self.livePacketAddFieldPushButtonClicked)
        self.livePacketRemoveFieldPushButton.clicked.connect(self.livePacketRemoveFieldPushButtonClicked)
        self.livePacketDropPacketPushButton.clicked.connect(self.livePacketDropPacketPushButtonClicked)
        self.livePacketStopFuzzingPushButton.clicked.connect(self.livePacketStopFuzzingPushButtonClicked)
        self.livePacketFuzzPushButton.clicked.connect(self.livePacketFuzzPushButtonClicked)

        self.livePacketMinimumLineEdit.textEdited.connect(self.livePacketMinimumLineEdited)
        self.livePacketMaximumLineEdit.textEdited.connect(self.livePacketMaximumLineEdited)
        self.livePacketExpectedReturnTypeLineEdit.textEdited.connect(self.livePacketExpectedReturnTypeLineEdited)
        self.livePacketSelectedFieldNameLineEdit.textEdited.connect(self.livePacketSelectedFieldNameLineEdited)
        self.livePacketSelectedPacketNameLineEdit.textEdited.connect(self.livePacketSelectedPacketNameLineEdited)

        self.livePacketQueueSizeLineEdit.textEdited.connect(self.livePacketQueueSizeLineEdited)
        self.livePacketCaptureFilterLineEdit.textEdited.connect(self.livePacketCaptureFilterLineEdited)

        self.livePacketProxyBehaviorComboBox.currentIndexChanged.connect(self.livePacketProxyBehaviorComboBoxIndexChanged)
        self.livePacketInterceptionBehaviorComboBox.currentIndexChanged.connect(self.livePacketInterceptionBehaviorComboBoxIndexChanged)
        self.livePacketDisplayFormatComboBox.currentIndexChanged.connect(self.livePacketDisplayFormatComboBoxIndexChanged)

        self.livePacketTabWidget.currentChanged.connect(self.livePacketTabWidgetChanged)

        # self.livePacketDissectedListView

        # self.livePacketBinaryListView
        # self.livePacketHEXListView



    # Every Widget in the Packet from PCAP View
        self.packetFromPCAPApplyCaptureFilterPushButton.clicked.connect(self.packetFromPCAPApplyCaptureFilterPushButtonClicked)
        self.packetFromPCAPClearCaptureFilterPushButton.clicked.connect(self.packetFromPCAPClearCaptureFilterPushButtonClicked)
        self.packetFromPCAPOpenFilePushButton.clicked.connect(self.packetFromPCAPOpenFilePushButtonClicked)
        self.packetFromPCAPCancelFilePushButton.clicked.connect(self.packetFromPCAPCancelFilePushButtonClicked)
        self.packetFromPCAPClearPacketAreaPushButton.clicked.connect(self.packetFromPCAPClearPacketAreaPushButtonClicked)
        self.packetFromPCAPForwardPushButton.clicked.connect(self.packetFromPCAPForwardPushButtonClicked)
        self.packetFromPCAPSaveModificationPushButton.clicked.connect(self.packetFromPCAPSaveModificationPushButtonClicked)
        self.packetFromPCAPDropPushButton.clicked.connect(self.packetFromPCAPDropPushButtonClicked)
        self.packetFromPCAPAddPushButton.clicked.connect(self.packetFromPCAPAddPushButtonClicked)
        self.packetFromPCAPRemovePushButton.clicked.connect(self.packetFromPCAPRemovePushButtonClicked)
        self.packetFromPCAPStopFuzzingPushButton.clicked.connect(self.packetFromPCAPStopFuzzingPushButtonClicked)
        self.packetFromPCAPFuzzPushButton.clicked.connect(self.packetFromPCAPFuzzPushButtonClicked)

        self.packetFromPCAPFileLineEdit.textEdited.connect(self.packetFromPCAPFileLineEdited)
        self.packetFromPCAPMinimumLineEdit.textEdited.connect(self.packetFromPCAPMinimumLineEdited)
        self.packetFromPCAPMaximumLineEdit.textEdited.connect(self.packetFromPCAPMaximumLineEdited)

        self.packetFromPCAPExpectedReturnTypeLineEdit.textEdited.connect(self.packetFromPCAPExpectedReturnTypeLineEdited)
        self.packetFromPCAPSelectedFieldNameLineEdit.textEdited.connect(self.packetFromPCAPSelectedFieldNameLineEdited)
        self.packetFromPCAPSelectedPacketNameLineEdit.textEdited.connect(self.packetFromPCAPSelectedPacketNameLineEdited)
        self.packetFromPCAPQueueSizeLineEdit.textEdited.connect(self.packetFromPCAPQueueSizeLineEdited)
        self.packetFromPCAPCaptureFilterLineEdit.textEdited.connect(self.packetFromPCAPCaptureFilterLineEdited)

        self.packetFromPCAPProxyBehaviorComboBox.currentIndexChanged.connect(self.packetFromPCAPProxyBehaviorComboBoxIndexChanged)
        self.packetFromPCAPInterceptionBehaviorComboBox.currentIndexChanged.connect(self.packetFromPCAPInterceptionBehaviorComboBoxIndexChanged)
        self.packetFromPCAPDisplayFormatComboBox.currentIndexChanged.connect(self.packetFromPCAPDisplayFormatComboBoxIndexChanged)
        self.packetFromPCAPTabWidget.currentChanged.connect(self.packetFromPCAPTabWidgetChanged)

        self.retranslateUi(Form)
        self.contentViewTabWidget.setCurrentIndex(3)
        self.livePacketTabWidget.setCurrentIndex(0)
        self.packetFromPCAPTabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)


#Option View Buttons - used to switch between tabs

    @pyqtSlot( )
    def hookPushButtonClicked( self ):
        self.contentViewTabWidget.setCurrentIndex(0)


    @pyqtSlot( )
    def hookCollectionPushButtonClicked( self ):
        self.contentViewTabWidget.setCurrentIndex(1)


    @pyqtSlot( )
    def livePacketPushButtonClicked( self ):
        self.contentViewTabWidget.setCurrentIndex(2)


    @pyqtSlot( )
    def packetFromPCAPPushButtonClicked( self ):
        self.contentViewTabWidget.setCurrentIndex(3)


# Holds the Content View Tab widget that can be used to switch between hook, hook collection, live packet, and packet from PCAP views
    @pyqtSlot(int)
    def contentViewTabWidgetChanged( self, index ):
        self.label_3.setText(str(index))


# Hook View Event Listener Functions

    @pyqtSlot( )
    def hookDeletePushButtonClicked( self ):
        self.label_3.setText("hookDeletePushButtonClicked")


    @pyqtSlot( )
    def hookEditPushButtonClicked( self ):
        self.label_3.setText("hookEditPushButtonClicked")


    @pyqtSlot( )
    def hookAddPushButtonClicked( self ):
        addHookWindow = QtWidgets.QDialog()
        addHookWindow.setWindowTitle("Add Hook")
        addHookWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        ui = Hook_Ui_Form()
        ui.setupUi(addHookWindow)
        addHookWindow.exec_()
        if ui.hookData:
            self.hookManager.add_hook(ui.hookData[0], ui.hookData[1], ui.hookData[2])
            self.hookPropertiesTableView.setModel(self.hookManager.createHookModel())


    @pyqtSlot(str)
    def hookSearchLineEdited( self, text ):
        self.label_3.setText(text)


# Hook Collection View Event Listener Functions

    @pyqtSlot( )
    def hookCollectionAddPushButtonClicked( self ):
        addHookCollectionWindow = QtWidgets.QDialog()
        addHookCollectionWindow.setWindowTitle("Add Hook Collection")
        addHookCollectionWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        ui = Hook_Collection_Ui_Form()
        ui.setupUi(addHookCollectionWindow, self.hookManager.hooks)
        addHookCollectionWindow.exec_()
        if ui.hookCollectionData:
            self.hookCollectionManager.add_collection(ui.hookCollectionData[0], ui.hookCollectionData[1], ui.hookCollectionData[2], ui.hookCollectionData[3], ui.hookCollectionData[4])
            self.hookCollectionPropertiesTableView.setModel(self.hookCollectionManager.createHookCollectionModel())


    @pyqtSlot( )
    def hookCollectionEditPushButtonClicked( self ):
        self.label_3.setText("hookCollectionEditPushButtonClicked")


    @pyqtSlot( )
    def hookCollectionDeletePushButtonClicked( self ):
        self.label_3.setText("hookCollectionDeletePushButtonClicked")


    @pyqtSlot(str)
    def hookCollectionSearchLineEdited( self, text ):
        self.label_3.setText(text)


# Live Packet View Event Listener Functions

    @pyqtSlot( )
    def livePacketClearFilterPushButtonClicked( self ):
        self.label_3.setText("livePacketClearFilterPushButtonClicked")


    @pyqtSlot( )
    def livePacketApplyFilterPushButtonClicked( self ):
        self.label_3.setText("livePacketApplyFilterPushButtonClicked")


    @pyqtSlot( )
    def livePacketClearAreaPushButtonClicked( self ):
        self.label_3.setText("livePacketClearAreaPushButtonClicked")


    @pyqtSlot( )
    def livePacketForwardPushButtonClicked( self ):
        self.label_3.setText("livePacketForwardPushButtonClicked")


    @pyqtSlot( )
    def livePacketSaveModificationPushButtonClicked( self ):
        self.label_3.setText("livePacketSaveModificationPushButtonClicked")


    @pyqtSlot( )
    def livePacketAddFieldPushButtonClicked( self ):
        self.label_3.setText("livePacketAddFieldPushButtonClicked")


    @pyqtSlot( )
    def livePacketRemoveFieldPushButtonClicked( self ):
        self.label_3.setText("livePacketRemoveFieldPushButtonClicked")


    @pyqtSlot( )
    def livePacketDropPacketPushButtonClicked( self ):
        self.label_3.setText("livePacketDropPacketPushButtonClicked")


    @pyqtSlot( )
    def livePacketStopFuzzingPushButtonClicked( self ):
        self.label_3.setText("livePacketStopFuzzingPushButtonClicked")


    @pyqtSlot( )
    def livePacketFuzzPushButtonClicked( self ):
        self.label_3.setText("livePacketFuzzPushButtonClicked")


    @pyqtSlot(str)
    def livePacketMinimumLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def livePacketMaximumLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def livePacketExpectedReturnTypeLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def livePacketSelectedFieldNameLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def livePacketSelectedPacketNameLineEdited( self, text ):
        self.label_3.setText(text)


    @pyqtSlot(str)
    def livePacketQueueSizeLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def livePacketCaptureFilterLineEdited( self, text ):
        self.label_3.setText(text)


      from threading import Thread
    from src.integration_test import testq
    @pyqtSlot(int)
    def livePacketProxyBehaviorComboBoxIndexChanged(self, index):
        if index == 0:
            # TODO Turn off proxy
            self.livePacketInterceptionBehaviorComboBox.setCurrentIndex(0)
            self.livePacketInterceptionBehaviorComboBox.setEnabled(False)

        if index == 1:
            # TODO turn on proxy behavior

            self.livePacketInterceptionBehaviorComboBox.setEnabled(True)
        # self.label_3.setText(str(index))


    @pyqtSlot(int)
    def livePacketInterceptionBehaviorComboBoxIndexChanged(self, index):
        from src.intercept import interceptor
        # index 0 is off, 1 is on
        if index == 1:
            proxy = Thread(target=interceptor.interception)
            proxy.start()

            # TODO Start the hookrunner


            if self.livePacketManager is None:
                self.livePacketManager = LiveTrafficPacketFileManager()
                self.livePacketDissectedListView.setModel(self.livePacketManager.dissectedModel)
            else:
                # start threads
                self.livePacketManager.get_pkts()
        #     TODO turn on interception behavior
        if index == 0:
            # TODO turn off interception behavior
            #testq.turn_off()
            interceptor.turn_off()
        self.label_3.setText(str(index))

    @pyqtSlot(int)
    def livePacketDisplayFormatComboBoxIndexChanged( self, index ):
        self.label_3.setText(str(index))

    @pyqtSlot(int)
    def livePacketFieldCheckBoxStateChanged( self, state ):
        self.label_3.setText(str(state))

    @pyqtSlot()
    def livePacketBinaryListViewItemClicked( self ):
        self.label_3.setText("livePacketBinaryListViewItemClicked")

    @pyqtSlot()
    def livePacketDissectedListViewItemClicked( self ):
        self.label_3.setText("livePacketDissectedListViewItemClicked")

    @pyqtSlot()
    def livePacketHEXListViewItemClicked( self ):
        self.label_3.setText("livePacketHEXListViewItemClicked")


    @pyqtSlot(int)
    def livePacketTabWidgetChanged( self, index ):
        self.label_3.setText(str(index))

# Packet from PCAP View Event Listener Functions


    @pyqtSlot( )
    def packetFromPCAPApplyCaptureFilterPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPApplyCaptureFilterPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPClearCaptureFilterPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPClearCaptureFilterPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPOpenFilePushButtonClicked( self ):
    	fname = self.packetFromPCAPFileLineEdit.text()
    	self.PCAPFileManager = PCAPFileManager(fname)

    	self.packetFromPCAPDissectedTreeView.setModel(self.PCAPFileManager.dissectedModel)
    	self.packetFromPCAPDissectedTreeView.clicked.connect(self.layerSelected)

    	self.packetFromPCAPBinaryListView.setModel(self.PCAPFileManager.binaryModel)
    	
    	self.packetFromPCAPHEXListView.setModel(self.PCAPFileManager.HEXModel)

    	self.label_3.setText("packetFromPCAPOpenFilePushButtonClicked")

    @pyqtSlot(QtCore.QModelIndex)
    def layerSelected(self, modelIndex):
    	#clear current field name widgets
        for i in reversed(range(self.PCAPFieldNamesWidgetGridLayout.count())): 
            self.PCAPFieldNamesWidgetGridLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.PCAPValueWidgetVerticalLayout.count())): 
            self.PCAPValueWidgetVerticalLayout.itemAt(i).widget().setParent(None)

        self.PCAPFieldToValueLineEditDict = {}
        self.PCAPFieldToFieldLineEditDict = {}
        layerName = str(modelIndex.data())
        if 'Frame ' in layerName:
            return
        packetIndex = modelIndex.parent().row()
        fieldDict = self.PCAPFileManager.getFieldDict(packetIndex, layerName)
        i = 0
        for field, value in fieldDict.items():
            self.packetFromPCAPFieldCheckBox = QtWidgets.QCheckBox(self.PCAPFieldNamesWidget)
            self.PCAPFieldNamesWidgetGridLayout.addWidget(self.packetFromPCAPFieldCheckBox, i, 0, 1, 1)
            self.packetFromPCAPFieldLineEdit = QtWidgets.QLineEdit(self.PCAPFieldNamesWidget)
            self.packetFromPCAPFieldLineEdit.setText(field)
            self.PCAPFieldNamesWidgetGridLayout.addWidget(self.packetFromPCAPFieldLineEdit, i, 1, 1, 1)

            self.packetFromPCAPValueLineEdit = QtWidgets.QLineEdit(self.PCAPValueWidget)
            self.packetFromPCAPValueLineEdit.setText(str(value))
            self.PCAPValueWidgetVerticalLayout.addWidget(self.packetFromPCAPValueLineEdit)
            self.PCAPFieldToValueLineEditDict[field] = self.packetFromPCAPValueLineEdit
            self.PCAPFieldToFieldLineEditDict[field] = self.packetFromPCAPFieldLineEdit
            i+=1



    @pyqtSlot( )
    def packetFromPCAPCancelFilePushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPCancelFilePushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPClearPacketAreaPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPClearPacketAreaPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPForwardPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPForwardPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPSaveModificationPushButtonClicked( self ):
        modelIndex = self.packetFromPCAPDissectedTreeView.currentIndex()
        layerName = str(modelIndex.data())
        if 'Frame ' in layerName:
            return
        packetIndex = modelIndex.parent().row()
        fieldDict = self.PCAPFileManager.getFieldDict(packetIndex, layerName)
        modifications = {}
        for field, value in fieldDict.items():
            newValue = self.PCAPFieldToValueLineEditDict[field].text()
            if newValue is str(value):
                modifications[field] = value
            else:
                modifications[field] = newValue
        self.PCAPFileManager.modifyPacket(packetIndex, layerName, modifications)
        self.label_3.setText("packetFromPCAPSaveModificationPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPDropPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPDropPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPAddPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPAddPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPRemovePushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPRemovePushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPStopFuzzingPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPStopFuzzingPushButtonClicked")


    @pyqtSlot( )
    def packetFromPCAPFuzzPushButtonClicked( self ):
        self.label_3.setText("packetFromPCAPFuzzPushButtonClicked")


    @pyqtSlot(str)
    def packetFromPCAPMinimumLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def packetFromPCAPMaximumLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def packetFromPCAPExpectedReturnTypeLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def packetFromPCAPSelectedFieldNameLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def packetFromPCAPSelectedPacketNameLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def packetFromPCAPQueueSizeLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def packetFromPCAPFileLineEdited( self, text ):
        self.label_3.setText(text)

    @pyqtSlot(str)
    def packetFromPCAPCaptureFilterLineEdited( self, text ):
        self.label_3.setText(text)


    @pyqtSlot(int)
    def packetFromPCAPProxyBehaviorComboBoxIndexChanged( self, index ):
        self.label_3.setText(str(index))

    @pyqtSlot(int)
    def packetFromPCAPInterceptionBehaviorComboBoxIndexChanged( self, index ):
        self.label_3.setText(str(index))

    @pyqtSlot(int)
    def packetFromPCAPDisplayFormatComboBoxIndexChanged( self, index ):
        self.label_3.setText(str(index))



    @pyqtSlot(int)
    def packetFromPCAPFieldCheckBoxStateChanged( self, state ):
        self.label_3.setText(str(state))

    @pyqtSlot()
    def packetFromPCAPDissectedListViewItemClicked( self ):
        self.label_3.setText("packetFromPCAPDissectedListViewItemClicked")

    @pyqtSlot()
    def packetFromPCAPBinaryListViewItemClicked( self ):
        self.label_3.setText("packetFromPCAPBinaryListViewItemClicked")

    @pyqtSlot()
    def packetFromPCAPHEXListViewItemClicked( self ):
        self.label_3.setText("packetFromPCAPHEXListViewItemClicked")


    @pyqtSlot(int)
    def packetFromPCAPTabWidgetChanged( self, index ):
        self.label_3.setText(str(index))



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Content View"))
        self.label.setText(_translate("Form", "Option View"))
        self.label_3.setText(_translate("Form", "Network Traffic Proxy System"))
        self.groupBox_23.setTitle(_translate("Form", "Hook Properties"))
        self.hookDeletePushButton.setText(_translate("Form", "Delete"))
        self.label_33.setText(_translate("Form", "Search"))
        self.hookEditPushButton.setText(_translate("Form", "Edit"))
        self.hookAddPushButton.setText(_translate("Form", "+Hook"))
        self.contentViewTabWidget.setTabText(self.contentViewTabWidget.indexOf(self.tab), _translate("Form", "Hook"))
        self.groupBox_24.setTitle(_translate("Form", "Hook Collection Properties"))
        self.label_34.setText(_translate("Form", "Search"))
        self.livePacketFieldNamesGroupBox.setTitle(_translate("Form", "Field Name"))
        self.liveTrafficValueGroupBox.setTitle(_translate("Form", "Value"))
        self.hookCollectionEditPushButton.setText(_translate("Form", "Edit"))
        self.hookCollectionDeletePushButton.setText(_translate("Form", "Delete"))
        self.hookCollectionAddPushButton.setText(_translate("Form", "+Hook Collection"))
        self.contentViewTabWidget.setTabText(self.contentViewTabWidget.indexOf(self.tab_2), _translate("Form", "Hook Collection"))
        self.label_24.setText(_translate("Form", "Proxy Behavior"))
        self.label_26.setText(_translate("Form", "Interception Behavior"))
        self.label_23.setText(_translate("Form", "Queue Size"))
        self.groupBox_14.setTitle(_translate("Form", "Capture Filter"))
        self.label_25.setText(_translate("Form", "FIlter"))
        self.livePacketClearFilterPushButton.setText(_translate("Form", "Clear"))
        self.livePacketApplyFilterPushButton.setText(_translate("Form", "Apply"))
        self.groupBox_15.setTitle(_translate("Form", "Packet Area"))
        self.livePacketTabWidget.setTabText(self.livePacketTabWidget.indexOf(self.tab_11), _translate("Form", "Dissected"))
        self.livePacketTabWidget.setTabText(self.livePacketTabWidget.indexOf(self.tab_12), _translate("Form", "Binary"))
        self.livePacketTabWidget.setTabText(self.livePacketTabWidget.indexOf(self.tab_13), _translate("Form", "HEX"))
        self.livePacketClearAreaPushButton.setText(_translate("Form", "Clear"))
        self.groupBox_17.setTitle(_translate("Form", "Field Area"))
        self.livePacketForwardPushButton.setText(_translate("Form", "Forward"))
        self.label_32.setText(_translate("Form", "Field Name, value, and display format are editable fields"))
        self.livePacketSaveModificationPushButton.setText(_translate("Form", "Save Modification"))
        self.groupBox_18.setTitle(_translate("Form", "Mask"))
        self.maskLabel_3.setText(_translate("Form", "0"))
        self.livePacketDropPacketPushButton.setText(_translate("Form", "Drop"))
        self.groupBox_21.setTitle(_translate("Form", "Display Format"))
        self.livePacketAddFieldPushButton.setText(_translate("Form", "+"))
        self.livePacketRemoveFieldPushButton.setText(_translate("Form", "-"))
        self.groupBox_16.setTitle(_translate("Form", "Fuzzing Area"))
        self.label_27.setText(_translate("Form", "Expected Return Type"))
        self.label_28.setText(_translate("Form", "Selected Packet Name"))
        self.label_29.setText(_translate("Form", "Selected Field Name"))
        self.label_30.setText(_translate("Form", "Maximum"))
        self.label_31.setText(_translate("Form", "Minimum"))
        self.livePacketStopFuzzingPushButton.setText(_translate("Form", "Stop"))
        self.livePacketFuzzPushButton.setText(_translate("Form", "Fuzz"))

        self.contentViewTabWidget.setTabText(self.contentViewTabWidget.indexOf(self.tab_3), _translate("Form", "Live Packet"))
        self.label_6.setText(_translate("Form", "Proxy Behavior"))
        self.label_4.setText(_translate("Form", "Interception Behavior"))
        self.label_5.setText(_translate("Form", "Queue Size"))
        self.groupBox_9.setTitle(_translate("Form", "PCAP File"))
        self.label_14.setText(_translate("Form", "PCAP File"))
        self.packetFromPCAPOpenFilePushButton.setText(_translate("Form", "Open"))
        self.packetFromPCAPCancelFilePushButton.setText(_translate("Form", "Cancel"))
        self.groupBox.setTitle(_translate("Form", "Capture Filter"))
        self.label_22.setText(_translate("Form", "FIlter"))
        self.packetFromPCAPApplyCaptureFilterPushButton.setText(_translate("Form", "Apply"))
        self.packetFromPCAPClearCaptureFilterPushButton.setText(_translate("Form", "Clear"))
        self.groupBox_2.setTitle(_translate("Form", "Packet Area"))

        self.packetFromPCAPTabWidget.setTabText(self.packetFromPCAPTabWidget.indexOf(self.tab_14), _translate("Form", "Dissected"))
        self.packetFromPCAPTabWidget.setTabText(self.packetFromPCAPTabWidget.indexOf(self.tab_15), _translate("Form", "Binary"))
        self.packetFromPCAPTabWidget.setTabText(self.packetFromPCAPTabWidget.indexOf(self.tab_16), _translate("Form", "HEX"))

        self.packetFromPCAPClearPacketAreaPushButton.setText(_translate("Form", "Clear"))
        self.groupBox_3.setTitle(_translate("Form", "Field Area"))
        self.packetFromPCAPForwardPushButton.setText(_translate("Form", "Forward"))
        self.label_21.setText(_translate("Form", "Field Name, value, and display format are editable fields"))
        self.packetFromPCAPSaveModificationPushButton.setText(_translate("Form", "Save Modification"))
        self.groupBox_10.setTitle(_translate("Form", "Mask"))
        self.maskLabel_2.setText(_translate("Form", "0"))
        self.PCAPValueGroupBox.setTitle(_translate("Form", "Value"))
        self.PCAPFieldNamesGroupBox.setTitle(_translate("Form", "FieldName"))
        self.packetFromPCAPDropPushButton.setText(_translate("Form", "Drop"))
        self.groupBox_13.setTitle(_translate("Form", "Display Format"))
        self.packetFromPCAPAddPushButton.setText(_translate("Form", "+"))
        self.packetFromPCAPRemovePushButton.setText(_translate("Form", "-"))
        self.groupBox_4.setTitle(_translate("Form", "Fuzzing Area"))
        self.label_15.setText(_translate("Form", "Expected Return Type"))
        self.label_16.setText(_translate("Form", "Selected Packet Name"))
        self.label_17.setText(_translate("Form", "Selected Field Name"))
        self.label_18.setText(_translate("Form", "Maximum"))
        self.label_19.setText(_translate("Form", "Minimum"))
        self.packetFromPCAPStopFuzzingPushButton.setText(_translate("Form", "Stop"))
        self.packetFromPCAPFuzzPushButton.setText(_translate("Form", "Fuzz"))
        self.contentViewTabWidget.setTabText(self.contentViewTabWidget.indexOf(self.tab_4), _translate("Form", "Packet From PCAP"))

        self.hookPushButton.setText(_translate("Form", "Hook"))
        self.hookCollectionPushButton.setText(_translate("Form", "Hook Collection"))
        self.livePacketPushButton.setText(_translate("Form", "Live Packet"))
        self.packetFromPCAPPushButton.setText(_translate("Form", "Packet from PCAP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
