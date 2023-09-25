from basededatos import *
from Usuario import *
from AdministradorGeneral import *

conexion = Basedatos("localhost",5432,"postgres","kevomm636","ServidorPOO")
conexion.conectar()

# Crear una instancia de AdministradorGeneral en lugar de Usuario
admin_general = AdministradorGeneral(conexion.conectar())

# Llamar al método crearUsuarioAdministradorGeneral
admin_general.ejecutar()


#Falta crear la clase mesero, chef, factura