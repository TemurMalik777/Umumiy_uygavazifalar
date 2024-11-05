import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(500, 300)
        self.setWindowTitle("PyQt5 - OOP")

        self.label = QLabel("Salom dunyo", self)
        font = QFont("Arial", 18)
        self.label.setFont(font)
        self.label.move(150, 100)
        self.label.hide()

        self.button = QPushButton("Tugmani bosing", self)
        self.button.setFont(QFont("Arial", 14))
        self.button.move(180, 180)
        self.button.clicked.connect(self.show_message) 

    def show_message(self):
        self.label.show() 

def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
