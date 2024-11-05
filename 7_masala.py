import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    # QVBoxLayout ichida tugmalar
    b1 = QPushButton("QVBoxLayout - Button 1")
    b2 = QPushButton("QVBoxLayout - Button 2")
    vbox = QVBoxLayout()
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(b2)

    hbox = QHBoxLayout()
    b3 = QPushButton("QHBoxLayout - Button 1")
    b4 = QPushButton("QHBoxLayout - Button 2")
    hbox.addWidget(b3)
    hbox.addStretch()
    hbox.addWidget(b4)

    vbox.addStretch()
    vbox.addLayout(hbox)

    win.setLayout(vbox)
    win.setWindowTitle("QBox Layout")
    win.resize(300, 200)
    win.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
