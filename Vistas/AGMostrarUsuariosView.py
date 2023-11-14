from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QLabel, QTableWidget, QTableWidgetItem

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

        self.tableUsuarios = self.findChild(QTableWidget, "tableWidgetUsuarios")


        #Eventos
        self.salir.setIcon(QIcon("assets/x-solid.svg"))
        self.minimizar.setIcon(QIcon("assets/minus-solid.svg"))
        self.crearUsuario.clicked.connect(self.mostrarCrearUsuarios)
        self.salir.clicked.connect(self.exitApp)
        self.minimizar.clicked.connect(self.showMinimized)
        self.crearLocales.clicked.connect(self.mostrarCrearLocales)

        self.tableUsuarios.setRowCount(10)
        self.tableUsuarios.setColumnCount(6)
        self.tableUsuarios.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'Local', 'Teléfono', 'Rol','Acciones'))
        self.tableUsuarios.setColumnWidth(0,120)

        usuarios = UsuarioControler.leerDatos(self)
        for i in range(len(usuarios)):
            for j in range(len(usuarios[i])):
                print(usuarios[i][j])
                self.tableUsuarios.setItem(i, j, QTableWidgetItem(usuarios[i][j]))

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