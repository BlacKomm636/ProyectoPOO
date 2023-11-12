from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton

from controlers.CocineroControler import Cocinero
from controlers.MensajeControler import Ui_DialogMensaje
from models.Respuesta import Respuesta


class LoginCocinero(QMainWindow):
    def __init__(self, parent=None):
        super(LoginCocinero, self).__init__(parent)
        self.setupUI()
    def setupUI(self):
        uic.loadUi("Vistas/ui_files/loginCocinero.ui", self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        # Definición de componentes
        self.user_name = self.findChild(QLineEdit, 'lineEditUser')
        self.password = self.findChild(QLineEdit, 'lineEditPassword')
        self.iconMenu = self.findChild(QPushButton, "btn_icon")
        self.login = self.findChild(QPushButton, "btnIngresar")

        # Carga de iconos y métodos

    def connectCocinero(self, user, password):
        user = Cocinero.obtenerCocinero(self, user, password)
        if user:
            uic.loadUi("Vistas/ui_files/Admi.G(mostrarusuarios).ui", self)
        else:
            respuesta = Respuesta("error", "Error!", "Usuario y/o contraseña incorrectos!")
            Ui_DialogMensaje(respuesta)
            self.findChild(QLineEdit, 'lineEditUser').setText("")
            self.findChild(QLineEdit, 'lineEditPassword').setText("")