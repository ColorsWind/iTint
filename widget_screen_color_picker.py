from PySide2.QtCore import Qt, QPoint, QSize
from PySide2.QtGui import QGuiApplication, QPainter, QColor, QCursor, QPixmap, QMouseEvent
from PySide2.QtWidgets import QWidget, QApplication

winSize = QSize(135, 100)
sizeOfMouseIcon = 20
magnificationTimes = 10
split = 0.7


class WidgetScreenColorPicker(QWidget):

    def __init__(self, parent):
        super(WidgetScreenColorPicker, self).__init__(parent)
        self.setFixedSize(winSize)
        self.setMouseTracking(True)
        self.screenshot = None
        self.color = QColor(0, 0, 0)

    def get_color(self):
        return self.color

    def update_location(self):
        cursor_pos = QCursor.pos()
        show_pos: QPoint = cursor_pos + QPoint(20, -(winSize.height() + 20))
        if show_pos.y() < 0:
            show_pos.setY(show_pos.y() + winSize.height() + sizeOfMouseIcon)
        if show_pos.x() + winSize.width() > self.parent().width():
            show_pos.setX(show_pos.x() - (winSize.width() + sizeOfMouseIcon))
        self.move(show_pos)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        cursor_pos = QCursor.pos()
        # 截图
        ratio = QApplication.primaryScreen().devicePixelRatio()
        screenshot = self.screenshot.copy(
            (cursor_pos.x() - winSize.width() / magnificationTimes / 2) * ratio,
            (cursor_pos.y() - winSize.height() * split / magnificationTimes / 2) * ratio,
            (winSize.width() / magnificationTimes) * ratio,
            (winSize.height() * split / magnificationTimes) * ratio,
        )
        painter.drawPixmap(0, 0, winSize.width(), winSize.height() * split, screenshot)
        pixmap = screenshot.copy(
            (winSize.width() / magnificationTimes / 2) * ratio,
            (winSize.height() * split / magnificationTimes / 2) * ratio,
            1,
            1,
        )
        self.color = QColor(pixmap.toImage().pixel(0, 0))
        if self.color.red() > 100 and self.color.blue() > 100 and self.color.green() > 100:
            painter.setPen(QColor(0, 0, 0))
        else:
            painter.setPen(QColor(255, 255, 255))

        painter.fillRect(
            0,
            winSize.height() * split,
            winSize.width() - 1,
            winSize.height() * (1 - split),
            QColor(100, 100, 100),
        )

        painter.drawRect(0, 0, self.rect().width() - 1, self.rect().height() - 1)
        painter.fillRect(4, 74, 22, 22, self.color)
        # painter.drawLine(50, 30, 50, 40)
        # painter.drawLine(45, 35, 55, 35)
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(32, 82, "RGB")
        painter.drawText(32, 95, "%d,%d,%d" % (
            (self.color.red() - 1) * 255 / 254, (self.color.green() - 1) * 255 / 254,
            (self.color.blue() - 1) * 255 / 254))


class WidgetScreenBackground(QWidget):

    def __init__(self, screenshot=None, parent=None):
        super(WidgetScreenBackground, self).__init__(parent)
        self.callback = None
        self.screenshot = screenshot
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        # self.setAttribute(Qt.WA_InputMethodTransparent, False)
        self.is_picking = False
        desktop_rect = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(desktop_rect)
        self.setCursor(Qt.CrossCursor)
        self.setMouseTracking(True)
        self.internal_picker = WidgetScreenColorPicker(self)

    def paintEvent(self, event):
        if self.screenshot is not None:
            painter = QPainter(self)
            painter.drawPixmap(0, 0, self.screenshot)

    def mousePressEvent(self, event):
        self.is_picking = False
        if event.button() == Qt.LeftButton:
            self.setVisible(False)
            self.internal_picker.setVisible(False)
            if self.callback is not None:
                color = self.internal_picker.get_color()
                self.callback((color.red(), color.green(), color.blue()))
                self.callback = None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.is_picking:
            self.internal_picker.update_location()

    def pick_color(self, screenshot, callback=None):
        self.callback = callback
        self.screenshot = screenshot
        self.setVisible(True)
        self.is_picking = True
        self.internal_picker.screenshot = screenshot
        self.internal_picker.update_location()
        self.internal_picker.setVisible(True)


class ScreenColorPicker(object):

    def __init__(self):
        self.background = WidgetScreenBackground()
        self.internal_picker = self.background.internal_picker

    def pick_color(self, callback=None):
        screenshot: QPixmap = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        self.background.pick_color(screenshot, callback)
