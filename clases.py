class Imagen:
    def __init__(self, ruta, nombre, formato):
        self.nombre = nombre
        self.ruta = ruta
        self.formato = formato
        self.segmentos = []


class Segmento:
    def __init__(self, puntos, nombre, etiqueta):
        self.nombre = nombre
        self.puntos = puntos
        self.titulo = etiqueta + " : " + nombre
        self.etiqueta = etiqueta
        self.comentario = None


class Punto:
    def __init__(self, x, y, nombre = None, etiqueta = None):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.etiqueta = etiqueta
        self.comentario = None
        if self.nombre is not None and self.etiqueta is not None:
            self.titulo = etiqueta + " : " + nombre
