from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton

from controlers.MensajeControler import Ui_DialogMensaje
from controlers.MeseroControler import Mesero
from models.Respuesta import Respuesta


class LoginMesero(QMainWindow):
    def __init__(self, parent=None):
        super(LoginMesero, self).__init__(parent)
        self.setupUI()
    def setupUI(self):
        uic.loadUi("Vistas/ui_files/loginMesero.ui", self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        # Definición de componentes
        self.user_name = self.findChild(QLineEdit, 'lineEditUser')
        self.password = self.findChild(QLineEdit, 'lineEditPassword')
        self.iconMenu = self.findChild(QPushButton, "btn_icon")
        self.login = self.findChild(QPushButton, "btnIngresar")

        # Carga de iconos y métodos
        self.iconMenu.setIcon(QIcon("assets/mesero.png"))
        self.user_name.addAction(QIcon("assets/user-solid.svg"), QLineEdit.ActionPosition(1))
        self.password.addAction(QIcon("assets/candado.svg"), QLineEdit.ActionPosition(1))
        self.login.clicked.connect(
            lambda: self.connectMesero(self.user_name.text(), self.password.text()))
        self.findChild(QPushButton, 'btn_back').clicked.connect(self.hide)
    def connectMesero(self, user, password):
        user = Mesero.obtenerMesero(self, user, password)
        if user:
            uic.loadUi("Vistas/ui_files/VentasDiaMesero.ui", self)
        else:
            respuesta = Respuesta("error", "Error!", "Usuario y/o contraseña incorrectos!")
            Ui_DialogMensaje(respuesta)
            self.findChild(QLineEdit, 'lineEditUser').setText("")
            self.findChild(QLineEdit, 'lineEditPassword').setText("")