# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_zoom = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_zoom.sizePolicy().hasHeightForWidth())
        self.label_zoom.setSizePolicy(sizePolicy)
        self.label_zoom.setObjectName("label_zoom")
        self.horizontalLayout_5.addWidget(self.label_zoom)
        spacerItem1 = QtWidgets.QSpacerItem(5, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.spin_zoom = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_zoom.sizePolicy().hasHeightForWidth())
        self.spin_zoom.setSizePolicy(sizePolicy)
        self.spin_zoom.setMinimum(1)
        self.spin_zoom.setMaximum(5)
        self.spin_zoom.setProperty("value", 1)
        self.spin_zoom.setObjectName("spin_zoom")
        self.horizontalLayout_5.addWidget(self.spin_zoom)
        spacerItem2 = QtWidgets.QSpacerItem(63, 13, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_segmentos = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_segmentos.sizePolicy().hasHeightForWidth())
        self.label_segmentos.setSizePolicy(sizePolicy)
        self.label_segmentos.setObjectName("label_segmentos")
        self.verticalLayout_2.addWidget(self.label_segmentos)
        self.lista_segmentos = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lista_segmentos.sizePolicy().hasHeightForWidth())
        self.lista_segmentos.setSizePolicy(sizePolicy)
        self.lista_segmentos.setMaximumSize(QtCore.QSize(175, 16777215))
        self.lista_segmentos.setObjectName("lista_segmentos")
        self.verticalLayout_2.addWidget(self.lista_segmentos)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_puntos = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_puntos.sizePolicy().hasHeightForWidth())
        self.label_puntos.setSizePolicy(sizePolicy)
        self.label_puntos.setObjectName("label_puntos")
        self.verticalLayout_3.addWidget(self.label_puntos)
        self.lista_puntos = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lista_puntos.sizePolicy().hasHeightForWidth())
        self.lista_puntos.setSizePolicy(sizePolicy)
        self.lista_puntos.setMaximumSize(QtCore.QSize(175, 16777215))
        self.lista_puntos.setObjectName("lista_puntos")
        self.verticalLayout_3.addWidget(self.lista_puntos)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.boton_editar = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_editar.sizePolicy().hasHeightForWidth())
        self.boton_editar.setSizePolicy(sizePolicy)
        self.boton_editar.setBaseSize(QtCore.QSize(0, 0))
        self.boton_editar.setObjectName("boton_editar")
        self.horizontalLayout.addWidget(self.boton_editar)
        self.combobox_editar = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_editar.sizePolicy().hasHeightForWidth())
        self.combobox_editar.setSizePolicy(sizePolicy)
        self.combobox_editar.setMinimumSize(QtCore.QSize(140, 0))
        self.combobox_editar.setEditable(True)
        self.combobox_editar.setObjectName("combobox_editar")
        # self.combobox_editar.addItem("")
        # self.combobox_editar.addItem("")
        # self.combobox_editar.addItem("")
        # self.combobox_editar.addItem("")
        self.horizontalLayout.addWidget(self.combobox_editar)
        spacerItem6 = QtWidgets.QSpacerItem(46, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.boton_previo = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_previo.sizePolicy().hasHeightForWidth())
        self.boton_previo.setSizePolicy(sizePolicy)
        self.boton_previo.setMinimumSize(QtCore.QSize(30, 30))
        self.boton_previo.setObjectName("boton_previo")
        self.horizontalLayout_2.addWidget(self.boton_previo)
        self.boton_siguiente = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_siguiente.sizePolicy().hasHeightForWidth())
        self.boton_siguiente.setSizePolicy(sizePolicy)
        self.boton_siguiente.setMinimumSize(QtCore.QSize(30, 30))
        self.boton_siguiente.setObjectName("boton_siguiente")
        self.horizontalLayout_2.addWidget(self.boton_siguiente)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(60, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.boton_borrar = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_borrar.sizePolicy().hasHeightForWidth())
        self.boton_borrar.setSizePolicy(sizePolicy)
        self.boton_borrar.setMinimumSize(QtCore.QSize(0, 30))
        self.boton_borrar.setObjectName("boton_borrar")
        self.horizontalLayout.addWidget(self.boton_borrar)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame_edicion = QtWidgets.QGraphicsView(self.centralwidget)
        self.frame_edicion.setObjectName("frame_edicion")
        self.verticalLayout.addWidget(self.frame_edicion)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(MainWindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 1083, 26))
        self.menu.setObjectName("menu")
        self.menuMen = QtWidgets.QMenu(self.menu)
        self.menuMen.setObjectName("menuMen")
        self.menuEdici_n = QtWidgets.QMenu(self.menu)
        self.menuEdici_n.setObjectName("menuEdici_n")
        self.menuAyuda = QtWidgets.QMenu(self.menu)
        self.menuAyuda.setObjectName("menuAyuda")
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
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuMen.addAction(self.actionAbrir_Carpeta)
        self.menuMen.addAction(self.actionAbrir_Imagen)
        self.menuEdici_n.addAction(self.actionGuardar)
        self.menuAyuda.addAction(self.actionManual)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menu.addAction(self.menuMen.menuAction())
        self.menu.addAction(self.menuEdici_n.menuAction())
        self.menu.addAction(self.menuAyuda.menuAction())
        self.frame_edicion.setMouseTracking(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_zoom.setText(_translate("MainWindow", "Zoom"))
        self.label_segmentos.setText(_translate("MainWindow", "Segmentos"))
        self.label_puntos.setText(_translate("MainWindow", "Puntos"))
        self.boton_editar.setText(_translate("MainWindow", "Editar"))
        # self.combobox_editar.setItemText(0, _translate("MainWindow", "A"))
        # self.combobox_editar.setItemText(1, _translate("MainWindow", "B"))
        # self.combobox_editar.setItemText(2, _translate("MainWindow", "V"))
        # self.combobox_editar.setItemText(3, _translate("MainWindow", "D"))
        self.boton_previo.setText(_translate("MainWindow", "<-"))
        self.boton_siguiente.setText(_translate("MainWindow", "->"))
        self.boton_borrar.setText(_translate("MainWindow", "DEL"))
        self.menuMen.setTitle(_translate("MainWindow", "Menú"))
        self.menuEdici_n.setTitle(_translate("MainWindow", "Edición"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAbrir_Carpeta.setText(_translate("MainWindow", "Abrir Carpeta"))
        self.actionAbrir_Imagen.setText(_translate("MainWindow", "Abrir Imagen"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de ..."))
