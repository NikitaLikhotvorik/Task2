import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Генерация флага')
        self.pushButton.clicked.connect(lambda: self.run())
        self.number = 0
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(QColor(255, 255, 0))
        qp.setPen(pen)
        d = randint(0, 500)
        qp.drawEllipse(randint(0, 500), randint(0, 500), d, d)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())