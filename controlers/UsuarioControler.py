import psycopg2
from psycopg2 import *

from controlers.AdministradorGeneralControler import bd
from models.Usuario import Usuario


class UsuarioControler():

    def crearUsuario(self, usuario:Usuario):
        try:
            cursor = bd.conexion.cursor()
            # Consulta SQL para insertar un nuevo usuario sin proporcionar un valor para id_usuario
            consulta = ("INSERT INTO usuarios (nombre, apellido, cedula, local, telefono, contrasena, estado, rol) "
                        "VALUES (%(nombre)s,"
                        " %(apellido)s,"
                        " %(cedula)s,"
                        " %(local)s,"
                        " %(telefono)s,"
                        " %(contrasena)s,"
                        " %(estado)s,"
                        " %(rol)s)")
            cursor.execute(consulta, usuario)
            valido = True
            bd.conexion.commit()  # Confirmamos la transacción
            print("Usuario creado exitosamente")
            cursor.close()
            return valido  # Devolvemos True para indicar que la operación fue exitosa
        except psycopg2.Error as e:
            print("Error al crear usuario", e)
            return e  # Devolvemos False en caso de error

    def ObtenerRoles(self):
        try:
            cursor = bd.conexion.cursor()
            consulta = "SELECT id, nombre_rol, estado FROM roles ORDER BY id ASC"
            cursor.execute(consulta)
            roles = cursor.fetchall()
            if roles:
                nombres_roles = [tupla[1] for tupla in roles]
                return nombres_roles
            cursor.close()
        except psycopg2.Error as e:
            return e
    def leerDatos(self):
        try:
            cursor = bd.conexion.cursor()
            sql = "SELECT id, nombre, apellido, cedula, local, telefono, contrasena, estado, rol  FROM usuarios;"
            cursor.execute(sql)
            bd.conexion.commit()
            usuarios = cursor.fetchall()
            cursor.close()
            return usuarios
        except psycopg2.Error as e:
            print("Error al leer los datos del usuario", e)
            return e

    def obtenerUsuarioPorId(self, id):
        try:
            cursor = bd.conexion.cursor()
            sql = "SELECT id, nombre, apellido, cedula, local, telefono, contrasena, estado, rol  FROM usuarios WHERE id = %(id)s;"
            cursor.execute(sql, {"id": id})
            result = cursor.fetchone()
            cursor.close()
            return result
        except psycopg2.Error as e:
            print(f"Error al leer los datos del usuario con ID {id}", e)
            return e

    def editarUsuario(self, usuario:Usuario):
        try:
            cursor = bd.conexion.cursor()
            sql = ("UPDATE usuarios SET"
                   " nombre = %(nombre)s,"
                   " apellido = %(apellido)s,"
                   " cedula = %(cedula)s,"
                   " local = %(local)s,"
                   " telefono = %(telefono)s,"
                   " contrasena = %(contrasena)s,"
                   " estado = %(estado)s,"
                   " rol = %(rol)s "
                   "WHERE id = %(id)s;")
            cursor.execute(sql, {"nombre": usuario.nombre,
                                 "apellido": usuario.apellido,
                                 "cedula": usuario.cedula,
                                 "local": usuario.local,
                                 "telefono": usuario.telefono,
                                 "contrasena": usuario.contrasena,
                                 "estado": usuario.estado,
                                 "rol": usuario.rol,
                                 "id": usuario.id_usuario})
            bd.conexion.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print(f"Error al leer los datos del usuario con ID {id}", e)
            return e


    def eliminarUsuario(self, id_usuario):
        try:
            cursor = bd.conexion.cursor()
            consulta = "DELETE FROM usuarios WHERE id = %(id)s"
            cursor.execute(consulta, {"id": id_usuario})
            bd.conexion.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print("Error al eliminar los datos del usuario", e)
            return e
