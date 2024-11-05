import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(500, 250)
        self.setWindowTitle("PyQt5 - OOP")

        self.label = QLabel(self)
        self.label.setText("Salom dunyo")
        font = QFont("Arial", 18)
        self.label.setFont(font)
        self.label.move(180, 100)

        self.btn_1 = QPushButton("Tugmani bosing", self)
        self.btn_1.setFont(QFont("Arial", 14))
        self.btn_1.move(180, 180)
        self.btn_1.clicked.connect(self.xabar_chiq)

        self.is_hello = True

    def xabar_chiq(self):
        if self.is_hello:
            self.label.setText("Hello World")
        else:
            self.label.setText("Salom dunyo")
        self.is_hello = not self.is_hello
def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
