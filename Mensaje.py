from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtCore import *
from models.Respuestas import Respuestas

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

class Ui_Dialog(QDialog):
    def __init__(self, Mensaje, parent = None):
        super(Ui_Dialog, self).__init__(parent)
        self.setupUi(Mensaje)

    def setupUi(self, r:Respuestas):
        uic.loadUi("Vistas/mensajes.ui", self)
        self.setWindowTitle(r.titulo)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        label = self.findChild(QLabel, "txt_icon")
        if r.tipo == "error":
            pixmap = QPixmap("assets/check-mark-error.png")
        else:
            pixmap = QPixmap("assets/check-mark-icon.png")
        label.setPixmap(pixmap)
        self.findChild(QLabel, "txt_message").setText(r.mensaje)
        self.findChild(QPushButton, "btn_cerrar").clicked.connect(lambda: self.close())
        self.show()

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