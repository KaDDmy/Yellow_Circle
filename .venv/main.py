import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import QRect


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Рисование кругов")
        self.setGeometry(0, 0, 500, 500)

        self.button = QPushButton("Нарисовать круг", self)
        self.button.setGeometry(170, 30, 141, 31)
        self.button.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        x = random.randint(50, self.width() - 100)
        y = random.randint(50, self.height() - 100)
        diameter = random.randint(20, 100)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for x, y, d, color in self.circles:
            painter.setBrush(QBrush(color))
            painter.drawEllipse(QRect(x, y, d, d))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())