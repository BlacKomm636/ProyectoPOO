from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton

from controlers.AdministradorGeneralControler import AdministradorGeneral
from controlers.MensajeControler import Ui_Dialog
from models.Respuesta import Respuesta


class LoginAdminGeneral(QMainWindow):
    def __init__(self, parent=None):
        super(LoginAdminGeneral, self).__init__(parent)
        self.setupUI()
    def setupUI(self):
        uic.loadUi("Vistas/loginAdminitradorGeneral.ui", self)
        # Configura las flags para eliminar el encabezado y los botones de cierre
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        # Definición de componentes
        self.user_name = self.findChild(QLineEdit, 'lineEdit')
        self.password = self.findChild(QLineEdit, 'lineEdit_2')
        self.iconMenu = self.findChild(QPushButton, "btn_icon")

        # Carga de iconos y métodos
        self.iconMenu.setIcon(QIcon("assets/imagenAdministradorGeneral.png"))
        self.user_name.addAction(QIcon("assets/user-solid.svg"), QLineEdit.ActionPosition(1))
        self.password.addAction(QIcon("assets/candado.svg"), QLineEdit.ActionPosition(1))
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(
            lambda: self.connectAdministradorGeneral(self.user_name.text(), self.password.text()))
        self.findChild(QPushButton, 'btn_back').clicked.connect(self.hide)
    def connectAdministradorGeneral(self, user, password):
        usuarioAdmin = AdministradorGeneral.obtenerUsuarioAdministrador(self, user, password)
        if usuarioAdmin:
            uic.loadUi("Vistas/Admi.G(mostrarusuarios).ui", self)
        else:
            respuesta = Respuesta("error", "Error!", "Usuario y/o contraseña incorrectos!")
            Ui_Dialog(respuesta)
            self.findChild(QLineEdit, 'lineEdit').setText("")
            self.findChild(QLineEdit, 'lineEdit_2').setText("")

