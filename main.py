from Mensaje import Ui_Dialog
from basededatos import *
from Usuario import *
import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLineEdit
from AdministradorGeneral import *
from models.Respuestas import Respuestas


class Home(QDialog):

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        uic.loadUi("Vistas/Bienvenido.ui", self)
        self.setWindowTitle("Home")
        self.findChild(QPushButton, 'BotonAdminGeneral').clicked.connect(self.abrir_administradorGeneral)



    def abrir_administradorGeneral(self):
        self.loginAdministradorGeneral = LoginAdministradorGeneral()
        self.loginAdministradorGeneral.show()
        self.hide()

class LoginAdministradorGeneral(QMainWindow):
    def __init__(self, parent=None):
        try:
            super(LoginAdministradorGeneral, self).__init__(parent)
            uic.loadUi("Vistas/loginAdminitradorGeneral.ui", self)
            self.setWindowTitle("Administrador General")
            self.findChild(QPushButton, 'pushButton_2').clicked.connect(lambda: self.AbrirAdministrador())

        except Exception as ex:
            print(ex)

    def AbrirAdministrador(self):
        self.user_name = self.findChild(QLineEdit, 'lineEdit').text()
        self.password = self.findChild(QLineEdit, 'lineEdit_2').text()
        usuarioAdmin = AdministradorGeneral.obtenerUsuarioAdministrador(self, self.user_name, self.password)
        if usuarioAdmin:
            uic.loadUi("Vistas/Admi.G(mostrarusuarios).ui", self)
            self.showMaximized()
        else:
            respuesta = Respuestas("error", "Error!", "Usuario y/o contraseña incorrectos!")
            Ui_Dialog(respuesta)
            self.findChild(QLineEdit, 'lineEdit').setText("")
            self.findChild(QLineEdit, 'lineEdit_2').setText("")


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