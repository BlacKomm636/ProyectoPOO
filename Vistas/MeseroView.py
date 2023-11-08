from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton


class LoginMesero(QMainWindow):
    def __init__(self, parent=None):
        super(LoginMesero, self).__init__(parent)
        self.setupUI()
    def setupUI(self):
        uic.loadUi("Vistas/loginMesero.ui", self)
        self.setWindowTitle("Mesero")

        # Definición de componentes


        # Carga de iconos y métodos

    #def connectAdministradorLocal(self, user, password):
        #usuarioAdmin = AdministradorLocal.obtenerUsuarioAdministrador(self, user, password)
        #if usuarioAdmin:
            #uic.loadUi("Vistas/Admi.G(mostrarusuarios).ui", self)
            #self.showMaximized()
        #else:
            #respuesta = Respuestas("error", "Error!", "Usuario y/o contraseña incorrectos!")
            #Ui_Dialog(respuesta)
            #self.findChild(QLineEdit, 'lineEdit').setText("")
            #self.findChild(QLineEdit, 'lineEdit_2').setText("")