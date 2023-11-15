from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout,QHBoxLayout, QLineEdit, QLabel, QTableWidget, QTableWidgetItem

from Vistas.AGCrearUsuariosView import AGCrearUsuarios
from Vistas.AGCrearLocalesView import AGCrearLocales
from controlers.QuestionControler import Ui_DialogQuestion
from controlers.UsuarioControler import UsuarioControler
from models.Pregunta import Pregunta
from models.Usuario import Usuario


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
        self.tableUsuarios.setColumnCount(7)
        self.tableUsuarios.setHorizontalHeaderLabels(('ID','Nombre', 'Apellido', 'Local', 'Teléfono', 'Rol','Acciones'))
        self.tableUsuarios.setColumnWidth(1, 150)
        self.tableUsuarios.setColumnWidth(2, 150)
        self.tableUsuarios.setColumnWidth(3, 150)
        self.tableUsuarios.setColumnWidth(4, 150)
        self.tableUsuarios.verticalHeader().setVisible(False)

        usuarios = UsuarioControler.leerDatos(self)
        for i in range(len(usuarios)):
            self.tableUsuarios.setRowHeight(i, 50)

            btnEditar = QPushButton(self)
            btnEliminar = QPushButton(self)

            btnEditar.setIcon(QIcon("assets/editar.png"))
            btnEliminar.setIcon(QIcon("assets/borrar.png"))

            for button in [btnEditar, btnEliminar]:
                button.setCursor(Qt.PointingHandCursor)
                button.setStyleSheet("border-radius:10px;padding:3px;width:64px;")
                button.setIconSize(QSize(30, 30))

            layout = QHBoxLayout()
            layout.addWidget(btnEditar)
            layout.addWidget(btnEliminar)

            cell_widget = QWidget()
            cell_widget.setLayout(layout)
            newCadena = [str(usuarios[i][0]), usuarios[i][1], usuarios[i][2], usuarios[i][4], usuarios[i][5], usuarios[i][8]]

            btnEditar.clicked.connect(lambda _, r=i: self.handleButtonClickEdit(r))
            btnEliminar.clicked.connect(lambda _, r=i: self.handleButtonClickDelete(r))

            for j in range(len(newCadena)):
                self.tableUsuarios.setItem(i, j, QTableWidgetItem(newCadena[j]))
                self.tableUsuarios.setCellWidget(i, 6, cell_widget)

    def mostrarCrearUsuarios(self):
        try:
            self.agCrearUsuarios = AGCrearUsuarios(None)
            self.agCrearUsuarios.show()
        except Exception as ex:
            print(ex)

    def mostrarCrearLocales(self):
        try:
            self.agCrearLocales = AGCrearLocales()
            self.agCrearLocales.show()
        except Exception as ex:
            print(ex)
    def handleButtonClickEdit(self, row):
        valorId = int(self.tableUsuarios.item(row, 0).text())
        usuario:Usuario = UsuarioControler.obtenerUsuarioPorId(self, valorId)
        self.modificarUsuario(usuario)

    def handleButtonClickDelete(self, row):
        valorId = int(self.tableUsuarios.item(row, 0).text())
        usuario:Usuario = UsuarioControler.obtenerUsuarioPorId(self, valorId)
        self.eliminarUsuario(usuario)

    def modificarUsuario(self, usuario:Usuario):
        try:
            self.agModificarUsuario = AGCrearUsuarios(usuario)
            self.agModificarUsuario.show()
        except Exception as ex:
            print(ex)

    def eliminarUsuario(self, usuario: Usuario):
        try:
            mensaje = Pregunta("Question", "Eliminar", f"Está seguro de que desea eliminar el registro: {usuario[3]}?",
                               "eliminarUsuario", usuario[0])
            Ui_DialogQuestion(mensaje)
        except Exception as ex:
            print(ex)


    def exitApp(self):
        mensaje = Pregunta("Question","Salir", "Está seguro de que desea cerrar sesión y salir de la aplicación?", "cerrarAplicacion", None)
        Ui_DialogQuestion(mensaje)