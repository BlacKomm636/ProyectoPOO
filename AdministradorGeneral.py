# Importa la clase base Usuario
from Usuario import *
from basededatos import *
import psycopg2
conexion = Basedatos("localhost",5432,"postgres","kevomm636","ServidorPOO")
c = conexion.conectar()

class AdministradorGeneral(Usuario):
    def __init__(self, conexion):
        super().__init__(conexion)
    
    def ejecutar(self):
        opcion = 0
        while opcion != 7:
            print("+----------------------------------+")
            print("|                                  |")
            print("|        ADMINISTRADOR GENERAL     |")
            print("|                                  |")
            print("+----------------------------------+")
            print("|                                  |")
            print("| 1. Crear Usuario                 |")
            print("| 2. Desactivar Usuario            |")
            print("| 3. Mostrar Usuarios              |")
            print("| 4. Crear Local                   |")
            print("| 5. Desactivar Local              |")
            print("| 6. Mostrar Locales               |")
            print("| 7. Salir                         |")
            print("|                                  |")
            print("+----------------------------------+")
            opcion = int(input("Ingrese la operación que desea realizar: "))
            if opcion == 1:
                self.crearUsuarioAdministradorGeneral(conexion.conectar())

            elif opcion == 2:
                self.desactivarUsuario(conexion.conectar())
            elif opcion ==3:
                self.leerUsuarios(conexion.conectar())
            elif opcion ==4:
                self.crearLocal()
            elif opcion ==5:
                self.desactivarLocal()
            elif opcion ==6:
                self.leerLocales()
            elif opcion ==7:
                print("Hasta luego")
                break

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


