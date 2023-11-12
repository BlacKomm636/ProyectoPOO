  # Importa la clase base Usuario
from controlers.AdministradorGeneralControler import bd
from controlers.UsuarioControler import UsuarioControler
from db.db_connection import Basedatos
import psycopg2

class AdministradorLocal(UsuarioControler):
    def __init__(self, conexion):
        super()._init_(conexion)

    def obtenerUsuarioAdministrador(self, usuario, contrasena):
        try:
            valido = False
            cursor = bd.conexion.cursor()
            sql = "SELECT id, user_name, password, is_active FROM administrador_local;"
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

    def crearChef(self):
        nombre = input("Nombre del chef: ")
        apellido = input("Apellido del chef: ")
        especialidad = input("Especialidad del chef: ")
        
        try:
            with self.conexion.cursor() as cursor:
                consulta = "INSERT INTO chefs(nombre, apellido, especialidad) VALUES (%s, %s, %s);"
                cursor.execute(consulta, (nombre, apellido, especialidad))
            self.conexion.commit()
            print("Chef creado exitosamente")
        except psycopg2.Error as e:
            print("Error al crear chef", e)

    def leerChefs(self):
        try:
            with self.conexion.cursor() as cursor:
                consulta = "SELECT id_chef, nombre, apellido, especialidad FROM chefs;"
                cursor.execute(consulta)
                chefs = cursor.fetchall()
                
                if chefs:
                    print("Lista de Chefs:")
                    for chef in chefs:
                        print(f"ID: {chef[0]}, Nombre: {chef[1]}, Apellido: {chef[2]}, Especialidad: {chef[3]}")
                else:
                    print("No hay chefs registrados.")
        except psycopg2.Error as e:
            print("Error al leer chefs", e)

#Nos falta hacer el crud de productos
#Nos falta desactivar y actualizar chefs
#nos falta ver el registro de ventas










    def verRegistroVentas(self):
        # Implementa aquí la lógica para ver el registro de ventas del día
        pass

