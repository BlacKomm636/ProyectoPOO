from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

# Importa la clase base Usuario
from controlers.AdministradorGeneralControler import bd
from controlers.UsuarioControler import UsuarioControler
import psycopg2


class Cocinero(UsuarioControler):
    def __init__(self, conexion):
        super()._init_(conexion)

    def obtenerCocinero(self, usuario, contrasena):
        try:
            valido = False
            cursor = bd.conexion.cursor()
            sql = "SELECT id, nombre, user_name, password, is_active FROM cocinero;"
            cursor.execute(sql)
            cocinero = cursor.fetchall()
            if cocinero:
                for tupla in enumerate(cocinero):
                    if not usuario in tupla[1]:
                        valido = False
                        print("usuario incorrecto")
                    elif not contrasena in tupla[1]:
                        valido = False
                        print("contraseña incorrecta")
                    else:
                        valido = True
                        print("correcto!")

            return valido

        except psycopg2.Error as e:
            print("Error al leer usuarios", e)
            return []
