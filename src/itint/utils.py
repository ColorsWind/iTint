from PySide2.QtCore import QPoint
from PySide2.QtWidgets import QApplication


def get_real_coordinate(point: QPoint) -> QPoint:
    ratio = QApplication.primaryScreen().devicePixelRatio()
    return QPoint(point.x() * ratio, point.y() * ratio)


def get_real_length(l: float) -> float:
    ratio = QApplication.primaryScreen().devicePixelRatio()
    return ratio * l
