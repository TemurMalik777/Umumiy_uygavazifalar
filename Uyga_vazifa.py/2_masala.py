import sys
from PyQt5.QtWidgets import *

class TetrisWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tetris o'yini")
        self.setGeometry(700, 300, 300, 400)


        self.main_layout = QVBoxLayout()

        self.shape_buttons = []
        for i in range(1, 5):
            btn = QPushButton(f"Shakl {i}", self)
            btn.clicked.connect(lambda _, x=i: self.show_shape_buttons(x))
            self.main_layout.addWidget(btn)
            self.shape_buttons.append(btn)

        self.shape_display = QWidget(self)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(5) 
        self.shape_display.setLayout(self.grid_layout)
        self.main_layout.addWidget(self.shape_display)
        
        self.setLayout(self.main_layout)

    def show_shape_buttons(self, shape_id):
        for i in reversed(range(self.grid_layout.count())): 
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        if shape_id == 1:
            self.create_button(0, 1, "cyan")
            self.create_button(1, 1, "cyan")
            self.create_button(2, 1, "cyan")
            self.create_button(2, 0, "cyan")
        
        elif shape_id == 2:
            self.create_button(0, 0, "magenta")
            self.create_button(0, 1, "magenta")
            self.create_button(1, 0, "magenta")
            self.create_button(1, 1, "magenta")
        
        elif shape_id == 3:
            self.create_button(0, 0, "blue")
            self.create_button(0, 1, "blue")
            self.create_button(0, 2, "blue")
            self.create_button(0, 3, "blue")
        
        elif shape_id == 4:
            self.create_button(0, 1, "red")
            self.create_button(1, 0, "red")
            self.create_button(1, 1, "red")
            self.create_button(1, 2, "red")

    def create_button(self, row, col, color):
        btn = QPushButton(self)
        btn.setFixedSize(50, 50)
        btn.setStyleSheet(f"background-color: {color}; border: none;")
        self.grid_layout.addWidget(btn, row, col)

def main():
    app = QApplication(sys.argv)
    win = TetrisWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
