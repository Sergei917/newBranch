import time
import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QPainter, QColor


class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui')

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw(qp)
        # Завершаем рисование
        qp.end()

    def draw():
        x, y, d = random.randint(300), randow.randint(200), random.randint(111)
        self.Pixmap = QPixmap(screen)
        self.image = QLabel(self)
        self.image.setPixmap(self.Pixmap)
        self.qp
        qp.draw.ellipse((x, y, x + d, y + d), QColor('yellow'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec_())
