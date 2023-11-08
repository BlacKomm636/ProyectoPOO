import psycopg2
from psycopg2 import *

def menuPrincipalLogin():
    print("+----------------------------------+")
    print("|                                  |")
    print("|               Login              |")
    print("|                                  |")
    print("+----------------------------------+")
    print("|   Seleccione su rol:             |")
    print("| 1. Administrador general         |")
    print("| 2. Administrador de local        |")
    print("| 3. Mesero                        |")
    print("| 4. Cocinero                      |")        
    print("| 5. crear pedido                  |")                         
    print("+----------------------------------+")



class Usuario():
    def __init__(self, conexion):
        self.conexion = conexion
        self.id_usuario = None
        self.nombre = ""
        self.apellido = ""
        self.cedula = ""
        self.local = ""
        self.telefono = ""
        self.contrasena = ""
        self.rol = ""
        self.estado = True  # Por defecto, un usuario nuevo está activo

    def imprimirNombre(self):
        print("el nombre del usuario es: ", self.nombre)

    def crearUsuario(self, nombre,apellido, cedula, local, telefono, contrasena, rol):
        try:
            with self.conexion.cursor() as cursor:
                # Consulta SQL para insertar un nuevo usuario sin proporcionar un valor para id_usuario
                consulta = "INSERT INTO usuarios(nombre, apellido, cedula, local, telefono, contrasena, estado, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_usuario;"
                cursor.execute(consulta, (nombre, apellido, cedula, local, telefono, contrasena, self.estado, rol))
                self.id_usuario = cursor.fetchone()[0]  # Obtenemos el id_usuario generado
            self.conexion.commit()  # Confirmamos la transacción
            print("Usuario creado exitosamente")
            return True  # Devolvemos True para indicar que la operación fue exitosa
        except psycopg2.Error as e:
            print("Error al crear usuario", e)
            return False  # Devolvemos False en caso de error

    def leerDatos(self):
        try:
            with self.conexion.cursor() as cursor:
                leer = "SELECT nombre, apellido, cedula, id_usuario , local, telefono, contrasena, estado, rol  FROM usuarios;"
                cursor.execute(leer)
                leerUsuario = cursor.fetchall()
                return leerUsuario
        except psycopg2.Error as e:
            print("Error al leer los datos del usuario", e)
            return None


    def Login(self, documento, password):
        try:
            with self.conexion.cursor() as cursor:
                consulta = "SELECT u.id_usuario, u.apellido, u.cedula, u.contrasena, u.estado, u.rol, u.telefono, u.nombre " \
                            "FROM Usuarios u " \
                            "WHERE u.cedula = %s;"
                cursor.execute(consulta, (documento,))
                usuario = cursor.fetchone()

                if usuario:
                    print(usuario)
                else:
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

