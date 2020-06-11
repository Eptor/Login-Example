from PyQt5 import QtCore, QtGui, QtWidgets

user_icon = "img/single-neutral-focus.png"

class Ui_login_window(object):

    """ Login window definition """

    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(291, 108)
        login_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        login_window.setWindowIcon(QtGui.QIcon(user_icon))
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(10, 70, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(10, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        self.user_input.setFont(font)
        self.user_input.setAlignment(QtCore.Qt.AlignCenter)
        self.user_input.setObjectName("user_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(10, 40, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName("password_input")
        login_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Login"))
        self.login_button.setText(_translate("login_window", "LOGIN"))
        self.user_input.setPlaceholderText(_translate("login_window", "USERNAME"))
        self.password_input.setPlaceholderText(_translate("login_window", "CONTRASEÑA"))
