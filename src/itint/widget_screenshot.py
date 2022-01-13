from PySide2.QtCore import Qt, QPoint, QRect
from PySide2.QtGui import QGuiApplication, QBitmap, QPainter, QPen, QBrush, QPaintEvent, QMouseEvent, QCursor
from PySide2.QtWidgets import QWidget, QApplication

from itint.utils import get_real_coordinate


class WidgetScreenShot(QWidget):

    def __init__(self, parent=None):
        super(WidgetScreenShot, self).__init__(parent)
        self.callback = None
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.6)
        desktop_rect = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(desktop_rect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktop_rect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.is_drawing = False
        self.start_point = QPoint()
        self.end_point = QPoint()

    def paintEvent(self, event: QPaintEvent):
        if self.is_drawing:
            self.mask = self.blackMask.copy()
            pp = QPainter(self.mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen)
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self.start_point, self.end_point))
            self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.end_point = self.start_point
            self.is_drawing = True

    def mouseMoveEvent(self, event):
        if self.is_drawing:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 防止发送错误导致一直处于截屏状态
            screen_region = None
            try:
                self.end_point = event.pos()
                screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
                rect = QRect(get_real_coordinate(self.start_point), get_real_coordinate(self.end_point))
                screen_region = screenshot.copy(rect)
                screen_region.mask()
            except Exception as e:
                print(e)
            finally:
                self.is_drawing = False
                self.clearMask()
                self.setVisible(False)
            if self.callback is not None and screen_region is not None:
                self.callback(screen_region)
                self.callback = None

    def capture_screen(self, callback=None):
        self.callback = callback
        self.setVisible(True)
