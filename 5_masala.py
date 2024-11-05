import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt Toggle Buttons")
        self.resize(300, 200)

        self.b1 = QPushButton("Button1", self)
        self.b1.setFont(QFont("Arial", 14))
        self.b1.clicked.connect(self.show_b2)

        self.b2 = QPushButton("Button2", self)
        self.b2.setFont(QFont("Arial", 14))
        self.b2.hide() 
        self.b2.clicked.connect(self.show_b1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.b1)
        vbox.addWidget(self.b2)
        self.setLayout(vbox)

    def show_b2(self):
        self.b1.hide()
        self.b2.show()

    def show_b1(self):
        self.b2.hide()
        self.b1.show()

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
