from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from Vistas.AdministradorGeneralView import LoginAdminGeneral
from Vistas.AdministradorLocalView import LoginAdminLocal

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton

from Vistas.CocineroView import LoginCocinero
from Vistas.HomeView import Home
from Vistas.MeseroView import LoginMesero
from controlers.QuestionControler import Ui_DialogQuestion
from models.Pregunta import Pregunta


class Main(QDialog):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        Home.setupUI(self)
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
        except Exception as ex:
            print(ex)

    def abrir_administradorLocal(self):
        try:
            self.loginAdministradorLocal = LoginAdminLocal()
            self.loginAdministradorLocal.show()
        except Exception as ex:
            print(ex)

    def abrir_mesero(self):
        try:
            self.loginMesero = LoginMesero()
            self.loginMesero.show()
        except Exception as ex:
            print(ex)

    def cerrarAplicacion(self):
        mensaje = Pregunta("question", "Seguro?", "está seguro que desea cerrar la aplicación?", "cerrarAplicacion")
        Ui_DialogQuestion(mensaje)
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
    ventana = Main()
    ventana.show()
    sys.exit(app.exec_())



# Crear una instancia de AdministradorGeneral en lugar de Usuario
#admin_general = AdministradorGeneral(conexion.conectar())

# Llamar al método crearUsuarioAdministradorGeneral
#admin_general.ejecutar()


#Falta crear la clase mesero, chef, factura