from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QCheckBox, QComboBox, QListWidget

from controlers.MensajeControler import Ui_DialogMensaje
from controlers.UsuarioControler import UsuarioControler
from models.Respuesta import Respuesta
from models.Usuario import Usuario

class AGCrearLocales(QMainWindow):
    def __init__(self,parent=None):
        super(AGCrearLocales, self).__init__(parent)
        self.setupUI()
    def setupIU(self):
        uic.loadUi("Vistas/iu_files/Admi.G(crearlocales).iu",self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        self.CrearLocales=self.findChild(QPushButton,"btnCrearLocales_6")
        self.CrearUsuarios=self.findChild(QPushButton,"btnCrearUsuario")
        self.locales=self.findChild(QPushButton, "btnVerLocales_3")
        self.salir = self.findChild(QPushButton, "btnExit")
        self.ventas = self.findChild(QPushButton, "btnVentas")
        self.logout = self.findChild(QPushButton, "btnLogout")
        self.minimizar = self.findChild(QPushButton, "btnMin")
        self.guardar = self.findChild(QPushButton, "btnGuardar")
        self.cancelar = self.findChild(QPushButton, "btnCancelar")

        #local
        self.nombreNegocio=self.findChild(QLineEdit,"lineEditNombreNegocio")
        self.numeroLocal = self.findChild(QLineEdit, "lineEditNombreNegocio")

        #productos

        self.ListadeProductos=self.findChild(QListWidget, "listWidgetProductos")
        self.EspecificarProducto=self.findChild(QLineEdit, "lineEditProducto")
        self.Agregar=self.findChild(QPushButton, "Agregar")

        #Eventos
    def LocalControler(self):

       #Lo que indica el video
       comida=self.iu.txt_comida.text()
       self.ui.lst_comida.addItem(comida)
       self.iu.txt_comida.setText('')
       self.iu.txt_comida.setFocus()









