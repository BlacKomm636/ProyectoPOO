class Pregunta():
    tipo = ""
    titulo = ""
    mensaje = ""
    aprobar = ""
    objeto = ""

    def __init__(self, tipo, titulo, mensaje, aprobar, objeto):
        self.tipo = tipo
        self.titulo = titulo
        self.mensaje = mensaje
        self.aprobar = aprobar
        self.objeto = objeto