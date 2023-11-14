class Local():
    id_local = None
    nombre = ""
    numero = ""
    productos = ""
    estado = True

    def __init__(self, id_local, nombre, numero, productos, estado):
        self.id_local = id_local
        self.nombre = nombre
        self.numero = numero
        self.productos = productos
        self.estado = estado