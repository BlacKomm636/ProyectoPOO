from basededatos import *
from Usuario import *
import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLineEdit
from AdministradorGeneral import *

conexion = Basedatos("localhost",5432,"postgres","root","ServidorPOO")
conexion.conectar()

class Home(QDialog):

    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi("Vistas/Bienvenido.ui", self)
        self.findChild(QPushButton, 'BotonAdminGeneral').clicked.connect(self.abrir_administradorGeneral)

    def abrir_administradorGeneral(self):
        self.loginAdministradorGeneral = LoginAdministradorGeneral()
        self.loginAdministradorGeneral.show()
        self.hide()

class LoginAdministradorGeneral(QMainWindow):
    def __init__(self, parent=None):
        try:
            super(LoginAdministradorGeneral, self).__init__(parent)
            self.setWindowTitle("Administrador General")
            uic.loadUi("Vistas/loginAdminitradorGeneral.ui", self)
            self.user_name = self.findChild(QLineEdit, 'lineEdit')
            self.password = self.findChild(QLineEdit, 'lineEdit_2')
            self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.AbrirAdministrador)

        except Exception as ex:
            print(ex)

    def AbrirAdministrador(self):
        usuarioAdmin = AdministradorGeneral.obtenerUsuarioAdministrador(self)
        return usuarioAdmin


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Home()
    ventana.show()
    sys.exit(app.exec_())

# Crear una instancia de AdministradorGeneral en lugar de Usuario
#admin_general = AdministradorGeneral(conexion.conectar())

# Llamar al método crearUsuarioAdministradorGeneral
#admin_general.ejecutar()


#Falta crear la clase mesero, chef, factura