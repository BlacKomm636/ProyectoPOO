from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from Vistas.AdministradorGeneralView import LoginAdminGeneral
from Vistas.AdministradorLocalView import LoginAdminLocal

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton

from Vistas.CocineroView import LoginCocinero
from Vistas.MeseroView import LoginMesero
from models.Respuesta import Respuesta


class Home(QDialog):

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        uic.loadUi("Vistas/Bienvenido.ui", self)
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
    def abrir_administradorGeneral(self):
        try:
            self.loginAdministradorGeneral = LoginAdminGeneral()
            self.loginAdministradorGeneral.show()
        except Exception as ex:
            print(ex)

    def abrir_cocinero(self):
        try:
            self.loginCocinero = LoginCocinero()
            self.loginCocinero.show()
            self.hide()
        except Exception as ex:
            print(ex)

    def abrir_administradorLocal(self):
        try:
            self.loginAdministradorLocal = LoginAdminLocal()
            self.loginAdministradorLocal.show()
            self.hide()
        except Exception as ex:
            print(ex)

    def abrir_mesero(self):
        try:
            self.loginMesero = LoginMesero()
            self.loginMesero.show()
            self.hide()
        except Exception as ex:
            print(ex)

    def cerrarAplicacion(self):
        mensaje = Respuesta("question", "Seguro?", "está seguro que desea cerrar la aplicación?")
        self.close()

    # Mover ventana
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.globalPos() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

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