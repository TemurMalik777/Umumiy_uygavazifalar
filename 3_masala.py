import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(500, 250)
        self.setWindowTitle("PyQt5 - OOP")

        a = "Salom dunyo"
        b = "Hello World"

        self.label = QLabel(self)
        self.label_2 = QLabel(self)
        self.label.setText(a)
        self.label_2.setText(b)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.move(150, 120)

        self.label_2.setFont(font)
        self.label_2.move(100, 90)

        self.btn_1 = QPushButton("Tugmani bosing", self)
        self.btn_1.setFont(QFont("Arial", 14))
        self.btn_1.move(180, 180)
        self.btn_1.clicked.connect(self.show_message)

    def show_message(self):
        self.label.show()

def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
