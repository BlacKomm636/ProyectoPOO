class Pregunta():
    tipo = ""
    titulo = ""
    mensaje = ""
    aprobar = ""

    def __init__(self, tipo, titulo, mensaje, aprobar):
        self.tipo = tipo
        self.titulo = titulo
        self.mensaje = mensaje
        self.aprobar = aprobar