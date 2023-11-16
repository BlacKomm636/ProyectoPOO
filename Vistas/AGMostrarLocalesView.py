from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout,QHBoxLayout, QLineEdit, QLabel, QTableWidget, QTableWidgetItem

from Vistas.AGCrearUsuariosView import AGCrearUsuarios
from Vistas.AGCrearLocalesView import AGCrearLocales
from controlers.LocalControler import LocalControler
from controlers.QuestionControler import Ui_DialogQuestion
from controlers.UsuarioControler import UsuarioControler
from models.Local import Local
from models.Pregunta import Pregunta
from models.Usuario import Usuario


class AGMostrarLocales(QMainWindow):

    def __init__(self, parent=None):
        super(AGMostrarLocales, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        uic.loadUi("Vistas/ui_files/Admi.G(verlocales).ui", self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        #Definir componentes
        self.crearUsuario = self.findChild(QPushButton, "btnCrearUsuario")
        self.locales = self.findChild(QPushButton, "btnVerLocales")
        self.salir = self.findChild(QPushButton, "btnExit")
        self.ventas = self.findChild(QPushButton, "btnVentas")
        self.logout = self.findChild(QPushButton, "btnLogout")
        self.minimizar = self.findChild(QPushButton, "btnMinimizar")
        self.crearLocales = self.findChild(QPushButton, "btnCrearLocales")

        self.tableLocales = self.findChild(QTableWidget, "tableWidgetLocal")
        self.actualizar = self.findChild(QPushButton, "btnRecargar")

        #Eventos
        self.salir.setIcon(QIcon("assets/x-solid.svg"))
        self.minimizar.setIcon(QIcon("assets/minus-solid.svg"))
        self.actualizar.setIcon(QIcon("assets/girar.png"))
        self.crearUsuario.clicked.connect(self.mostrarCrearUsuarios)
        self.salir.clicked.connect(self.exitApp)
        self.minimizar.clicked.connect(self.showMinimized)
        self.crearLocales.clicked.connect(self.mostrarCrearLocales)

        self.actualizarTabla()
        self.actualizar.clicked.connect(self.actualizarTabla)

    def mostrarCrearUsuarios(self):
        try:
            self.agCrearUsuarios = AGCrearUsuarios(None)
            self.agCrearUsuarios.show()
        except Exception as ex:
            print(ex)

    def mostrarCrearLocales(self):
        try:
            self.agCrearLocales = AGCrearLocales(None)
            self.agCrearLocales.show()
        except Exception as ex:
            print(ex)
    def handleButtonClickEdit(self, row):
        valorId = int(self.tableLocales.item(row, 0).text())
        local:Local = LocalControler.obtenerLocalPorId(self, valorId)
        self.modificarLocal(local)

    def handleButtonClickDelete(self, row):
        valorId = int(self.tableLocales.item(row, 0).text())
        local:Local = LocalControler.obtenerLocalPorId(self, valorId)
        self.eliminarLocal(local)

    def modificarLocal(self, local:Local):
        try:
            self.agModificarLocal = AGCrearLocales(local)
            self.agModificarLocal.show()
        except Exception as ex:
            print(ex)

    def eliminarLocal(self, local: Local):
        try:
            mensaje = Pregunta("Question", "Eliminar", f"Está seguro de que desea eliminar el registro: {local[1]}?",
                               "eliminarLocal", local[0])
            Ui_DialogQuestion(mensaje)
        except Exception as ex:
            print(ex)

    def actualizarTabla(self):
        self.tableLocales.setRowCount(0)
        self.tableLocales.setColumnCount(0)
        locales = LocalControler.obtenerLocales(self)
        self.tableLocales.setRowCount(10)
        self.tableLocales.setColumnCount(5)
        self.tableLocales.setHorizontalHeaderLabels(
            ('ID', 'Nombre', '# Local', 'Productos', 'Acciones'))
        self.tableLocales.setColumnWidth(1, 150)
        self.tableLocales.setColumnWidth(2, 150)
        self.tableLocales.setColumnWidth(3, 150)
        self.tableLocales.setColumnWidth(4, 150)
        self.tableLocales.verticalHeader().setVisible(False)
        for i in range(len(locales)):
            self.tableLocales.setRowHeight(i, 50)

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
            ultima_tupla = locales[i][-1]

            # Convertir la tupla en una cadena separada por comas
            cadena_resultante = ', '.join(map(str, ultima_tupla))

            newCadena = [str(locales[i][0]), locales[i][1], str(locales[i][2]), cadena_resultante]

            btnEditar.clicked.connect(lambda _, r=i: self.handleButtonClickEdit(r))
            btnEliminar.clicked.connect(lambda _, r=i: self.handleButtonClickDelete(r))

            for j in range(len(newCadena)):
                self.tableLocales.setItem(i, j, QTableWidgetItem(newCadena[j]))
                self.tableLocales.setCellWidget(i, 4, cell_widget)


    def exitApp(self):
        mensaje = Pregunta("Question","Salir", "Está seguro de que desea cerrar sesión y salir de la aplicación?", "cerrarAplicacion", None)
        Ui_DialogQuestion(mensaje)