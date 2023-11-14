# Importa la clase base Usuario
from controlers.MensajeControler import Ui_DialogMensaje
from db.db_connection import *
import psycopg2

from models.Respuesta import Respuesta
from models.Usuario import Usuario

with open('db/db_connection.json', 'r') as file:
    config = json.load(file)

bd = Basedatos(
    config['DEFAULT']['DB_HOST'],
    config['DEFAULT']['DB_PORT'],
    config['DEFAULT']['DB_USER'],
    config['DEFAULT']['DB_PASSWORD'],
    config['DEFAULT']['DB_NAME'])

bd.conectar()

class AdministradorGeneral():
    def __init__(self, conexion):
        super().__init__(conexion)
    
    def obtenerUsuarioAdministrador(self, usuario, contrasena):
        try:
            valido = False
            cursor = bd.conexion.cursor()
            sql = "SELECT id, user_name, password, is_active FROM administrador_general;"
            cursor.execute(sql)
            administrador = cursor.fetchall()
            if administrador:
                for tupla in enumerate(administrador):
                    if not usuario in tupla[1]:
                        valido = False
                        respuesta = Respuesta("error", "Error!", "Usuario y/o contraseña incorrectos!")
                        Ui_DialogMensaje(respuesta)
                    elif not contrasena in tupla[1]:
                        valido = False
                        respuesta = Respuesta("error", "Error!", "Usuario y/o contraseña incorrectos!")
                        Ui_DialogMensaje(respuesta)
                    else:
                        valido = True
                        respuesta = Respuesta("success", "Éxito!", "Bienvenido " + tupla[1][1])

            cursor.close()
            return valido

        except psycopg2.Error as e:
            print("Error al leer usuarios", e)
            return []

    def actualizarUsuario(self, usuario:Usuario):
        try:
            valido = False
            cursor = bd.conexion.cursor()
            consulta = "UPDATE usuarios SET nombre=%s, apellido=%s, cedula=%s, local=%s, telefono=%s, contrasena=%s, rol=%s WHERE id_usuario=%s;"
            cursor.execute(consulta, (
                usuario.nombre,
                usuario.apellido,
                usuario.cedula,
                usuario.local,
                usuario.telefono,
                usuario.contrasena,
                usuario.rol,
                usuario.id_usuario))
            if consulta is None:
                valido = False
                print("Error actualizando el usuario")
            else:
                valido = True
                self.conexion.commit()
            return valido
        except psycopg2.Error as e:
            print("Error al actualizar usuario", e)
            return []

    def desactivarUsuario(self, id_usuario):
        try:
            with self.conexion.cursor() as cursor:
                consulta = "UPDATE usuarios SET estado=%s WHERE id_usuario=%s;"
                cursor.execute(consulta, (False, id_usuario))
            self.conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al desactivar usuario", e)
            return False

#nos falta el crud para locales


