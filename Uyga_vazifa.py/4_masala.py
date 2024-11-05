import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        
        self.w = QWidget()
        self.b = QLabel(self.w)
        self.b.setText("Salom dunyo")
        self.w.setGeometry(300, 300, 500, 300)
        self.b.move(50, 20)

        self.w.setWindowTitle("PyQt5->MessageBox")
        font = QFont()
        font.setPointSize(16)
        self.w.setFont(font)

        self.initUI()

    def initUI(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "PyQt5 ni yoqtirasizmi?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if buttonReply == QMessageBox.Yes:
            self.b.setText('Yes tugmasi bosildi. Rahmat')
        else:
            self.b.setText('No tugmasi bosildi.\n Yoqtirmasangiz ham iloji qancha')
        
        self.w.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())