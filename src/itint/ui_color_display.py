# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_color_display.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import assets_rc

class Ui_ColorDisplay(object):
    def setupUi(self, ColorDisplay):
        if not ColorDisplay.objectName():
            ColorDisplay.setObjectName(u"ColorDisplay")
        ColorDisplay.resize(184, 288)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorDisplay.sizePolicy().hasHeightForWidth())
        ColorDisplay.setSizePolicy(sizePolicy)
        ColorDisplay.setMinimumSize(QSize(184, 288))
        ColorDisplay.setMaximumSize(QSize(184, 288))
        self.gridLayout_3 = QGridLayout(ColorDisplay)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.frameColor = QFrame(ColorDisplay)
        self.frameColor.setObjectName(u"frameColor")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameColor.sizePolicy().hasHeightForWidth())
        self.frameColor.setSizePolicy(sizePolicy1)
        self.frameColor.setMinimumSize(QSize(130, 130))
        self.frameColor.setMaximumSize(QSize(130, 130))
        self.frameColor.setAutoFillBackground(True)
        self.frameColor.setFrameShape(QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameColor)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelColor = QLabel(self.frameColor)
        self.labelColor.setObjectName(u"labelColor")
        sizePolicy.setHeightForWidth(self.labelColor.sizePolicy().hasHeightForWidth())
        self.labelColor.setSizePolicy(sizePolicy)
        self.labelColor.setMinimumSize(QSize(100, 100))
        self.labelColor.setMaximumSize(QSize(100, 100))
        self.labelColor.setAlignment(Qt.AlignCenter)
        self.labelColor.setMargin(0)

        self.horizontalLayout.addWidget(self.labelColor)


        self.gridLayout_3.addWidget(self.frameColor, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.frame_2 = QFrame(ColorDisplay)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textRGB1 = QLineEdit(self.frame_3)
        self.textRGB1.setObjectName(u"textRGB1")
        self.textRGB1.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textRGB1.sizePolicy().hasHeightForWidth())
        self.textRGB1.setSizePolicy(sizePolicy4)
        self.textRGB1.setReadOnly(True)

        self.gridLayout.addWidget(self.textRGB1, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.textRGB3 = QLineEdit(self.frame_3)
        self.textRGB3.setObjectName(u"textRGB3")
        self.textRGB3.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textRGB3.sizePolicy().hasHeightForWidth())
        self.textRGB3.setSizePolicy(sizePolicy4)
        self.textRGB3.setReadOnly(True)

        self.gridLayout.addWidget(self.textRGB3, 2, 1, 1, 1)

        self.textRGB2 = QLineEdit(self.frame_3)
        self.textRGB2.setObjectName(u"textRGB2")
        self.textRGB2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textRGB2.sizePolicy().hasHeightForWidth())
        self.textRGB2.setSizePolicy(sizePolicy4)
        self.textRGB2.setReadOnly(True)

        self.gridLayout.addWidget(self.textRGB2, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textHSB2 = QLineEdit(self.frame_4)
        self.textHSB2.setObjectName(u"textHSB2")
        self.textHSB2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textHSB2.sizePolicy().hasHeightForWidth())
        self.textHSB2.setSizePolicy(sizePolicy4)
        self.textHSB2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textHSB2, 1, 1, 1, 1)

        self.textHSB1 = QLineEdit(self.frame_4)
        self.textHSB1.setObjectName(u"textHSB1")
        self.textHSB1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textHSB1.sizePolicy().hasHeightForWidth())
        self.textHSB1.setSizePolicy(sizePolicy4)
        self.textHSB1.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textHSB1, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.textHSB3 = QLineEdit(self.frame_4)
        self.textHSB3.setObjectName(u"textHSB3")
        self.textHSB3.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textHSB3.sizePolicy().hasHeightForWidth())
        self.textHSB3.setSizePolicy(sizePolicy4)
        self.textHSB3.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textHSB3, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 3)

        self.frame = QFrame(ColorDisplay)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnCopyRGB = QPushButton(self.frame)
        self.btnCopyRGB.setObjectName(u"btnCopyRGB")
        self.btnCopyRGB.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u":/icon/assets/content_copy_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCopyRGB.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btnCopyRGB)

        self.btnEdit = QPushButton(self.frame)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icon/assets/edit_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEdit.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btnEdit)

        self.btnPick = QPushButton(self.frame)
        self.btnPick.setObjectName(u"btnPick")
        self.btnPick.setMaximumSize(QSize(30, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icon/assets/colorize_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPick.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btnPick)

        self.btnCopyHSB = QPushButton(self.frame)
        self.btnCopyHSB.setObjectName(u"btnCopyHSB")
        self.btnCopyHSB.setMaximumSize(QSize(30, 16777215))
        self.btnCopyHSB.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btnCopyHSB)

        self.btnRemove = QPushButton(self.frame)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icon/assets/close_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRemove.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.btnRemove)


        self.gridLayout_3.addWidget(self.frame, 3, 0, 1, 3)


        self.retranslateUi(ColorDisplay)

        QMetaObject.connectSlotsByName(ColorDisplay)
    # setupUi

    def retranslateUi(self, ColorDisplay):
        ColorDisplay.setWindowTitle(QCoreApplication.translate("ColorDisplay", u"Form", None))
        self.labelColor.setText(QCoreApplication.translate("ColorDisplay", u"\u8272\u6761\u663e\u793a", None))
        self.label_4.setText(QCoreApplication.translate("ColorDisplay", u"B", None))
        self.label_2.setText(QCoreApplication.translate("ColorDisplay", u"R", None))
        self.label_3.setText(QCoreApplication.translate("ColorDisplay", u"G", None))
        self.label_6.setText(QCoreApplication.translate("ColorDisplay", u"S", None))
        self.label_5.setText(QCoreApplication.translate("ColorDisplay", u"H", None))
        self.label_7.setText(QCoreApplication.translate("ColorDisplay", u"B", None))
        self.btnCopyRGB.setText("")
        self.btnEdit.setText("")
        self.btnPick.setText("")
        self.btnCopyHSB.setText("")
        self.btnRemove.setText("")
    # retranslateUi

