import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Buttunlar seryasi")
        self.resize(300, 200)
        
        self.a = input("So'zni kiriting")

        self.b1 = QPushButton("Button1", self)
        self.b1.setFont(QFont("Arial", 14))
        self.b1.clicked.connect(self.add_form1_btn)

        self.b2 = QPushButton("Button2", self)
        self.b2.setFont(QFont("Arial", 14))
        self.b2.clicked.connect(self.add_form2_btn)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.setLayout(self.vbox)

    def add_form1_btn(self):
        form1_button = QLineEdit(self.a, self)
        form1_button.setFont(QFont("Arial", 12))
        self.vbox.addWidget(form1_button)

    def add_form2_btn(self):
        form2_button = QLineEdit(self.a, self)
        form2_button.setFont(QFont("Arial", 12))
        self.vbox.addWidget(form2_button)

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
