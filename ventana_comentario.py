from ventana_comentario_ui import *


class CommentWindow(QtWidgets.QDialog, Ui_ventana_comentario):
    def __init__(self, parent, tipo_item, index, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.parent = parent

        self.tipo_item = tipo_item
        self.index = index
        self.dato = None

        # Mostrar comentario si existe
        if self.tipo_item == "Segmento":
            self.dato = self.parent.segmentos[self.index]
        elif self.tipo_item == "Punto":
            self.dato = self.parent.puntos[self.index]
        if self.dato.comentario is not None:
            self.texto_comentario.setPlainText(self.dato.comentario)

        # Botones --> acciones
        self.boton_cancelar.clicked.connect(self.cancelar_comentario)  # Botón cancelar edición comentario
        self.boton_aceptar.clicked.connect(self.aceptar_comentario)  # Botón guardar cambios comentario
        # -------------------

    def cancelar_comentario(self):
        print("CANCELAR COMENTARIO")
        self.destroy()

    def aceptar_comentario(self):
        print("ACEPTAR COMENTARIO")
        if self.tipo_item == "Segmento":
            print("GUARDAR COMENTARIO DE SEGEMENTO")
            self.parent.segmentos[self.index].comentario = self.texto_comentario.toPlainText()
        elif self.tipo_item == "Punto":
            print("GUARDAR COMETNARIO DE PUNTO")
            self.parent.puntos[self.index].comentario = self.texto_comentario.toPlainText()
        self.destroy()
