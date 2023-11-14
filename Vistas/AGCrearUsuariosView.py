from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QCheckBox, QComboBox

from controlers.MensajeControler import Ui_DialogMensaje
from controlers.UsuarioControler import UsuarioControler
from models.Respuesta import Respuesta
from models.Usuario import Usuario


class AGCrearUsuarios(QMainWindow):
    def __init__(self, parent=None):
        super(AGCrearUsuarios, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        uic.loadUi("Vistas/ui_files/Admi.G(crearusuarios).ui", self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        #Definición de componentes
        self.crearUsuario = self.findChild(QPushButton, "btnCrearUsuario")
        self.locales = self.findChild(QPushButton, "btnVerLocales")
        self.salir = self.findChild(QPushButton, "btnExit")
        self.ventas = self.findChild(QPushButton, "btnVentas")
        self.logout = self.findChild(QPushButton, "btnLogout")
        self.minimizar = self.findChild(QPushButton, "btnMinimizar")
        self.guardar = self.findChild(QPushButton, "btnGuardar")
        self.cancelar = self.findChild(QPushButton, "btnCancelar")

        #Usuario
        self.name = self.findChild(QLineEdit, "lineEditNombre")
        self.apellido = self.findChild(QLineEdit, "lineEditApellido")
        self.identificacion = self.findChild(QLineEdit, "lineEditIdentificacion")
        self.genero = self.findChild(QLineEdit, "lineEditGenero")
        self.telefono = self.findChild(QLineEdit, "lineEditTelefono")
        self.password = self.findChild(QLineEdit, "lineEditContrasena")
        self.confirmPass = self.findChild(QLineEdit, "lineEditConfirmPass")
        self.createLocalByUser = self.findChild(QCheckBox, "checkBoxCrearLocal")

        #Local
        self.nombreNegocio = self.findChild(QLineEdit, "lineEditNombreNegocio")
        self.numeroLocal = self.findChild(QLineEdit, "lineEditNumeroLocal")
        self.productos = self.findChild(QLineEdit, "lineEditProductos")

        self.roles = self.findChild(QComboBox, "comboBoxRol")

        #Eventos
        self.password.setEchoMode(QLineEdit.Password)
        self.confirmPass.setEchoMode(QLineEdit.Password)
        self.listaRoles = UsuarioControler.ObtenerRoles(self)
        self.roles.addItems(self.listaRoles)

        if self.createLocalByUser.isChecked():
            self.newRol = "Administrador Local"
        else:
            self.newRol = self.roles.currentText()

        self.guardar.clicked.connect(lambda: self.crearUsuarioPorAdministrador(
            self.name.text(),
            self.apellido.text(),
            self.identificacion.text(),
            self.nombreNegocio.text(),
            self.telefono.text(),
            self.password.text(),
            self.confirmPass.text(),
            self.newRol
            ))
    def crearUsuarioPorAdministrador(self, nombre, apellido, cedula, local, telefono, contrasena, confirmPass, rol):
        try:
            if contrasena == confirmPass:
                usuario:Usuario = {
                    "id_usuario": 0,
                    "nombre": nombre,
                    "apellido": apellido,
                    "cedula": cedula,
                    "local": local,
                    "telefono": telefono,
                    "contrasena": contrasena,
                    "rol": rol,
                    "estado": True
                }
                self.usuario = UsuarioControler.crearUsuario(self, usuario)
                if self.usuario:
                    mensaje = Respuesta("Success", "Exito!",
                                        "Usuario creado correctamente!")
                    Ui_DialogMensaje(mensaje)
                else:
                    mensaje = Respuesta("Error", "Error!",
                                        "Error al crear el usuario, revise la información suministrada.")
                    Ui_DialogMensaje(mensaje)
            else:
                mensaje = Respuesta("Error", "Error!", "La contraseña no coincide, revise los campos de contraseña y confirmar contraseña!")
                Ui_DialogMensaje(mensaje)

            self.hide()
        except Exception as ex:
            print(ex)