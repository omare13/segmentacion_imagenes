from ventana_inicial_ui import *
import os
import re
import clases


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Creamos escena para poder dibujar sobre frame_edicion (GraphicsView)
        self.escena = MyGraphicsScene(self)
        self.frame_edicion.setScene(self.escena)

        # Botones --> acciones
        self.boton_punto.clicked.connect(self.nuevo_punto)  # Botón nuevo punto
        self.boton_segmento.clicked.connect(self.nuevo_segmento)  # Botón nuevo segmento
        self.boton_previo.clicked.connect(self.imagen_previa)  # Botón de imagen previa
        self.boton_siguiente.clicked.connect(self.imagen_siguiente)  # Botón de imagen siguiente
        # -------------------

        # Menú
        self.actionAbrir_Imagen.triggered.connect(self.abrir_imagen)
        self.actionAbrir_Carpeta.triggered.connect(self.abrir_carpeta)

        self.carpeta = None
        self.imagenes = None
        self.imagen_actual = None
        self.puntos = None
        self.segmentos = None
        self.zoom = 0
        self.estado = "INIT"  # [INIT, PUNTO, SEGMENTO]
        self.n_puntos = 0
        self.n_segmentos = 0
        self.historial = None  # Historial de edición para (des|re)hacer

    def nuevo_punto(self):
        if self.imagen_actual is not None:
            print("SELECCIÓN PUNTO")

            # Cambio la forma del cursor del frame de edición
            self.frame_edicion.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

            # El estado es PUNTO
            self.estado = "PUNTO"

    def nuevo_segmento(self):
        print("SELECCIÓN SEGMENTO")

        # Cambio la forma del cursor del frame edición
        self.frame_edicion.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

    def abrir_carpeta(self):
        print("ABRIR CARPETA")
        # Variable de control qué formatos peuden tener?
        formatos_validos = [".jpg", ".bmp", ".gif"]
        # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtgui/qpixmap.html?highlight=qpixmap#reading-and-writing-image-files

        # Diálogo de selección de carpeta
        self.carpeta = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Seleccionar fichero"))
        print("CARPETA SELECCIONADA", self.carpeta)

        # Inicializamos las imágenes de la carpeta
        self.imagenes = []

        # Comprobamos que hay imágenes y las recuperamos
        for fichero in os.listdir(self.carpeta):
            extension = re.match(r'(.*)(\.[a-zA-Z0-9]{1,5})', fichero)
            nombre_fichero = extension.group(1)
            extension_fichero = extension.group(2)
            if extension_fichero in formatos_validos:
                imagen = clases.Imagen(ruta=self.carpeta + "/" + fichero, nombre=nombre_fichero,
                                       formato=extension_fichero)
                self.imagenes.append(imagen)

        if len(self.imagenes) > 0:
            print("CARGA DE " + str(len(self.imagenes)) + " IMÁGENES")
            self.imagen_actual = 0
            print("IMAGEN ACTUAL ", self.imagen_actual)
            self.cargar_imagen()
        else:
            self.imagenes = None
            print("NO SE ENCONTRARON IMÁGENES")

    def abrir_imagen(self):
        print(self.imagen_actual)
        print("ABRIR IMAGEN")

    def cargar_imagen(self):
        print("CARGAR IMAGEN")
        ruta_imagen = self.imagenes[self.imagen_actual].ruta
        imagen = QtGui.QPixmap(ruta_imagen)
        # self.painter.drawImage(self.frame_edicion.frameRect(), imagen)
        self.escena.addPixmap(imagen)
        print("CARGADA IMAGEN ", self.imagenes[self.imagen_actual].nombre)
        self.puntos = []
        self.segmentos = []
        # TODO - Incluir la forma de cargar puntos y segmentos previamente incluidos (de una imagen guardada)

    def add_punto(self, coord_x, coord_y, elemento):
        print("AÑADIR PUNTO")
        # Creo un objeto punto y lo añado al aray de puntos
        nombre_punto = "Punto_" + str(self.n_puntos)
        punto = clases.Punto(coord_x, coord_y, nombre_punto)
        self.puntos.append(punto)

        # Aumento el contador de puntos para variar los nombres
        self.n_puntos += 1

        # Añado el punto a la lista de puntos
        print("INCLUIR PUNTO EN LISTA DE PUNTOS")
        item_punto = QtWidgets.QListWidgetItem(self.lista_puntos)
        item_punto.setText(nombre_punto)

        # Añado el ítem al historial de ediciones



    def imagen_previa(self):
        if self.imagen_actual > 0:
            self.imagen_actual -= 1
            self.cargar_imagen()

    def imagen_siguiente(self):
        if self.imagen_actual < (len(self.imagenes) - 1):
            self.imagen_actual += 1
            self.cargar_imagen()

class MyGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.parent = parent

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        if self.parent.estado == "PUNTO":
            # Configuro el pincel y la brocha
            pen = QtGui.QPen(QtCore.Qt.black)
            brush = QtGui.QBrush(QtCore.Qt.black)

            # Obtengo las coordenadas del evento de click
            x = QGraphicsSceneMouseEvent.scenePos().x()
            y = QGraphicsSceneMouseEvent.scenePos().y()

            # Dibujo el punto
            elipse = self.addEllipse(x, y, 4, 4, pen, brush)
            print(self.items())
            print("PUNTO DIBUJADO")

            # Actualizo la lista de puntos
            nombre_elemento = self.parent.add_punto(x, y, elipse)

            # Cambio el estado a inicial y el cursor por defecto
            self.parent.estado = "INIT"
            self.parent.frame_edicion.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
