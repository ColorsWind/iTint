# This Python file uses the following encoding: utf-8
import time

import numpy as np
from PySide2.QtCore import Qt, QUrl, QSize, QEventLoop
from PySide2.QtGui import QPixmap, QDropEvent, QDragEnterEvent, QMouseEvent, QResizeEvent, QHideEvent
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QFileDialog, QWidgetItem

from octree import Octree
from ui_widget import Ui_MainWidget
from widget_color_display import qimage_to_pil, ColorDisplayWidget
from widget_screen_color_picker import ScreenColorPicker
from widget_screenshot import WidgetScreenShot


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.internal_loader = Ui_MainWidget()
        self.internal_loader.setupUi(self)
        self.screen = WidgetScreenShot()
        self.picker = ScreenColorPicker()
        self.layout = QHBoxLayout(self.internal_loader.colorDisplayContent)
        self.layout.setAlignment(Qt.AlignLeft)
        self.internal_loader.btnFromScan.clicked.connect(self.btn_from_screen)
        self.default_text = self.internal_loader.labelImagePreview.text()
        self.internal_loader.labelImagePreview.mousePressEvent = self.btn_from_file
        self.internal_loader.btnColorPickup.clicked.connect(self.btn_from_screen_color_picker)
        self.internal_loader.btnFromClipboard.clicked.connect(self.btn_from_clipboard)

        self.pixmap = QPixmap()
        self.hide_callback = None

    def dropEvent(self, event: QDropEvent) -> None:
        url: QUrl = event.mimeData().urls()[0]
        self.pixmap.load(url.toLocalFile())
        self.update_image()
        if not self.pixmap.isNull():
            self.update_color_display(self.pixmap)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls() and event.mimeData().urls()[0].isLocalFile():
            event.acceptProposedAction()

    def check_and_clear_color_display(self):
        if self.internal_loader.cBtnAutoClear.isChecked():
            for i in range(self.layout.count()):
                color_display_widget: QWidgetItem = self.layout.itemAt(i)
                color_display_widget.widget().deleteLater()

    def update_color_display(self, image: QPixmap):
        if image.isNull():
            return
        data = np.asarray(qimage_to_pil(image)).reshape((-1, 3))
        tree = Octree()
        tree.build(data, 8)

        colors = tree.get_color(tree.root)
        self.check_and_clear_color_display()

        for r, g, b in colors:
            color_display_widget = ColorDisplayWidget(r, g, b, self)
            self.layout.addWidget(color_display_widget)

    def resizeEvent(self, event: QResizeEvent):
        self.update_image()

    def hideEvent(self, event: QHideEvent):

        if self.hide_callback is not None:
            self.hide_callback()
            self.hide_callback = None

    def update_image(self):
        if self.pixmap.isNull():
            self.internal_loader.labelImagePreview.setText(self.default_text)
        else:
            pixel_ratio = QApplication.primaryScreen().devicePixelRatio()
            pixmap_aspect = self.pixmap.width() / self.pixmap.height()
            label_width = self.internal_loader.labelImagePreview.width() * pixel_ratio
            label_height = self.internal_loader.labelImagePreview.height() * pixel_ratio
            label_aspect = label_width / label_height
            if pixmap_aspect > label_aspect:
                pixmap = self.pixmap.scaled(
                    QSize(label_width,
                          label_width / pixmap_aspect),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )
            else:
                pixmap = self.pixmap.scaled(
                    QSize(label_height * pixmap_aspect,
                          label_height),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )
            self.internal_loader.labelImagePreview.setPixmap(pixmap)

    def btn_from_screen_color_picker(self):

        def callback_screen_color_picker(rgb):
            r, g, b = rgb
            color_display_widget = ColorDisplayWidget(r, g, b, self)
            self.layout.addWidget(color_display_widget)
            if self.internal_loader.cBtnAutoHide.isChecked():
                self.setVisible(True)
                self.setWindowOpacity(1.0)

        if self.internal_loader.cBtnAutoHide.isChecked():
            self.setVisible(False)
            self.setWindowOpacity(0.0)
            QApplication.processEvents(QEventLoop.AllEvents)
            # time.sleep(0.20) # 窗口动画
        self.picker.pick_color(callback=callback_screen_color_picker)

    def btn_from_screen(self):

        def callback_captured_image(pixmap: QPixmap):
            self.pixmap = pixmap
            self.update_image()
            if self.internal_loader.cBtnAutoHide.isChecked():
                self.setVisible(True)
            self.update_color_display(pixmap)

        if self.internal_loader.cBtnAutoHide.isChecked():
            self.setVisible(False)
        self.screen.capture_screen(callback=callback_captured_image)


    def btn_from_file(self, event: QMouseEvent):
        filepath, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "图片 (*.png;*.jpg;*.gif;*.bmp);;所有类型 (*)")
        self.pixmap.load(filepath)
        self.update_image()
        if not self.pixmap.isNull():
            self.update_color_display(self.pixmap)

    def btn_from_clipboard(self):
        clipboard = QApplication.clipboard()
        self.pixmap = clipboard.pixmap()
        self.update_image()
        self.update_color_display(self.pixmap)


