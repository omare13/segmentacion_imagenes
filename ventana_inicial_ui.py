# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spin_zoom = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_zoom.setGeometry(QtCore.QRect(810, 80, 91, 31))
        self.spin_zoom.setMaximum(5)
        self.spin_zoom.setObjectName("spin_zoom")
        self.label_zoom = QtWidgets.QLabel(self.centralwidget)
        self.label_zoom.setGeometry(QtCore.QRect(740, 80, 51, 31))
        self.label_zoom.setObjectName("label_zoom")
        self.lista_segmentos = QtWidgets.QListWidget(self.centralwidget)
        self.lista_segmentos.setGeometry(QtCore.QRect(740, 160, 161, 201))
        self.lista_segmentos.setObjectName("lista_segmentos")
        self.label_segmentos = QtWidgets.QLabel(self.centralwidget)
        self.label_segmentos.setGeometry(QtCore.QRect(740, 130, 141, 20))
        self.label_segmentos.setObjectName("label_segmentos")
        self.lista_puntos = QtWidgets.QListWidget(self.centralwidget)
        self.lista_puntos.setGeometry(QtCore.QRect(740, 430, 161, 192))
        self.lista_puntos.setObjectName("lista_puntos")
        self.label_puntos = QtWidgets.QLabel(self.centralwidget)
        self.label_puntos.setGeometry(QtCore.QRect(740, 400, 141, 21))
        self.label_puntos.setObjectName("label_puntos")
        self.boton_punto = QtWidgets.QToolButton(self.centralwidget)
        self.boton_punto.setGeometry(QtCore.QRect(60, 30, 61, 31))
        self.boton_punto.setObjectName("boton_punto")
        self.boton_segmento = QtWidgets.QToolButton(self.centralwidget)
        self.boton_segmento.setGeometry(QtCore.QRect(140, 30, 61, 31))
        self.boton_segmento.setObjectName("boton_segmento")
        self.boton_deshacer = QtWidgets.QToolButton(self.centralwidget)
        self.boton_deshacer.setGeometry(QtCore.QRect(480, 30, 61, 31))
        self.boton_deshacer.setObjectName("boton_deshacer")
        self.boton_rehacer = QtWidgets.QToolButton(self.centralwidget)
        self.boton_rehacer.setGeometry(QtCore.QRect(550, 30, 61, 31))
        self.boton_rehacer.setObjectName("boton_rehacer")
        self.frame_edicion = QtWidgets.QGraphicsView(self.centralwidget)
        self.frame_edicion.setGeometry(QtCore.QRect(25, 81, 691, 541))
        self.frame_edicion.setObjectName("frame_edicion")

        # https://stackoverflow.com/questions/7772080/tracking-mouse-move-in-qgraphicsscene-class
        self.frame_edicion.setMouseTracking(True)

        self.boton_borrar = QtWidgets.QToolButton(self.centralwidget)
        self.boton_borrar.setGeometry(QtCore.QRect(660, 30, 51, 31))
        self.boton_borrar.setObjectName("boton_borrar")
        self.boton_previo = QtWidgets.QToolButton(self.centralwidget)
        self.boton_previo.setGeometry(QtCore.QRect(300, 30, 41, 31))
        self.boton_previo.setObjectName("boton_previo")
        self.boton_siguiente = QtWidgets.QToolButton(self.centralwidget)
        self.boton_siguiente.setGeometry(QtCore.QRect(350, 30, 41, 31))
        self.boton_siguiente.setObjectName("boton_siguiente")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(MainWindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 930, 26))
        self.menu.setObjectName("menu")
        self.menuMen = QtWidgets.QMenu(self.menu)
        self.menuMen.setObjectName("menuMen")
        self.menuEdici_n = QtWidgets.QMenu(self.menu)
        self.menuEdici_n.setObjectName("menuEdici_n")
        MainWindow.setMenuBar(self.menu)
        self.barra_estado = QtWidgets.QStatusBar(MainWindow)
        self.barra_estado.setObjectName("barra_estado")
        MainWindow.setStatusBar(self.barra_estado)
        self.actionAbrir_Carpeta = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Carpeta.setObjectName("actionAbrir_Carpeta")
        self.actionAbrir_Imagen = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Imagen.setObjectName("actionAbrir_Imagen")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.menuMen.addAction(self.actionAbrir_Carpeta)
        self.menuMen.addAction(self.actionAbrir_Imagen)
        self.menuEdici_n.addAction(self.actionGuardar)
        self.menu.addAction(self.menuMen.menuAction())
        self.menu.addAction(self.menuEdici_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_zoom.setText(_translate("MainWindow", "Zoom"))
        self.label_segmentos.setText(_translate("MainWindow", "Segmentos"))
        self.label_puntos.setText(_translate("MainWindow", "Puntos"))
        self.boton_punto.setText(_translate("MainWindow", "P"))
        self.boton_segmento.setText(_translate("MainWindow", "S"))
        self.boton_deshacer.setText(_translate("MainWindow", "CTRL+Z"))
        self.boton_rehacer.setText(_translate("MainWindow", "CTRL+Y"))
        self.boton_borrar.setText(_translate("MainWindow", "DEL"))
        self.boton_previo.setText(_translate("MainWindow", "<-"))
        self.boton_siguiente.setText(_translate("MainWindow", "->"))
        self.menuMen.setTitle(_translate("MainWindow", "Menú"))
        self.menuEdici_n.setTitle(_translate("MainWindow", "Edición"))
        self.actionAbrir_Carpeta.setText(_translate("MainWindow", "Abrir Carpeta"))
        self.actionAbrir_Imagen.setText(_translate("MainWindow", "Abrir Imagen"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

