class Imagen:
    def __init__(self, ruta, nombre, formato):
        self.nombre = nombre
        self.ruta = ruta
        self.formato = formato
        self.segmentos = []


class Segmento:
    def __init__(self, puntos, nombre, elemento):
        self.nombre = nombre
        self.puntos = puntos
        self.comentario = None
        self.elemento = elemento


class Punto:
    def __init__(self, x, y, nombre = None, elemento = None):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.comentario = None
        self.elemento = elemento
