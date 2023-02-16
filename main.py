from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow, QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mainwindow.ui", self)
        self.password_check.stateChanged.connect(self.pass_show)
        self.login_button.clicked.connect(self.login)
        self.show()

    def pass_show(self, state):
        if state == 2:
            self.password_field.setEchoMode(QLineEdit.Normal)
        elif state == 0:
            self.password_field.setEchoMode(QLineEdit.Password)
    def login(self):
        if self.username.text() == 'ashish' and self.password_field.text() == 'ashish':
            self.home()
    def home(self):
        loadUi("home.ui", self)
        self.logout.clicked.connect(self.close)
    def close(self):
        sys.exit()

app = QApplication([])
window = MainWindow()
app.exec()
