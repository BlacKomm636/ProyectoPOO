from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QLabel

from Vistas.AGCrearUsuariosView import AGCrearUsuarios
from Vistas.AGCrearLocalesView import AGCrearLocales
from controlers.QuestionControler import Ui_DialogQuestion
from controlers.UsuarioControler import UsuarioControler
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
        self.crearLocales = self.findChild(QPushButton, "btnCrearLocales")

        self.component = self.findChild(QWidget, "wUsers")
        self.layout = self.findChild(QVBoxLayout, "verticalLayoutUsers")

        self.nombre = self.findChild(QLabel, "labelNombre")
        self.id = self.findChild(QLabel, "labelId")
        self.local = self.findChild(QLabel, "labelLocal")
        self.rol = self.findChild(QLabel, "labelRol")


        #Eventos
        self.salir.setIcon(QIcon("assets/x-solid.svg"))
        self.minimizar.setIcon(QIcon("assets/minus-solid.svg"))
        self.crearUsuario.clicked.connect(self.mostrarCrearUsuarios)
        self.salir.clicked.connect(self.exitApp)
        self.minimizar.clicked.connect(self.showMinimized)
        self.crearLocales.clicked.connect(self.mostrarCrearLocales)


        usuarios = UsuarioControler.leerDatos(self)
        #for obj in usuarios:
            #self.layout.addWidget(self.component)
            #self.nombre.setText(obj.nombre)
            #self.id.setText(obj.id)
            #self.local.setText(obj.local)
            #self.rol.setText(obj.rol)
        #self.component.setLayout(self.layout)
        print(usuarios)

    def mostrarCrearUsuarios(self):
        try:
            self.agCrearUsuarios = AGCrearUsuarios()
            self.agCrearUsuarios.show()
        except Exception as ex:
            print(ex)

    def mostrarCrearLocales(self):
        try:
            self.agCrearLocales = AGCrearLocales()
            self.agCrearLocales.show()
        except Exception as ex:
            print(ex)

    def exitApp(self):
        mensaje = Pregunta("Question","Salir", "Está seguro de que desea cerrar sesión y salir de la aplicación?", "cerrarAplicacion")
        Ui_DialogQuestion(mensaje)