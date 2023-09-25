from Usuario import Usuario  # Importa la clase base Usuario
from basededatos import Basedatos
import psycopg2

class AdministradorLocal(Usuario):
    def __init__(self, conexion):
        super()._init_(conexion)

    def ejecutar(self):
        opcion = 0
        while opcion != 4:
            print("+----------------------------------+")
            print("|                                  |")
            print("|       ADMINISTRADOR LOCAL        |")
            print("|                                  |")
            print("+----------------------------------+")
            print("|                                  |")
            print("| 1. CRUD Menú/Productos           |")
            print("| 2. CRUD Chef                     |")
            print("| 3. Ver Registro de Ventas        |")
            print("| 4. Salir                         |")
            print("|                                  |")
            print("+----------------------------------+")
            opcion = int(input("Ingrese la operación que desea realizar: "))
            if opcion == 1:
                self.crudMenuProductos()
            elif opcion == 2:
                self.crudChef()
            elif opcion == 3:
                self.verRegistroVentas()
            elif opcion == 4:
                print("¡Hasta luego!")
                break

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

if _name_ == "_main_":
    conexion = Basedatos("localhost", 5432, "postgres", "kevomm636", "ServidorPOO")
    c = conexion.conectar()
    
    # Crear una instancia de AdministradorLocal en lugar de Usuario
    admin_local = AdministradorLocal(c)
    
    # Llamar al método ejecutar
    admin_local.ejecutar()