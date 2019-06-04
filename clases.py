class Imagen:
    def __init__(self, ruta, nombre, formato):
        self.nombre = nombre
        self.ruta = ruta
        self.formato = formato
        self.segmentos = []


class Segmento:
    def __init__(self, puntos, nombre):
        self.nombre = nombre
        self.puntos = puntos
        self.comentario = None


class Punto:
    def __init__(self, x, y, nombre = None):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.comentario = None
