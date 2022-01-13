import io
import time

import numpy as np
from PIL import Image
from PySide2.QtCore import QBuffer, QEventLoop
from PySide2.QtGui import QImage, QPalette, QColor
from PySide2.QtWidgets import QWidget, QApplication

from ui_color_display import Ui_ColorDisplay

from widget_color_selector import ColorSelectorWidget


def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v


def float_to_str(f):
    return "%.2f" % f


def qimage_to_pil(image: QImage):
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    image.save(buffer, "PNG")
    pil_image: Image = Image.open(io.BytesIO(buffer.data()))
    pixels = 10000
    ratio = np.sqrt(pixels / (pil_image.size[0] * pil_image.size[1]))
    pil_image = pil_image.resize((int(pil_image.size[0] * ratio), int(pil_image.size[1] * ratio)))
    return pil_image


class ColorDisplayWidget(QWidget):
    def __init__(self, r, g, b, parent):
        super(ColorDisplayWidget, self).__init__(parent)
        self.main_widget = parent
        self.internal_loader = Ui_ColorDisplay()
        self.internal_loader.setupUi(self)
        self.internal_loader.textRGB1.setText(float_to_str(r))
        self.internal_loader.textRGB2.setText(float_to_str(g))
        self.internal_loader.textRGB3.setText(float_to_str(b))
        h, s, v = rgb_to_hsv(r, g, b)
        self.internal_loader.textHSB1.setText(float_to_str(r))
        self.internal_loader.textHSB2.setText(float_to_str(g))
        self.internal_loader.textHSB3.setText(float_to_str(v))
        self.internal_loader.labelColor.setVisible(False)
        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(r, g, b))
        self.internal_loader.frameColor.setPalette(self.pal)

        self.internal_loader.btnCopyRGB.clicked.connect(self.btn_copy_rgb)
        self.internal_loader.btnCopyHSB.clicked.connect(self.btn_copy_hsb)
        self.internal_loader.btnEdit.clicked.connect(self.btn_edit)
        self.internal_loader.btnPick.clicked.connect(self.btn_pick)
        self.internal_loader.btnRemove.clicked.connect(self.btn_remove)

    def btn_copy_rgb(self):
        clipboard = QApplication.clipboard()
        r = self.internal_loader.textRGB1.text()
        g = self.internal_loader.textRGB2.text()
        b = self.internal_loader.textRGB3.text()
        clipboard.setText(f"{r}, {g}, {b}")

    def btn_copy_hsb(self):
        clipboard = QApplication.clipboard()
        h = self.internal_loader.textHSB1.text()
        s = self.internal_loader.textHSB2.text()
        b = self.internal_loader.textHSB3.text()
        clipboard.setText(f"{h}, {s}, {b}")

    def btn_edit(self):
        r = self.internal_loader.textRGB1.text()
        g = self.internal_loader.textRGB2.text()
        b = self.internal_loader.textRGB3.text()
        color_selector_widget = ColorSelectorWidget(rgb=(float(r), float(g), float(b)))
        color_selector_widget.callback = self.callback_edit
        color_selector_widget.show()

    def callback_edit(self, rgb):
        if rgb is None:
            return
        r, g, b = rgb
        self.internal_loader.textRGB1.setText(float_to_str(r))
        self.internal_loader.textRGB2.setText(float_to_str(g))
        self.internal_loader.textRGB3.setText(float_to_str(b))

        h, s, v = rgb_to_hsv(r, g, b)
        self.internal_loader.textHSB1.setText(float_to_str(h))
        self.internal_loader.textHSB2.setText(float_to_str(s))
        self.internal_loader.textHSB3.setText(float_to_str(v))

        self.pal.setColor(QPalette.Background, QColor(r, g, b))
        self.internal_loader.frameColor.setPalette(self.pal)

    def btn_pick(self):
        def callback_pick(rgb):
            if self.main_widget.internal_loader.cBtnAutoHide.isChecked():
                self.main_widget.setVisible(True)
                self.callback_edit(rgb)

        if self.main_widget.internal_loader.cBtnAutoHide.isChecked():
            self.main_widget.setVisible(False)
            QApplication.processEvents(QEventLoop.AllEvents)
            time.sleep(0.20) # 窗口动画
        self.main_widget.picker.pick_color(callback=callback_pick)



    def btn_remove(self):
        self.deleteLater()
