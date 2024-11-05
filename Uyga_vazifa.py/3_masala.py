##############
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Uch_xonali_son")
        self.setFixedSize(500, 350)

        self.input_line = QLineEdit()

        self.ok_button = QPushButton("Ok")
        self.ok_button.setFixedSize(100, 60)
        self.output_buttons = [QPushButton() for i in range(3  )]

        layout = QVBoxLayout()
        layout.addWidget(self.input_line)
        layout.addWidget(self.ok_button)
        for button in self.output_buttons:
            layout.addWidget(button)

        self.setLayout(layout)

        self.ok_button.clicked.connect(self.display_digits)

    def display_digits(self):
        for button in self.output_buttons:
            button.setText("")

        number = self.input_line.text()
        if not number.isdigit() or not (1 <= int(number) <= 1000):
            QMessageBox.warning(self, "Xato", "Iltimos, 1 dan 1000 gacha bo'lgan raqam kiriting.")
            return

        for i, digit in enumerate(number):
            if i < 3:
                self.output_buttons[i].setText(digit)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
