import psycopg2
from psycopg2 import *

from controlers.AdministradorGeneralControler import bd
from models.Local import Local


class LocalControler():

    def crearLocal(self, local:Local):
        try:
            cursor = bd.conexion.cursor()
            # Consulta SQL para insertar un nuevo usuario sin proporcionar un valor para id_usuario
            consulta = ("INSERT INTO local (nombre, numero, productos, estado) "
                        "VALUES (%(nombre)s,"
                        " %(numero)s,"
                        " %(productos)s,"
                        " %(estado)s)")
            cursor.execute(consulta, local)
            valido = True
            bd.conexion.commit()  # Confirmamos la transacción
            print("local creado exitosamente")
            cursor.close()
            return valido  # Devolvemos True para indicar que la operación fue exitosa
        except psycopg2.Error as e:
            print("Error al crear local", e)
            return e  # Devolvemos False en caso de error

    def ObtenerLocales(self):
        try:
            cursor = bd.conexion.cursor()
            consulta = "SELECT id, nombre, numero, estado, productos FROM local ORDER BY id ASC"
            cursor.execute(consulta)
            locales = cursor.fetchall()
            if locales:
                nombres_locales = [tupla[1] for tupla in locales]
                return nombres_locales
            cursor.close()
        except psycopg2.Error as e:
            return e
    def obtenerLocales(self):
        try:
            cursor = bd.conexion.cursor()
            sql = "SELECT id, nombre, numero, estado, productos FROM local;"
            cursor.execute(sql)
            bd.conexion.commit()
            usuarios = cursor.fetchall()
            cursor.close()
            return usuarios
        except psycopg2.Error as e:
            print("Error al leer los datos de los locales", e)
            return e

    def obtenerLocalPorId(self, id):
        try:
            cursor = bd.conexion.cursor()
            sql = "SELECT id, nombre, numero, estado, productos FROM local WHERE id = %(id)s;"
            cursor.execute(sql, {"id": id})
            result = cursor.fetchone()
            cursor.close()
            return result
        except psycopg2.Error as e:
            print(f"Error al leer los datos del local con ID {id}", e)
            return e

    def editarLocales(self, local: Local):
        try:
            cursor = bd.conexion.cursor()
            sql = ("UPDATE local SET"
                   " nombre = %(nombre)s,"
                   " numero = %(numero)s,"
                   " estado = %(estado)s,"
                   " productos = %(productos)s"
                   " WHERE id = %(id)s;")
            cursor.execute(sql, {"nombre": local.nombre,
                                 "numero": local.numero,
                                 "estado": local.estado,
                                 "productos": local.productos,
                                 "id": local.id_local})
            bd.conexion.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print(f"Error al leer los datos de los locales con ID {id}", e)
            return e

    def eliminarLocal(self, id_local):
        try:
            cursor = bd.conexion.cursor()
            consulta = "DELETE FROM local WHERE id = %(id)s"
            cursor.execute(consulta, {"id": id_local})
            bd.conexion.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print("Error al eliminar los datos del local", e)
            return e

