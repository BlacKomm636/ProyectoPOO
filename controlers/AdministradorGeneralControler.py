# Importa la clase base Usuario
from controlers.UsuarioControler import Usuario
from db.db_connection import *
import psycopg2

with open('db/db_connection.json', 'r') as file:
    config = json.load(file)

bd = Basedatos(
    config['DEFAULT']['DB_HOST'],
    config['DEFAULT']['DB_PORT'],
    config['DEFAULT']['DB_USER'],
    config['DEFAULT']['DB_PASSWORD'],
    config['DEFAULT']['DB_NAME'])

bd.conectar()

class AdministradorGeneral(Usuario):
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

    def crearUsuarioAdministradorGeneral(self, conexion):
        nombre = input("Nombre del usuario: ")
        apellido = input("Apellido del usuario: ")
        cedula = input("Cédula del usuario: ")
        local = input("Local del usuario: ")
        telefono = input("Teléfono del usuario: ")
        contrasena = input("Contraseña del usuario: ")
        rol = input("Rol del usuario: ")

        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuarios(nombre, apellido, cedula, local, telefono, contrasena, estado, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_usuario;"
                cursor.execute(consulta, (nombre, apellido, cedula, local, telefono, contrasena, self.estado, rol))
                self.id_usuario = cursor.fetchone()[0]
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al crear usuario", e)
            return False


    def leerUsuarios(self,conexion):
        try:
            with self.conexion.cursor() as cursor:
                consulta = "SELECT id_usuario, nombre, apellido, cedula, local, telefono, contrasena, estado, rol FROM usuarios;"
                cursor.execute(consulta)
                usuarios = cursor.fetchall()
                return usuarios
        except psycopg2.Error as e:
            print("Error al leer usuarios", e)
            return []

    def actualizarUsuario(self, id_usuario, nombre, apellido, cedula, local, telefono, contrasena, rol):
        try:
            with self.conexion.cursor() as cursor:
                consulta = "UPDATE usuarios SET nombre=%s, apellido=%s, cedula=%s, local=%s, telefono=%s, contrasena=%s, rol=%s WHERE id_usuario=%s;"
                cursor.execute(consulta, (nombre, apellido, cedula, local, telefono, contrasena, rol, id_usuario))
            self.conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al actualizar usuario", e)
            return False

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


