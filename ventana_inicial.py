# -*- coding: utf-8 -*-
from ventana_inicial_ui import *
from ventana_comentario import *
import os
import re
import clases
import pickle
import obtenerGrafo
import math


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
        self.lista_puntos.itemDoubleClicked.connect(self.mostrar_comentario)  # Doble click en un punto -> comentario
        self.lista_segmentos.itemDoubleClicked.connect(self.mostrar_comentario)  # Doble click en un segm -> comentario
        self.lista_puntos.itemClicked.connect(self.resaltar_punto)  # Resaltar punto y no resaltar segmento
        self.lista_segmentos.itemClicked.connect(self.resaltar_segmento)  # Resaltar punto y no resaltar segmento
        self.boton_borrar.clicked.connect(self.borrar_item)  # Borrar un ítem de una de las dos listas
        self.spin_zoom.valueChanged.connect(self.cambiar_zoom)
        # -------------------

        # Menú
        self.actionAbrir_Imagen.triggered.connect(self.abrir_imagen)
        self.actionAbrir_Carpeta.triggered.connect(self.abrir_carpeta)
        self.actionGuardar.triggered.connect(self.guardar_imagen)

        # Ventana comentario
        self.ventana_comentario = None

        self.carpeta = None
        self.imagenes = None
        self.imagen_actual = None  # Un entero que indica la posicion del array de imagenes rango (0, ...)
        self.puntos = None
        self.segmentos = None
        self.zoom = self.spin_zoom.value()
        self.estado = "INIT"  # [INIT, PUNTO, SEGMENTO]
        self.n_puntos = 0
        self.n_segmentos = 0

        self.historial = []  # Historial de edición para (des|re)hacer
        self.resaltado = None

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

        # Cuentos los puntos para saber cómo nombrar nuevos puntos o segmentos
        self.contar_puntos()

    def cargar_puntos(self):
        print("CARGAR MODELO")
        # Inicializamos/Cargamos los puntos y segmentos que pudieran haber sido guardados previamente

        # Asumismos que existe una carpeta con el mismo nombre de la seleccionada, pero bajo ../ANOTACIONES
        path = self.carpeta
        ocurrencias = [i for i, char in enumerate(path) if char == "/"]
        print(ocurrencias)
        nombre_carpeta = path[ocurrencias[-1]+1:]
        carpeta_anotaciones = path[:ocurrencias[-2]]+"/ANOTACIONES/" + nombre_carpeta + "/"

        # Obtenemos los puntos y los segmentos posiblemente guardados previamente
        fichero_puntos = self.imagenes[self.imagen_actual].nombre+"_puntos.pickle"
        fichero_segmentos = self.imagenes[self.imagen_actual].nombre+"_segmentos.pickle"

        print(carpeta_anotaciones)
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

        # Rellenamos las listas de segmentos y puntos
        self.rellenar_listas()

    def add_punto(self, coord_x, coord_y, elemento):
        print("AÑADIR PUNTO")

        # Creo un objeto punto y lo añado al array de puntos
        nombre_punto = "Punto_" + str(self.n_puntos)
        punto = clases.Punto(coord_x, coord_y, nombre_punto)
        self.puntos.append(punto)

        # Aumento el contador de puntos para variar los nombres
        self.n_puntos += 1

        # Añado el punto a la lista de puntos
        print("INCLUIR PUNTO EN LISTA DE PUNTOS")
        item_punto = QtWidgets.QListWidgetItem(self.lista_puntos)
        item_punto.setText(nombre_punto)

        # Añado el elemento visual a la lista de elementos visuales
        self.escena.elementos.update({nombre_punto: elemento})

        # Paso al estado inicial
        self.estado_inicial()

    def add_segmento(self, puntos_segmento, elemento):
        print("AÑADIR SEGMENTO")

        # Creo un objeto segmento y lo añado al array de segmentos
        nombre_segmento = "Segmento_" + str(self.n_segmentos)
        segmento = clases.Segmento(puntos_segmento, nombre_segmento)
        self.segmentos.append(segmento)

        # Aumento el contador de segmentos para variar los nombres
        self.n_segmentos += 1

        # Añado el segmento a la lista de segmentos
        print("INCLUIR SEGMENTO EN LISTA DE SEGMENTOS")
        item_segmento = QtWidgets.QListWidgetItem(self.lista_segmentos)
        item_segmento.setText(nombre_segmento)

        # Añado el elemento visual del segmento en la lista de elementos visuales
        self.escena.elementos.update({nombre_segmento: elemento})

        # Paso al estado inicial
        self.estado_inicial()

    def imagen_previa(self):
        if self.imagen_actual > 0:
            self.guardar_imagen()
            self.desmontar_imagen()
            self.reset_modelo()
            self.vaciar_listas()
            self.imagen_actual -= 1
            self.escena.init_escena()
            self.cargar_imagen()

    def imagen_siguiente(self):
        if self.imagen_actual < (len(self.imagenes) - 1):
            self.guardar_imagen()
            self.desmontar_imagen()
            self.reset_modelo()
            self.vaciar_listas()
            self.imagen_actual += 1
            self.escena.init_escena()
            self.cargar_imagen()

    def estado_inicial(self):
        # Cambio el estado a inicial y el cursor por defecto
        self.estado = "INIT"
        self.frame_edicion.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def guardar_imagen(self):
        print("GUARDAR IMAGEN", self.imagen_actual)

        # Obtengo la carpeta correspondiente a la imagen en ../ANOTACIONES
        path = self.carpeta
        ocurrencias = [i for i, char in enumerate(path) if char == "/"]
        print(ocurrencias)
        nombre_carpeta = path[ocurrencias[-1] + 1:]
        carpeta_anotaciones = path[:ocurrencias[-2]] + "/ANOTACIONES/" + nombre_carpeta + "/"

        # Defino los nombres de los ficheros que guardan los puntos y segmentos incluidos
        fichero_puntos = self.imagenes[self.imagen_actual].nombre + "_puntos.pickle"
        fichero_segmentos = self.imagenes[self.imagen_actual].nombre + "_segmentos.pickle"
        print(fichero_puntos)
        print(fichero_segmentos)

        # Guardo los arrays de puntos y segmentos en los ficheros para que presistan los datos
        with open(carpeta_anotaciones + fichero_puntos, 'wb') as file:
            pickle.dump(self.puntos, file)

        with open(carpeta_anotaciones + fichero_segmentos, 'wb') as file:
            pickle.dump(self.segmentos, file)

        # Genero el grafo de salida usando obtenerGrafo
        fichero_grafo = self.imagenes[self.imagen_actual].nombre + "_grafo.txt"
        ruta_fichero_grafo = carpeta_anotaciones + fichero_grafo
        self.guardar_grafo(ruta_fichero_grafo)

    def desmontar_imagen(self):
        # Encuentro el elemento en la escena que es de tipo imagen y lo quito
        for item_escena in self.escena.items():
            if type(item_escena) == QtWidgets.QGraphicsPixmapItem:
                self.escena.removeItem(item_escena)

    def vaciar_listas(self):
        # Vacío los ítems de lista de las listas de segmentos y puntos
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
            # Añado el segmento a la lista de segmentos
            print("INCLUIR SEGMENTO EN LISTA DE SEGMENTOS")
            item_segmento = QtWidgets.QListWidgetItem(self.lista_segmentos)
            item_segmento.setText(segmento.nombre)

    def dibujar_puntos(self):
        """Este método se llama cuando se cargan los datos previamente guardados de una imagen"""

        # Una vez obtenidos los puntos y segmentos, recorro estos arrays y dibujo en la escena sus elementos visuales
        for punto in self.puntos:
            elemento = self.escena.dibujar_punto(punto)

            # Incluir el elemento en la lista de elementos
            self.escena.elementos.update({punto.nombre: elemento})

        for segmento in self.segmentos:
            elemento = self.escena.dibujar_segmento(segmento)

            # Incluir el elemento en la lista de elementos
            self.escena.elementos.update({segmento.nombre: elemento})

    def reset_modelo(self):
        self.estado = "INIT"
        self.puntos = None
        self.segmentos = None
        self.n_puntos = 0
        self.n_segmentos = 0
        self.historial = None
        self.resaltado = None
        self.spin_zoom.setValue(1)

    def guardar_grafo(self, ruta_fichero):
        print("GUARDAR GRAFO")

        trazos = []

        # Creo una lista con los puntos y segmentos del tipo [ [(x,y)], [(x,y),(x,y)] ... ]
        for segmento in self.segmentos:
            trazos_segmento = []
            for punto in segmento.puntos:
                trazos_segmento.append((round(punto.x), round(punto.y)))  # Coordenadas sin decimales
            trazos.append(trazos_segmento)

        for punto in self.puntos:
            trazos.append([(round(punto.x), round(punto.y))])  # Coordenadas sin decimales

        print(trazos, "TRAZOS")
        print("GENERANDO GRAFO")
        print(trazos, "TRAZOS")
        # Genero el grafo
        grafo = obtenerGrafo.obtenerGrafo(trazos, 6)
        print("GUARDANDO GRAFO")
        # Guardo el grafo en .txt
        obtenerGrafo.salvarGrafo(grafo[0], grafo[1], ruta_fichero)

    def mostrar_comentario(self):
        # Obtengo el nombre y el índice del punto o segmento seleccionado
        nombre, index = self.resaltado
        tipo_item = nombre.split("_")[0]
        # Creo la ventana para el comentario indicando si es segmento o punto y su posición en el array (y lista)
        self.ventana_comentario = CommentWindow(parent=self, tipo_item=tipo_item, index=index)
        self.ventana_comentario.show()

    def borrar_item(self):
        print("BORRAR ITEM SELECCIONADO")

        if self.resaltado is not None:
            # Obtengo el nombre y el índice del elemento a borrar
            nombre, index = self.resaltado
            print("BORRAR ITEM CON INDICE ", index, nombre)
            if "Segmento" in nombre:
                # Borro el elemento visual de la escena
                self.escena.borrar_elemento(self.segmentos[index].nombre)

                # Defino el nuevo array de segmentos
                nuevos_segmentos = [segmento for i, segmento in enumerate(self.segmentos) if i != index]
                self.segmentos = nuevos_segmentos

                # Elimino el segmento de la lista de segmentos
                self.lista_segmentos.takeItem(index)
                print(self.segmentos, "SEGMENTOS DESPUÉS DE BORRADO")

                # Elimno el focus de la lista de segmentos
                self.lista_segmentos.setCurrentIndex(QtCore.QModelIndex())

            elif "Punto" in nombre:
                # Borro el elemento visual de la escena
                self.escena.borrar_elemento(self.puntos[index].nombre)

                # Obtengo nuevo array de puntos
                nuevos_puntos = [punto for i, punto in enumerate(self.puntos) if i != index]
                self.puntos = nuevos_puntos

                # Elimino el punto de la lista de puntos
                self.lista_puntos.takeItem(index)
                print(self.puntos)
                print(self.puntos, "PUNTOS DESPUÉS DE BORRADO")

                # Elimino el focus de la lista de puntos
                self.lista_puntos.setCurrentIndex(QtCore.QModelIndex())

        self.contar_puntos()
        self.resaltado = None

    def resaltar_punto(self):
        """Esta función establece cuál es el punto que ha sido seleccionado por última vez"""
        # Quito el focus de la lista de segmentos para permitir sólo 1 elemento seleccionado a la vez de las 2 listas
        self.lista_segmentos.clearFocus()
        self.lista_segmentos.setCurrentIndex(QtCore.QModelIndex())
        # Obtengo el elemento seleccionado
        self.resaltado = self.lista_puntos.currentItem().text(), self.lista_puntos.currentRow()
        print(self.resaltado)

    def resaltar_segmento(self):
        self.lista_puntos.clearFocus()
        self.lista_puntos.setCurrentIndex(QtCore.QModelIndex())
        self.resaltado = self.lista_segmentos.currentItem().text(), self.lista_segmentos.currentRow()
        print(self.resaltado)

    def contar_puntos(self):
        """Esta función establece cuál es el contador de puntos o segmentos para crear nuevos nombres"""
        print("CONTAR PUNTOS")
        if self.puntos is not None:
            if len(self.puntos) > 0:
                max = -1
                for punto in self.puntos:
                    if int(punto.nombre.split("_")[1]) > max:
                        max = int(punto.nombre.split("_")[1])
                self.n_puntos = max + 1
            else:
                self.n_puntos = 0
        else:
            self.n_puntos = 0

        if self.segmentos is not None:
            if len(self.segmentos) > 0:
                max = -1
                for segmento in self.segmentos:
                    if int(segmento.nombre.split("_")[1]) > max:
                        max = int(segmento.nombre.split("_")[1])
                self.n_segmentos = max + 1
            else:
                self.n_segmentos = 0
        else:
            self.n_segmentos = 0

    def cambiar_zoom(self):
        # Quitar zoom
        self.frame_edicion.scale(1/self.zoom, 1/self.zoom)

        # Poner zoom
        self.zoom = self.spin_zoom.value()
        self.frame_edicion.scale(self.zoom, self.zoom)


class MyGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.parent = parent
        self.creacion_segmento = False
        self.path = None
        self.path_item = None
        self.path_pen = QtGui.QPen(QtCore.Qt.darkGreen, 4)
        self.recta_apoyo = None
        self.elementos = {}

    def init_escena(self):
        self.creacion_segmento = False
        self.path = None
        self.path_item = None
        self.recta_apoyo = None
        self.elementos = {}

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

        self.parent.add_segmento(puntos, self.path_item)

        # Elimino las variables de manejo del path
        self.path = None
        self.path_item = None
        self.creacion_segmento = False

    def dibujar_punto(self, punto):
        print("DIBUJAR PUNTO")
        # Configuro el pincel y la brocha
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)

        # Obtengo las coordenadas del evento de click
        x = punto.x
        y = punto.y

        # Dibujo el punto y lo devuelvo
        elipse = self.addEllipse(x, y, 4, 4, pen, brush)
        return elipse

    def dibujar_segmento(self, segmento):
        print("DIBUJAR SEGMENTO")
        path = QtGui.QPainterPath(QtCore.QPointF(segmento.puntos[0].x, segmento.puntos[0].y))
        for punto in segmento.puntos[1:]:
            path.lineTo(QtCore.QPointF(punto.x, punto.y))

        # Dibujo el segmento y lo devuelvo
        path = self.addPath(path, pen=self.path_pen)
        return path

    def borrar_elemento(self, nombre_elemento):
        elemento_a_borrar = self.elementos.get(nombre_elemento)
        print(elemento_a_borrar, "ITEM A BORRAR")
        print(type(elemento_a_borrar), "TIPO DE ITEM A BORRAR")
        self.removeItem(elemento_a_borrar)
        for item in self.items():
            if item is elemento_a_borrar or item == elemento_a_borrar:
                self.removeItem(item)
                print("BORRADO")
        self.elementos.pop(nombre_elemento)
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    try:
        app.exec_()
    except:
        pass
