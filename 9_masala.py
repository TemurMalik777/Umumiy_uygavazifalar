# import sys
# from PyQt5.QtWidgets import *
# def window():
#   app = QApplication(sys.argv)
#   win = QWidget()
#   grid = QGridLayout()

#   for i in range(1, 5):
#     for j in range(1, 5):
#       grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j)
      
#   win.setLayout(grid)

#   win.setGeometry(100, 100, 200, 100)
#   win.setWindowTitle("PyQt Grid Layout")
#   win.show()
#   sys.exit(app.exec_())
  
# if __name__ == '__main__':
#   window()

import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
win = QWidget()
grid = QGridLayout()
layout = QGridLayout()
buttons = {}

def window():

    button = QPushButton(btn_text)
    for i in range(1, 5):
        for j in range(1, 5):
            # grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j)
            btn_text = f"B{i}{j}"
            button = QPushButton(btn_text)
            buttons[btn_text] = button
            layout.addWidget(button, i, j)

    buttons["B11"].clicked.connect(hide_b44)
    button.hide()
    win.setLayout(layout)
    

    win.setLayout(grid)
    win.setGeometry(100, 100, 200, 100)
    win.setWindowTitle("PyQt Grid Layout")
    win.show()
    sys.exit(app.exec_())

def hide_b44():
    buttons["B44"].hide()

if __name__ == '__main__':
    window()
