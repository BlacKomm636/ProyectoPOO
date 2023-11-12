from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QPushButton

from controlers.QuestionControler import Ui_DialogQuestion
from models.Pregunta import Pregunta


class Home(QDialog):
    def setupUI(self):
        uic.loadUi("Vistas/ui_files/Bienvenido.ui", self)
        # Configura las flags para eliminar el encabezado y los botones de cierre
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        # Definición de componentes
        self.administradorGeneral = self.findChild(QPushButton, 'btn_adminGeneral')
        self.logo = self.findChild(QPushButton, "btn_logo")
        self.cocinero = self.findChild(QPushButton, "btn_cocinero")
        self.administradorLocal = self.findChild(QPushButton, 'btn_adminLocal')
        self.mesero = self.findChild(QPushButton, 'btn_mesero')
        self.cerrar = self.findChild(QPushButton, 'btn_cerrar')

        # Carga de imágenes y métodos
        self.administradorGeneral.setIcon(QIcon("assets/imagenAdministradorGeneral.png"))
        self.administradorGeneral.clicked.connect(self.abrir_administradorGeneral)

        self.logo.setIcon(QIcon("assets/logo.png"))

        self.mesero.setIcon(QIcon("assets/mesero.png"))
        self.mesero.clicked.connect(self.abrir_mesero)

        self.administradorLocal.setIcon(QIcon("assets/administradorlocal.png"))
        self.administradorLocal.clicked.connect(self.abrir_administradorLocal)

        self.cocinero.setIcon(QIcon("assets/cocinero.png"))
        self.cocinero.clicked.connect(self.abrir_cocinero)

        self.cerrar.setIcon(QIcon("assets/x-solid.svg"))
        self.cerrar.clicked.connect(self.cerrarAplicacion)