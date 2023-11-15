from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QCheckBox, QComboBox

from controlers.MensajeControler import Ui_DialogMensaje
from controlers.QuestionControler import Ui_DialogQuestion
from controlers.UsuarioControler import UsuarioControler
from controlers.LocalControler import LocalControler
from models.Respuesta import Respuesta
from models.Usuario import Usuario
from models.Pregunta import Pregunta


class AGCrearUsuarios(QMainWindow):
    usuario: Usuario = None
    def __init__(self, usuario:Usuario, parent=None):
        super(AGCrearUsuarios, self).__init__(parent)
        self.usuario = usuario
        print(usuario)
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
        self.volver = self.findChild(QPushButton, "btnBack")
        self.mostrarUsuarios = self.findChild(QPushButton, "btnMostrarUsuarios")

        #Usuario
        self.name = self.findChild(QLineEdit, "lineEditNombre")
        self.apellido = self.findChild(QLineEdit, "lineEditApellido")
        self.identificacion = self.findChild(QLineEdit, "lineEditIdentificacion")
        self.telefono = self.findChild(QLineEdit, "lineEditTelefono")
        self.password = self.findChild(QLineEdit, "lineEditContrasena")
        self.confirmPass = self.findChild(QLineEdit, "lineEditConfirmPass")

        self.roles = self.findChild(QComboBox, "comboBoxRol")
        self.local = self.findChild(QComboBox, "comboBoxLocal")

        #Eventos
        if self.usuario is not None:
            self.name.setText(self.usuario[1])
            self.apellido.setText(self.usuario[2])
            self.identificacion.setText(self.usuario[3])
            self.telefono.setText(self.usuario[5])


        self.password.setEchoMode(QLineEdit.Password)
        self.confirmPass.setEchoMode(QLineEdit.Password)
        self.listaRoles = UsuarioControler.ObtenerRoles(self)
        self.listaLocales = LocalControler.ObtenerLocales(self)
        self.roles.addItems(self.listaRoles)
        self.local.addItems(self.listaLocales)

        self.volver.clicked.connect(self.hide)
        self.cancelar.clicked.connect(self.hide)
        self.salir.clicked.connect(self.exitApp)
        self.mostrarUsuarios.clicked.connect(self.hide)

        if self.usuario is None:

            self.guardar.clicked.connect(lambda: self.crearUsuarioPorAdministrador(
                self.name.text(),
                self.apellido.text(),
                self.identificacion.text(),
                self.local.currentText(),
                self.telefono.text(),
                self.password.text(),
                self.confirmPass.text(),
                self.roles.currentText()
                ))
        else:
            self.guardar.clicked.connect(lambda: self.modificarUsuarioPorAdministrador(
                self.name.text(),
                self.apellido.text(),
                self.identificacion.text(),
                self.local.currentText(),
                self.telefono.text(),
                self.password.text(),
                self.confirmPass.text(),
                self.roles.currentText(),
                self.usuario[0]
            ))
    def crearUsuarioPorAdministrador(self, nombre, apellido, cedula, local, telefono, contrasena, confirmPass, rol):
        try:
            if nombre == "" or cedula == "":
                mensaje = Respuesta("error", "Error!",
                                    "Faltan campos obligatorios")
                Ui_DialogMensaje(mensaje)
            else:
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
                        self.hide()
                    else:
                        mensaje = Respuesta("Error", "Error!",
                                            "Error al crear el usuario, revise la información suministrada.")
                        Ui_DialogMensaje(mensaje)
                else:
                    mensaje = Respuesta("Error", "Error!", "La contraseña no coincide, revise los campos de contraseña y confirmar contraseña!")
                    Ui_DialogMensaje(mensaje)
        except Exception as ex:
            print(ex)
    def modificarUsuarioPorAdministrador(self, nombre, apellido, cedula, local, telefono, contrasena, confirmPass, rol, id):
        try:
            if nombre == "" or cedula == "":
                mensaje = Respuesta("error", "Error!",
                                    "Faltan campos obligatorios")
                Ui_DialogMensaje(mensaje)
            else:
                if contrasena == confirmPass:
                    usuario = Usuario(id, nombre, apellido, cedula, local, telefono, contrasena, rol, True)
                    self.usuario = UsuarioControler.editarUsuario(self, usuario)
                    if self.usuario:
                        mensaje = Respuesta("success", "Exito!",
                                            "Usuario modificado correctamente!")
                        Ui_DialogMensaje(mensaje)
                        self.hide()
                    else:
                        mensaje = Respuesta("error", "Error!",
                                            "Error al modificar el usuario, revise la información suministrada.")
                        Ui_DialogMensaje(mensaje)
                else:
                    mensaje = Respuesta("error", "Error!",
                                        "La contraseña no coincide, revise los campos de contraseña y confirmar contraseña!")
                    Ui_DialogMensaje(mensaje)
        except Exception as ex:
            print(ex)
    def exitApp(self):
        mensaje = Pregunta("Question","Salir", "Está seguro de que desea cerrar sesión y salir de la aplicación?", "cerrarAplicacion", None)
        Ui_DialogQuestion(mensaje)