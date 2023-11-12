from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton

from Vistas.AGCrearUsuariosView import AGCrearUsuarios
from controlers.QuestionControler import Ui_DialogQuestion
from models.Pregunta import Pregunta


class AGMostrarUsuarios(QMainWindow):
    def __init__(self, parent=None):
        super(AGMostrarUsuarios, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        uic.loadUi("Vistas/ui_files/Admi.G(mostrarusuarios).ui", self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        #Definir componentes
        self.crearUsuario = self.findChild(QPushButton, "btnCrearUsuario")
        self.locales = self.findChild(QPushButton, "btnVerLocales")
        self.salir = self.findChild(QPushButton, "btnExit")
        self.ventas = self.findChild(QPushButton, "btnVentas")
        self.logout = self.findChild(QPushButton, "btnLogout")
        self.minimizar = self.findChild(QPushButton, "btnMinimizar")

        #Eventos
        self.salir.setIcon(QIcon("assets/x-solid.svg"))
        self.minimizar.setIcon(QIcon("assets/minus-solid.svg"))
        self.crearUsuario.clicked.connect(self.mostrarCrearUsuarios)
        self.salir.clicked.connect(self.exitApp)
        self.minimizar.clicked.connect(self.showMinimized)

    def mostrarCrearUsuarios(self):
        try:
            self.agCrearUsuarios = AGCrearUsuarios()
            self.agCrearUsuarios.show()
        except Exception as ex:
            print(ex)

    def exitApp(self):
        mensaje = Pregunta("Question","Salir", "Está seguro de que desea cerrar sesión y salir de la aplicación?", "cerrarAplicacion")
        Ui_DialogQuestion(mensaje)