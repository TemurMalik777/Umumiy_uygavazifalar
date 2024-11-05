import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import os

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Login System")
        self.resize(400, 250)

        self.label_login = QLabel("Login:")
        self.label_login.setFont(QFont("Arial", 15))
        self.line_login = QLineEdit()
        self.line_login.setFixedWidth(200)
        self.line_login.setFixedHeight(30)
        font = QFont("Arial", 12)
        self.line_login.setFont(font)

        self.label_password = QLabel("Parol:")
        self.label_password.setFont(QFont("Arial", 15))
        self.line_password = QLineEdit()
        self.line_password.setFixedWidth(200)
        self.line_password.setEchoMode(QLineEdit.Password)
        self.line_password.setFixedHeight(30)
        font = QFont("Arial, 12")
        self.line_password.setFont(font)

        self.btn_signin = QPushButton("Kirish")
        self.btn_signin.setFont(QFont("Arial", 8))
        self.btn_signin.setFixedSize(100, 30)

        self.btn_signin.clicked.connect(self.sign_in)

        self.btn_signup = QPushButton("Ro'yxatdan o'tish")
        self.btn_signup.setFont(QFont("Arial", 12))
        self.btn_signup.clicked.connect(self.sign_up)

        login_layout = QHBoxLayout()
        login_layout.addWidget(self.label_login)
        login_layout.addWidget(self.line_login)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.label_password)
        password_layout.addWidget(self.line_password)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_signin)
        button_layout.addWidget(self.btn_signup)

        main_layout = QVBoxLayout()
        main_layout.addLayout(login_layout)
        main_layout.addLayout(password_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def sign_in(self):
        login = self.line_login.text()
        password = self.line_password.text()

        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
        else:
            users = []

        if any(user["login"] == login and user["password"] == password for user in users):
            QMessageBox.information(self, "Tizimga kirish", "Siz tizimga kirdingiz")
        else:
            QMessageBox.warning(self, "Xatolik", "Login yoki parol noto'g'ri")

    def sign_up(self):
        login = self.line_login.text()
        password = self.line_password.text()

        
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
        else:
            users = []

        
        if not any(user["login"] == login for user in users):
            users.append({"login": login, "password": password})
            with open("users.json", "w") as file:
                json.dump(users, file, indent=4)
            QMessageBox.information(self, "Ro'yhatga qo'shish", "Login va parol qo'shildi")
        else:
            QMessageBox.warning(self, "Xatolik", "Bu login allaqachon mavjud")

def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
