from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtCore import *

from controlers.MensajeControler import Ui_DialogMensaje
from controlers.UsuarioControler import UsuarioControler
from models import Pregunta
from models.Respuesta import Respuesta

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogQuestion(QDialog):
    r: Pregunta
    def __init__(self, mensaje, parent = None):
        super(Ui_DialogQuestion, self).__init__(parent)
        self.setupUi(mensaje)

    def setupUi(self, r):
        uic.loadUi("Vistas/ui_files/question.ui", self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        label = self.findChild(QLabel, "txt_icon")
        pixmap = QPixmap("assets/Question_mark.png")
        label.setPixmap(pixmap)
        mensaje = self.findChild(QLabel, "txt_message")
        mensaje.setText(r.mensaje)
        mensaje.setWordWrap(True)
        if r.aprobar == "cerrarAplicacion":
            self.findChild(QPushButton, "btnAprobar").clicked.connect(lambda: self.cerrarAplicacion())
        elif r.aprobar == "eliminarUsuario":
            self.findChild(QPushButton, "btnAprobar").clicked.connect(lambda: self.eliminarUsuario(r.objeto))

        self.findChild(QPushButton, "btnRechazar").clicked.connect(lambda: self.close())
        self.show()

    def cerrarAplicacion(self):
        self.hide()
        QtWidgets.QApplication.quit()

    def eliminarUsuario(self, id):
        eliminado = UsuarioControler.eliminarUsuario(self, id)
        if eliminado:
            self.hide()
            mensaje = Respuesta("success", "Exito!",
                                "Usuario eliminado correctamente!")
            Ui_DialogMensaje(mensaje)

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

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Cerrar", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Prueba</span></p></body></html>", None))