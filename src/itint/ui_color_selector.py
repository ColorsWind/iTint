# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_color_selector.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ColorSelector(object):
    def setupUi(self, ColorSelector):
        if not ColorSelector.objectName():
            ColorSelector.setObjectName(u"ColorSelector")
        ColorSelector.resize(380, 218)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorSelector.sizePolicy().hasHeightForWidth())
        ColorSelector.setSizePolicy(sizePolicy)
        ColorSelector.setMinimumSize(QSize(0, 0))
        ColorSelector.setMaximumSize(QSize(16777215, 16777215))
        ColorSelector.setSizeIncrement(QSize(35, 20))
        ColorSelector.setBaseSize(QSize(380, 218))
        ColorSelector.setStyleSheet(u"QWidget{\n"
"	background-color: none;\n"
"}\n"
"QFrame{\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*  LINE EDIT */\n"
"QLineEdit{\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: #303030;\n"
"	border: 2px solid #303030;\n"
"	border-radius: 5px;\n"
"	selection-color: rgb(16, 16, 16);\n"
"	selection-background-color: rgb(221, 51, 34);\n"
"	font-family: Segoe UI;\n"
"	font-size: 11pt;\n"
"}\n"
"QLineEdit::focus{\n"
"	border-color: #aaaaaa;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(ColorSelector)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.color_view = QFrame(ColorSelector)
        self.color_view.setObjectName(u"color_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.color_view.sizePolicy().hasHeightForWidth())
        self.color_view.setSizePolicy(sizePolicy1)
        self.color_view.setMinimumSize(QSize(200, 200))
        self.color_view.setMaximumSize(QSize(16777215, 16777215))
        self.color_view.setStyleSheet(u"/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: qlineargradient(x1:1, x2:0, stop:0 hsl(0%,100%,50%), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.color_view.setFrameShape(QFrame.StyledPanel)
        self.color_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.color_view)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.black_overlay = QFrame(self.color_view)
        self.black_overlay.setObjectName(u"black_overlay")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.black_overlay.sizePolicy().hasHeightForWidth())
        self.black_overlay.setSizePolicy(sizePolicy2)
        self.black_overlay.setMinimumSize(QSize(200, 200))
        self.black_overlay.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 4px;\n"
"\n"
"")
        self.black_overlay.setFrameShape(QFrame.StyledPanel)
        self.black_overlay.setFrameShadow(QFrame.Raised)
        self.selector = QFrame(self.black_overlay)
        self.selector.setObjectName(u"selector")
        self.selector.setGeometry(QRect(-6, 194, 12, 12))
        self.selector.setMinimumSize(QSize(12, 12))
        self.selector.setMaximumSize(QSize(12, 12))
        self.selector.setStyleSheet(u"background-color:none;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.selector.setFrameShape(QFrame.StyledPanel)
        self.selector.setFrameShadow(QFrame.Raised)
        self.black_ring = QLabel(self.selector)
        self.black_ring.setObjectName(u"black_ring")
        self.black_ring.setGeometry(QRect(1, 1, 10, 10))
        self.black_ring.setMinimumSize(QSize(10, 10))
        self.black_ring.setMaximumSize(QSize(10, 10))
        self.black_ring.setBaseSize(QSize(10, 10))
        self.black_ring.setStyleSheet(u"background-color: none;\n"
"border: 1px solid black;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.black_overlay)


        self.horizontalLayout.addWidget(self.color_view)

        self.hue_frame = QFrame(ColorSelector)
        self.hue_frame.setObjectName(u"hue_frame")
        self.hue_frame.setMinimumSize(QSize(30, 0))
        self.hue_frame.setStyleSheet(u"QLabel{\n"
"	border-radius: 5px;\n"
"}")
        self.hue_frame.setFrameShape(QFrame.StyledPanel)
        self.hue_frame.setFrameShadow(QFrame.Raised)
        self.hue_bg = QFrame(self.hue_frame)
        self.hue_bg.setObjectName(u"hue_bg")
        self.hue_bg.setGeometry(QRect(10, 0, 20, 200))
        self.hue_bg.setMinimumSize(QSize(20, 200))
        self.hue_bg.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius: 5px;")
        self.hue_bg.setFrameShape(QFrame.StyledPanel)
        self.hue_bg.setFrameShadow(QFrame.Raised)
        self.hue_selector = QLabel(self.hue_frame)
        self.hue_selector.setObjectName(u"hue_selector")
        self.hue_selector.setGeometry(QRect(7, 185, 26, 15))
        self.hue_selector.setMinimumSize(QSize(26, 0))
        self.hue_selector.setStyleSheet(u"background-color: #222;\n"
"")
        self.hue = QFrame(self.hue_frame)
        self.hue.setObjectName(u"hue")
        self.hue.setGeometry(QRect(7, 0, 26, 200))
        self.hue.setMinimumSize(QSize(20, 200))
        self.hue.setStyleSheet(u"")
        self.hue.setFrameShape(QFrame.StyledPanel)
        self.hue.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.hue_frame)

        self.editfields = QFrame(ColorSelector)
        self.editfields.setObjectName(u"editfields")
        sizePolicy1.setHeightForWidth(self.editfields.sizePolicy().hasHeightForWidth())
        self.editfields.setSizePolicy(sizePolicy1)
        self.editfields.setMinimumSize(QSize(120, 200))
        self.editfields.setMaximumSize(QSize(16777215, 16777215))
        self.editfields.setStyleSheet(u"QLabel{\n"
"	font-family: Segoe UI;\n"
"font-weight: bold;\n"
"	font-size: 11pt;\n"
"	color: #aaaaaa;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.editfields.setFrameShape(QFrame.StyledPanel)
        self.editfields.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.editfields)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.red = QLineEdit(self.editfields)
        self.red.setObjectName(u"red")
        sizePolicy.setHeightForWidth(self.red.sizePolicy().hasHeightForWidth())
        self.red.setSizePolicy(sizePolicy)
        self.red.setAlignment(Qt.AlignCenter)
        self.red.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.red, 1, 1, 1, 1)

        self.lbl_green = QLabel(self.editfields)
        self.lbl_green.setObjectName(u"lbl_green")

        self.gridLayout.addWidget(self.lbl_green, 2, 0, 1, 1)

        self.lbl_saturation = QLabel(self.editfields)
        self.lbl_saturation.setObjectName(u"lbl_saturation")

        self.gridLayout.addWidget(self.lbl_saturation, 2, 2, 1, 1)

        self.le_saturation = QLineEdit(self.editfields)
        self.le_saturation.setObjectName(u"le_saturation")
        self.le_saturation.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_saturation, 2, 3, 1, 1)

        self.blue = QLineEdit(self.editfields)
        self.blue.setObjectName(u"blue")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(5)
        sizePolicy3.setHeightForWidth(self.blue.sizePolicy().hasHeightForWidth())
        self.blue.setSizePolicy(sizePolicy3)
        self.blue.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.blue, 3, 1, 1, 1)

        self.lbl_hex = QLabel(self.editfields)
        self.lbl_hex.setObjectName(u"lbl_hex")
        self.lbl_hex.setStyleSheet(u"font-size: 14pt;")

        self.gridLayout.addWidget(self.lbl_hex, 4, 0, 1, 1)

        self.lbl_value = QLabel(self.editfields)
        self.lbl_value.setObjectName(u"lbl_value")

        self.gridLayout.addWidget(self.lbl_value, 3, 2, 1, 1)

        self.le_hue = QLineEdit(self.editfields)
        self.le_hue.setObjectName(u"le_hue")
        self.le_hue.setAlignment(Qt.AlignCenter)
        self.le_hue.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.le_hue, 1, 3, 1, 1)

        self.le_value = QLineEdit(self.editfields)
        self.le_value.setObjectName(u"le_value")
        self.le_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.le_value, 3, 3, 1, 1)

        self.hex = QLineEdit(self.editfields)
        self.hex.setObjectName(u"hex")
        self.hex.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.hex, 4, 1, 1, 3)

        self.color_vis = QLabel(self.editfields)
        self.color_vis.setObjectName(u"color_vis")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.color_vis.sizePolicy().hasHeightForWidth())
        self.color_vis.setSizePolicy(sizePolicy4)
        self.color_vis.setMinimumSize(QSize(90, 0))
        self.color_vis.setMaximumSize(QSize(16777215, 50))
        self.color_vis.setStyleSheet(u"/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: #000;\n"
"")

        self.gridLayout.addWidget(self.color_vis, 0, 0, 1, 4)

        self.lbl_hub = QLabel(self.editfields)
        self.lbl_hub.setObjectName(u"lbl_hub")

        self.gridLayout.addWidget(self.lbl_hub, 1, 2, 1, 1)

        self.lbl_blue = QLabel(self.editfields)
        self.lbl_blue.setObjectName(u"lbl_blue")

        self.gridLayout.addWidget(self.lbl_blue, 3, 0, 1, 1)

        self.lbl_red = QLabel(self.editfields)
        self.lbl_red.setObjectName(u"lbl_red")

        self.gridLayout.addWidget(self.lbl_red, 1, 0, 1, 1)

        self.green = QLineEdit(self.editfields)
        self.green.setObjectName(u"green")
        self.green.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.green, 2, 1, 1, 1)

        self.btn_cancel = QPushButton(self.editfields)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.gridLayout.addWidget(self.btn_cancel, 5, 2, 1, 2)

        self.btn_ok = QPushButton(self.editfields)
        self.btn_ok.setObjectName(u"btn_ok")

        self.gridLayout.addWidget(self.btn_ok, 5, 0, 1, 2)


        self.horizontalLayout.addWidget(self.editfields)

#if QT_CONFIG(shortcut)
        self.lbl_green.setBuddy(self.green)
        self.lbl_saturation.setBuddy(self.green)
        self.lbl_hex.setBuddy(self.blue)
        self.lbl_value.setBuddy(self.blue)
        self.lbl_hub.setBuddy(self.red)
        self.lbl_blue.setBuddy(self.blue)
        self.lbl_red.setBuddy(self.red)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.red, self.green)
        QWidget.setTabOrder(self.green, self.blue)

        self.retranslateUi(ColorSelector)

        QMetaObject.connectSlotsByName(ColorSelector)
    # setupUi

    def retranslateUi(self, ColorSelector):
        ColorSelector.setWindowTitle(QCoreApplication.translate("ColorSelector", u"\u8c03\u8272\u677f", None))
        self.black_ring.setText("")
        self.hue_selector.setText("")
        self.red.setText(QCoreApplication.translate("ColorSelector", u"255", None))
        self.lbl_green.setText(QCoreApplication.translate("ColorSelector", u"G", None))
        self.lbl_saturation.setText(QCoreApplication.translate("ColorSelector", u"S", None))
        self.le_saturation.setText(QCoreApplication.translate("ColorSelector", u"255", None))
        self.blue.setText(QCoreApplication.translate("ColorSelector", u"255", None))
        self.lbl_hex.setText(QCoreApplication.translate("ColorSelector", u"#", None))
        self.lbl_value.setText(QCoreApplication.translate("ColorSelector", u"V", None))
        self.le_hue.setText(QCoreApplication.translate("ColorSelector", u"255", None))
        self.le_value.setText(QCoreApplication.translate("ColorSelector", u"255", None))
        self.hex.setText(QCoreApplication.translate("ColorSelector", u"ffffff", None))
        self.color_vis.setText("")
        self.lbl_hub.setText(QCoreApplication.translate("ColorSelector", u"H", None))
        self.lbl_blue.setText(QCoreApplication.translate("ColorSelector", u"B", None))
        self.lbl_red.setText(QCoreApplication.translate("ColorSelector", u"R", None))
        self.green.setText(QCoreApplication.translate("ColorSelector", u"255", None))
        self.btn_cancel.setText(QCoreApplication.translate("ColorSelector", u"\u53d6\u6d88", None))
        self.btn_ok.setText(QCoreApplication.translate("ColorSelector", u"\u786e\u5b9a", None))
    # retranslateUi

