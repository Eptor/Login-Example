# Local modules
from Windows import login

# Vanilla modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sys

# icon grabbed from https://www.streamlineicons.com/
user_icon = "img/single-neutral-focus.png"

users = {
    "user" : "admin123"
}

class login_class(QMainWindow, login.Ui_login_window):
    """ Handles the login window events """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.login_button.clicked.connect(self.check)  # Connects the button to an action

    def check(self):

        """ Checks if the given credentials are inside the database, in this case, a dictionary """

        if self.user_input.text() in users and self.password_input.text() == users[self.user_input.text()]:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon(user_icon))
            msg.setText("Successfull!")
            msg.setInformativeText("The credentials are correct.")
            msg.setWindowTitle("login")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon(user_icon))
            msg.setText("Error!")
            msg.setInformativeText("The credentials are incorrect.")
            msg.setWindowTitle("login")
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(open("style.css").read())
    login_gui = login_class()
    login_gui.show()
    sys.exit(app.exec_())
