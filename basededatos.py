import psycopg2
import json

class Basedatos():
    url = ""
    port = 5432
    user = ""
    password = ""
    database = ""


    def __init__(self, url, port, user, password, database):
        self.url = url
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None  # Agregamos una variable de instancia para la conexión

    def conectar(self):
        try:
            credenciales = {
                "database": self.database,
                "user": self.user,
                "password": self.password,
                "host": self.url,
                "port": self.port
            }
            self.conexion = psycopg2.connect(**credenciales)
            if self.conexion:
                print("Conexion exitosa a PostgreSQL")
        except psycopg2.Error as e:
            print("Ocurrió un error al conectar a PostgreSQL", e)
