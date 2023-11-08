class Usuario():
    id_usuario = None
    nombre = ""
    apellido = ""
    cedula = ""
    local = ""
    telefono = ""
    contrasena = ""
    rol = ""
    estado = True

    def __init__(self, id, nombre, apellido, cedula, local, telefono, contrasena, rol, estado):
        self.id_usuario = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.local = local
        self.telefono = telefono
        self.contrasena = contrasena
        self.rol = rol
        self.estado = estado
