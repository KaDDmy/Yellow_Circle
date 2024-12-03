import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import QRect


class Window(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Рисование кругов")
        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        x = random.randint(50, self.width() - 100)
        y = random.randint(50, self.height() - 100)
        diameter = random.randint(20, 100)

        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for x, y, d in self.circles:
            painter.setBrush(QBrush(QColor("yellow")))
            painter.drawEllipse(QRect(x, y, d, d))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())