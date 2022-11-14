import sys

from PyQt5.QtCore import Qt, QPoint
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.figure = 0
        self.coords = [0, 0]

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Circles')

    def mousePressEvent(self, event):
        self.coords = [event.x(), event.y()]
        if event.button() == Qt.LeftButton:
            self.figure = 1
            self.update()

    def mouseMoveEvent(self, event):
        self.coords = [event.x(), event.y()]

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.figure == 1:
            self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        x, y = self.coords
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0))
        #qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        #qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        size = randint(10, 100)
        print(x, y)
        qp.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleDrawer()
    ex.show()
    sys.exit(app.exec_())


