
# Importa la clase base Usuario
from controlers.AdministradorGeneralControler import bd
from controlers.UsuarioControler import UsuarioControler
import psycopg2


class Mesero(UsuarioControler):
    def __init__(self, conexion):
        super()._init_(conexion)

    def obtenerMesero(self, usuario, contrasena):
        try:
            valido = False
            cursor = bd.conexion.cursor()
            sql = "SELECT id, nombre, user_name, password, is_active FROM cocinero;"
            cursor.execute(sql)
            mesero = cursor.fetchall()
            if mesero:
                for tupla in enumerate(mesero):
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
