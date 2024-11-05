import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b2 = QLabel(w)
    btn = QPushButton(w)
    btn.setText("Tugmacha")
    b.setText("Salom Dunyo")
    b2.setText("Hello World")
    w.setGeometry(100,100,200,50)
    b.move(50,20)
    b2.move(50,60)
    btn.move(50, 90)
    w.setWindowTitle("PyQt5")
    w.show()
    sys.exit(app.exit())

if __name__ == '__main__':
    window()
