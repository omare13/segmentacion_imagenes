# -*- coding: utf-8 -*-
from ventana_inicial_ui import *
import os
import re
import clases
import pickle
import obtenerGrafo


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
        self.actionGuardar.triggered.connect(self.guardar_imagen)

        self.carpeta = None
        self.imagenes = None
        self.imagen_actual = None  # Un entero que indica la posicion del array de imagenes rango (0, ...)
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
        if self.imagen_actual is not None:
            print("SELECCIÓN SEGMENTO")

            # Cambio la forma del cursor del frame edición
            self.frame_edicion.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

            # El estado es SEGMENTO
            self.estado = "SEGMENTO"

    def abrir_carpeta(self):
        print("ABRIR CARPETA")
        # Variable de control qué formatos peuden tener?
        formatos_validos = [".jpg", ".bmp", ".gif"]
        # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtgui/qpixmap.html?highlight=qpixmap#reading-and-writing-image-files

        # Diálogo de selección de carpeta
        self.carpeta = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Seleccionar fichero"))
        if len(self.carpeta) > 0:
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

        # Diálogo de selección de imagen
        ruta_imagen = str(QtWidgets.QFileDialog.getOpenFileName(self, caption="Seleccionar imagen",
                                                                filter="Images (*.png *.xpm *.jpg)"))
        ruta_imagen = (ruta_imagen[2:ruta_imagen.rfind(",") - 1])

        if len(ruta_imagen) > 0:
            self.carpeta = ruta_imagen[:ruta_imagen.rfind('/')]
            fichero = ruta_imagen[ruta_imagen.rfind('/')+1:]
            extension = re.match(r'(.*)(\.[a-zA-Z0-9]{1,5})', fichero)
            nombre_fichero = extension.group(1)
            extension_fichero = extension.group(2)

            # Creamos el objeto imagen y lo incluimos
            self.imagenes = []
            imagen = clases.Imagen(ruta=self.carpeta + "/" + fichero, nombre=nombre_fichero,
                                   formato=extension_fichero)
            self.imagenes.append(imagen)
            print(imagen.__dict__)

            # Chequeamos que se haya cargado la imagen
            if len(self.imagenes) > 0:
                print("CARGA DE " + str(len(self.imagenes)) + " IMÁGENES")
                self.imagen_actual = 0
                print("IMAGEN ACTUAL ", self.imagen_actual)
                self.cargar_imagen()
            else:
                self.imagenes = None
                print("NO SE ENCONTRARON IMÁGENES")

    def cargar_imagen(self):
        print("CARGAR IMAGEN")
        ruta_imagen = self.imagenes[self.imagen_actual].ruta

        # Creamos la imagen a partir de su ruta en el sistema de ficheros y la dibujamos
        imagen = QtGui.QPixmap(ruta_imagen)
        # self.painter.drawImage(self.frame_edicion.frameRect(), imagen)
        self.escena.addPixmap(imagen)
        print("CARGADA IMAGEN ", self.imagenes[self.imagen_actual].nombre)

        # Cargamos datos posiblemente guardados en otra ocasión
        self.cargar_puntos()

        # Dibujamos los elementos que se pudieron guardar
        self.dibujar_puntos()

    def cargar_puntos(self):
        print("CARGAR MODELO")
        # Inicializamos/Cargamos los puntos y segmentos que pudieran haber sido guardados previamente
        path = self.carpeta
        ocurrencias = [i for i, char in enumerate(path) if char == "/"]
        print(ocurrencias)
        nombre_carpeta = path[ocurrencias[-1]+1:]
        carpeta_anotaciones = path[:ocurrencias[-2]]+"/ANOTACIONES/" + nombre_carpeta + "/"

        fichero_puntos = self.imagenes[self.imagen_actual].nombre+"_puntos.pickle"
        fichero_segmentos = self.imagenes[self.imagen_actual].nombre+"_segmentos.pickle"

        if fichero_puntos in os.listdir(carpeta_anotaciones):
            print("ENCONTRADOS PUNTOS")
            with open(carpeta_anotaciones + fichero_puntos, "rb") as file:
                self.puntos = pickle.load(file)
        else:
            self.puntos = []
            print("NO SE ENCONTRARON PUNTOS GUARDADOS")

        if fichero_segmentos in os.listdir(carpeta_anotaciones):
            print("ENCONTRADOS SEGMENTOS")
            with open(carpeta_anotaciones + fichero_segmentos, "rb") as file:
                self.segmentos = pickle.load(file)
        else:
            self.segmentos = []
            print("NO SE ENCONTRARON PUNTOS GUARDADOS")

        self.rellenar_listas()

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

        # TODO - Añado el ítem al historial de ediciones

        # Paso al estado inicial
        self.estado_inicial()

    def add_segmento(self, puntos_segmento, elemento):
        print("AÑADIR SEGMENTO")
        # Creo un objeto segmento y lo añado al aray de segmentos
        nombre_segmento = "Segmento_" + str(self.n_segmentos)

        # Creo el segmento y lo añado al array de segmentos
        segmento = clases.Segmento(puntos_segmento, nombre_segmento)
        self.segmentos.append(segmento)

        # Aumento el contador de segmentos para variar los nombres
        self.n_segmentos += 1

        # Añado el segmento a la lista de segmentos
        print("INCLUIR SEGMENTO EN LISTA DE SEGMENTOS")
        item_segmento = QtWidgets.QListWidgetItem(self.lista_segmentos)
        item_segmento.setText(nombre_segmento)

        # TODO - Añado ítem al historial de ediciones

        # Paso al estado inicial
        self.estado_inicial()

    def imagen_previa(self):
        if self.imagen_actual > 0:
            self.guardar_imagen()
            self.desmontar_imagen()
            self.reset_modelo()
            self.vaciar_listas()
            self.imagen_actual -= 1
            self.cargar_imagen()

    def imagen_siguiente(self):
        if self.imagen_actual < (len(self.imagenes) - 1):
            self.guardar_imagen()
            self.desmontar_imagen()
            self.reset_modelo()
            self.vaciar_listas()
            self.imagen_actual += 1
            self.cargar_imagen()

    def estado_inicial(self):
        # Cambio el estado a inicial y el cursor por defecto
        self.estado = "INIT"
        self.frame_edicion.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def guardar_imagen(self):
        print("GUARDAR IMAGEN", self.imagen_actual)

        path = self.carpeta
        ocurrencias = [i for i, char in enumerate(path) if char == "/"]
        print(ocurrencias)
        nombre_carpeta = path[ocurrencias[-1] + 1:]
        carpeta_anotaciones = path[:ocurrencias[-2]] + "/ANOTACIONES/" + nombre_carpeta + "/"

        fichero_puntos = self.imagenes[self.imagen_actual].nombre + "_puntos.pickle"
        fichero_segmentos = self.imagenes[self.imagen_actual].nombre + "_segmentos.pickle"
        print(fichero_puntos)
        print(fichero_segmentos)

        if len(self.puntos) > 0:
            with open(carpeta_anotaciones + fichero_puntos, 'wb') as file:
                pickle.dump(self.puntos, file)

        if len(self.segmentos) > 0:
            with open(carpeta_anotaciones + fichero_segmentos, 'wb') as file:
                pickle.dump(self.segmentos, file)

        # TODO - Los paso a grafo
        fichero_grafo = self.self.imagenes[self.imagen_actual].nombre + "_grafo.txt"
        ruta_fichero_grafo = carpeta_anotaciones + fichero_grafo
        self.guardar_grafo(ruta_fichero_grafo)

    def desmontar_imagen(self):
        for item_escena in self.escena.items():
            if type(item_escena) == QtWidgets.QGraphicsPixmapItem:
                self.escena.removeItem(item_escena)

    def vaciar_listas(self):
        listas = [self.lista_segmentos, self.lista_puntos]
        for lista in listas:
            lista.clear()

    def rellenar_listas(self):
        for punto in self.puntos:
            # Añado el punto a la lista de puntos
            print("INCLUIR PUNTO EN LISTA DE PUNTOS")
            item_punto = QtWidgets.QListWidgetItem(self.lista_puntos)
            item_punto.setText(punto.nombre)
        for segmento in self.segmentos:
            # Añado el punto a la lista de puntos
            print("INCLUIR SEGMENTO EN LISTA DE SEGMENTOS")
            item_punto = QtWidgets.QListWidgetItem(self.lista_segmentos)
            item_punto.setText(segmento.nombre)

    def dibujar_puntos(self):
        for punto in self.puntos:
            self.escena.dibujar_punto(punto)

        for segmento in self.segmentos:
            self.escena.dibujar_segmento(segmento)

    def reset_modelo(self):
        self.estado = "INIT"
        self.puntos = None
        self.segmentos = None
        self.n_puntos = 0
        self.n_segmentos = 0

    def guardar_grafo(self, ruta_fichero):
        print("GENERAR GRAFO")
        trazos = [[punto.x, punto.y] for punto in self.puntos]
        for segmento in self.segmentos:
            for punto in segmento.puntos:
                trazos.append([punto.x, punto.y])
        grafo = obtenerGrafo.obtenerGrafo(trazos, 6)
        print("GUARDAR GRAFO")
        obtenerGrafo.salvarGrafo(grafo[0], grafo[1], ruta_fichero)


class MyGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.parent = parent
        self.creacion_segmento = False
        self.path = None
        self.path_item = None
        self.path_pen = QtGui.QPen(QtCore.Qt.darkGreen, 4)
        self.recta_apoyo = None

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        if self.parent.estado == "PUNTO":
            self.crear_punto(QGraphicsSceneMouseEvent)

        elif self.parent.estado == "SEGMENTO":
            # Si se indica la opción segmento pero se hace click derecho (botón número 2), entonces se crea un punto
            if (QGraphicsSceneMouseEvent.button() == 2) and (self.creacion_segmento is False):
                self.crear_punto(QGraphicsSceneMouseEvent)

            # Si se indica opción segmento y se hace click izqdo(botón 1) por 1ª vez, entramos en creación de segmento
            elif (QGraphicsSceneMouseEvent.button() == 1) and (self.creacion_segmento is False):
                self.removeItem(self.recta_apoyo)
                print("PUNTO INICIAL DEL SEGMENTO")
                # Indicamos que actualmente se está creando un segmento
                self.creacion_segmento = True
                # Incluimos el punto inicial al path
                self.path = QtGui.QPainterPath(QGraphicsSceneMouseEvent.scenePos())
                print(self.path.isEmpty())
                self.path_item = self.addPath(self.path, pen=self.path_pen)
                print(self.items())

            # Si estamos en creación de segmento y se hace click izquierdo, generamos el path desde el punto anterior
            elif (QGraphicsSceneMouseEvent.button() == 1) and (self.creacion_segmento is True):
                self.removeItem(self.recta_apoyo)
                print("CONTINÚA EDICIÓN SEGMENTO")
                self.path.lineTo(QGraphicsSceneMouseEvent.scenePos())
                self.removeItem(self.path_item)
                self.path_item = self.addPath(self.path, pen=self.path_pen)
                print(self.items())

            # Si se acaba la creación de segmento
            elif (QGraphicsSceneMouseEvent.button() == 2) and (self.creacion_segmento is True):
                self.removeItem(self.recta_apoyo)
                print("FINAL DE EDICIÓN SEGMENTO")
                self.path.lineTo(QGraphicsSceneMouseEvent.scenePos())
                self.removeItem(self.path_item)
                self.path_item = self.addPath(self.path, pen=self.path_pen)
                self.crear_segmento()

    def mouseMoveEvent(self, evento):
        print("MOUSE MOVE")
        if (self.parent.estado == "SEGMENTO") and (self.creacion_segmento is True):
            print("RECTA APOYO")
            if self.recta_apoyo is not None:
                print("BORRAR RECTA APOYO")
                self.removeItem(self.recta_apoyo)
            print("CREAR RECTA APOYO")
            print(self.path.currentPosition(), evento.scenePos())
            self.recta_apoyo = self.addLine(QtCore.QLineF(self.path.currentPosition(), evento.scenePos()))

    def crear_punto(self, evento):
        # Configuro el pincel y la brocha
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)

        # Obtengo las coordenadas del evento de click
        x = evento.scenePos().x()
        y = evento.scenePos().y()

        # Dibujo el punto
        elipse = self.addEllipse(x, y, 4, 4, pen, brush)
        print(self.items())
        print("PUNTO DIBUJADO")

        # Incluyo el punto
        self.parent.add_punto(x, y, elipse)

    def crear_segmento(self):
        print("CREAR SEGMENTO")
        print(self)
        puntos = []
        for i_elemento in range(self.path.elementCount()):
            punto = clases.Punto(self.path.elementAt(i_elemento).x, self.path.elementAt(i_elemento).y)
            puntos.append(punto)

        self.parent.add_segmento(puntos, self.path)

        # Elimino las variables de manejo del path
        self.path = None
        self.path_item = None
        self.creacion_segmento = False

    def dibujar_punto(self, punto):
        # Configuro el pincel y la brocha
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)

        # Obtengo las coordenadas del evento de click
        x = punto.x
        y = punto.y

        # Dibujo el punto
        elipse = self.addEllipse(x, y, 4, 4, pen, brush)

    def dibujar_segmento(self, segmento):
        path = QtGui.QPainterPath(QtCore.QPointF(segmento.puntos[0].x, segmento.puntos[0].y))
        for punto in segmento.puntos[1:]:
            path.lineTo(QtCore.QPointF(punto.x, punto.y))
        self.addPath(path, pen=self.path_pen)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
