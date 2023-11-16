from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QCheckBox, QComboBox, QListWidget

from controlers.MensajeControler import Ui_DialogMensaje
from controlers.QuestionControler import Ui_DialogQuestion
from controlers.UsuarioControler import UsuarioControler
from models.Respuesta import Respuesta
from models.Usuario import Usuario
from models.Local import Local
from controlers.LocalControler import LocalControler
from models.Pregunta import Pregunta

class AGCrearLocales(QMainWindow):
    local:Local
    def __init__(self,local, parent=None):
        super(AGCrearLocales, self).__init__(parent)
        self.local = local
        self.setupUI()
    def setupUI(self):
        uic.loadUi("Vistas/ui_files/Admi.G(crearlocales).ui",self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        self.CrearLocales=self.findChild(QPushButton,"btnCrearLocales")
        self.CrearUsuarios=self.findChild(QPushButton,"btnCrearUsuario")
        self.locales=self.findChild(QPushButton, "btnVerLocales")
        self.salir = self.findChild(QPushButton, "btnExit")
        self.ventas = self.findChild(QPushButton, "btnVentas")
        self.logout = self.findChild(QPushButton, "btnLogout")
        self.minimizar = self.findChild(QPushButton, "btnMin")
        self.guardar = self.findChild(QPushButton, "btnGuardar")
        self.cancelar = self.findChild(QPushButton, "btnCancelar")

        #local
        self.nombreNegocio=self.findChild(QLineEdit,"lineEditNombreNegocio")
        self.numeroLocal = self.findChild(QLineEdit, "lineEditNumeroLocal")

        #productos

        self.listadeProductos=self.findChild(QListWidget, "listWidgetProductos")
        self.especificarProducto=self.findChild(QLineEdit, "lineEditProducto")
        self.agregar=self.findChild(QPushButton, "btnAgregar")

        #Eventos
        if self.local is not None:
            self.nombreNegocio.setText(self.local[1])
            self.numeroLocal.setText(str(self.local[2]))
            self.listadeProductos.addItems(self.local[4])

            self.guardar.clicked.connect(lambda: self.modificarLocalPorAdministrador(self.nombreNegocio.text(), self.numeroLocal.text(), self.listadeProductos, self.local[0]))
        else:
            self.guardar.clicked.connect(
                lambda: self.agregarLocalConProductos(self.nombreNegocio.text(), self.numeroLocal.text(),
                                                      self.listadeProductos, True))

        self.agregar.clicked.connect(self.localControler)

        self.cancelar.clicked.connect(self.hide)
        self.salir.clicked.connect(self.exitApp)

    def localControler(self):

       comida = self.especificarProducto.text()
       self.listadeProductos.addItem(comida)
       self.especificarProducto.setText('')
       self.especificarProducto.setFocus()

    def agregarLocalConProductos(self, nombre, numero, productos, estado):
        elements = []
        for i in range(productos.count()):
            item = productos.item(i)
            elements.append(item.text())
        if nombre != None and numero != None:
            local:Local = {
                "id_local": 0,
                "nombre": nombre,
                "numero": numero,
                "productos": elements,
                "estado": estado
            }

            self.localCreado = LocalControler.crearLocal(self, local)
            if self.localCreado:
                mensaje = Respuesta("Success", "Exito!",
                                    "Local creado correctamente!")
                Ui_DialogMensaje(mensaje)
                self.hide()
            else:
                mensaje = Respuesta("Error", "Error!",
                                    "Error al crear el local, revise la información suministrada.")
                Ui_DialogMensaje(mensaje)

    def modificarLocalPorAdministrador(self, nombre, numero, productos, id):
        try:
            if nombre == "" or numero == "":
                mensaje = Respuesta("error", "Error!",
                                    "Faltan campos obligatorios")
                Ui_DialogMensaje(mensaje)
            else:
                elements = []
                for i in range(productos.count()):
                    item = productos.item(i)
                    elements.append(item.text())
                local = Local(id, nombre, numero, elements, True)
                self.newLocal = LocalControler.editarLocales(self, local)
                if self.newLocal:
                    mensaje = Respuesta("success", "Exito!",
                                            "local modificado correctamente!")
                    Ui_DialogMensaje(mensaje)
                    self.hide()
                else:
                    mensaje = Respuesta("error", "Error!",
                                            "Error al modificar el local, revise la información suministrada.")
                    Ui_DialogMensaje(mensaje)
        except Exception as ex:
            print(ex)

    def exitApp(self):
        mensaje = Pregunta("Question","Salir", "Está seguro de que desea cerrar sesión y salir de la aplicación?", "cerrarAplicacion")
        Ui_DialogQuestion(mensaje)











