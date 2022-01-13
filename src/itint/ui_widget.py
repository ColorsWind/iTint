# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(900, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMaximumSize(QSize(16777215, 16777215))
        MainWidget.setSizeIncrement(QSize(8, 6))
        MainWidget.setBaseSize(QSize(900, 653))
        self.horizontalLayout_3 = QHBoxLayout(MainWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 5, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(MainWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(170, 0))
        self.groupBox.setMaximumSize(QSize(170, 280))
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnFromScan = QPushButton(self.groupBox)
        self.btnFromScan.setObjectName(u"btnFromScan")

        self.verticalLayout_3.addWidget(self.btnFromScan)

        self.btnFromClipboard = QPushButton(self.groupBox)
        self.btnFromClipboard.setObjectName(u"btnFromClipboard")

        self.verticalLayout_3.addWidget(self.btnFromClipboard)

        self.btnColorPickup = QPushButton(self.groupBox)
        self.btnColorPickup.setObjectName(u"btnColorPickup")

        self.verticalLayout_3.addWidget(self.btnColorPickup)

        self.cBtnAutoHide = QCheckBox(self.groupBox)
        self.cBtnAutoHide.setObjectName(u"cBtnAutoHide")
        self.cBtnAutoHide.setChecked(True)

        self.verticalLayout_3.addWidget(self.cBtnAutoHide)

        self.cBtnAutoClear = QCheckBox(self.groupBox)
        self.cBtnAutoClear.setObjectName(u"cBtnAutoClear")
        self.cBtnAutoClear.setChecked(True)

        self.verticalLayout_3.addWidget(self.cBtnAutoClear)


        self.horizontalLayout.addWidget(self.groupBox)

        self.imagePreview = QGroupBox(MainWidget)
        self.imagePreview.setObjectName(u"imagePreview")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy2)
        self.imagePreview.setMinimumSize(QSize(700, 280))
        self.horizontalLayout_2 = QHBoxLayout(self.imagePreview)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelImagePreview = QLabel(self.imagePreview)
        self.labelImagePreview.setObjectName(u"labelImagePreview")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelImagePreview.sizePolicy().hasHeightForWidth())
        self.labelImagePreview.setSizePolicy(sizePolicy3)
        self.labelImagePreview.setMinimumSize(QSize(600, 260))
        self.labelImagePreview.setTextFormat(Qt.AutoText)
        self.labelImagePreview.setScaledContents(False)
        self.labelImagePreview.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelImagePreview)


        self.horizontalLayout.addWidget(self.imagePreview)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frameColorDisplay = QGroupBox(MainWidget)
        self.frameColorDisplay.setObjectName(u"frameColorDisplay")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frameColorDisplay.sizePolicy().hasHeightForWidth())
        self.frameColorDisplay.setSizePolicy(sizePolicy4)
        self.frameColorDisplay.setMinimumSize(QSize(875, 360))
        self.frameColorDisplay.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.frameColorDisplay)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frameColorDisplay)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy5)
        self.scrollArea.setMinimumSize(QSize(0, 340))
        self.scrollArea.setMaximumSize(QSize(16777215, 340))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.colorDisplayContent = QWidget()
        self.colorDisplayContent.setObjectName(u"colorDisplayContent")
        self.colorDisplayContent.setGeometry(QRect(0, 0, 872, 340))
        self.scrollArea.setWidget(self.colorDisplayContent)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frameColorDisplay)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"iTint 0.0.1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWidget", u"\u52a0\u8f7d\u56fe\u7247", None))
        self.btnFromScan.setText(QCoreApplication.translate("MainWidget", u"\u4ece\u5c4f\u5e55...", None))
        self.btnFromClipboard.setText(QCoreApplication.translate("MainWidget", u"\u4ece\u526a\u5207\u677f...", None))
        self.btnColorPickup.setText(QCoreApplication.translate("MainWidget", u"\u62fe\u8272\u5668", None))
        self.cBtnAutoHide.setText(QCoreApplication.translate("MainWidget", u"\u81ea\u52a8\u9690\u85cf\u7a97\u53e3", None))
        self.cBtnAutoClear.setText(QCoreApplication.translate("MainWidget", u"\u81ea\u52a8\u6e05\u7a7a\u8272\u5361", None))
        self.imagePreview.setTitle(QCoreApplication.translate("MainWidget", u"\u9884\u89c8", None))
        self.labelImagePreview.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">\u5c06\u6587\u4ef6\u62d6\u5165\u751f\u6210\u8272\u5361</span></p><p align=\"center\"><span style=\" font-weight:600;\">\u6216\u70b9\u51fb\u9009\u62e9\u6587\u4ef6</span></p></body></html>", None))
        self.frameColorDisplay.setTitle(QCoreApplication.translate("MainWidget", u"\u8272\u5361", None))
    # retranslateUi

