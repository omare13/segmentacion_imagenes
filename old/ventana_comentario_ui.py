# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_comentario.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_comentario(object):
    def setupUi(self, ventana_comentario):
        ventana_comentario.setObjectName("ventana_comentario")
        ventana_comentario.resize(543, 208)
        self.label_comentario = QtWidgets.QLabel(ventana_comentario)
        self.label_comentario.setGeometry(QtCore.QRect(30, 29, 71, 21))
        self.label_comentario.setObjectName("label_comentario")
        self.texto_comentario = QtWidgets.QPlainTextEdit(ventana_comentario)
        self.texto_comentario.setGeometry(QtCore.QRect(120, 30, 391, 101))
        self.texto_comentario.setObjectName("texto_comentario")
        self.botones_comentario = QtWidgets.QSplitter(ventana_comentario)
        self.botones_comentario.setGeometry(QtCore.QRect(180, 160, 186, 28))
        self.botones_comentario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botones_comentario.setFrameShadow(QtWidgets.QFrame.Plain)
        self.botones_comentario.setOrientation(QtCore.Qt.Horizontal)
        self.botones_comentario.setHandleWidth(20)
        self.botones_comentario.setObjectName("botones_comentario")
        self.boton_aceptar = QtWidgets.QPushButton(self.botones_comentario)
        self.boton_aceptar.setObjectName("boton_aceptar")
        self.boton_cancelar = QtWidgets.QPushButton(self.botones_comentario)
        self.boton_cancelar.setObjectName("boton_cancelar")

        self.retranslateUi(ventana_comentario)
        QtCore.QMetaObject.connectSlotsByName(ventana_comentario)

    def retranslateUi(self, ventana_comentario):
        _translate = QtCore.QCoreApplication.translate
        ventana_comentario.setWindowTitle(_translate("ventana_comentario", "Insertar Comentario"))
        self.label_comentario.setText(_translate("ventana_comentario", "Comentario"))
        self.boton_aceptar.setText(_translate("ventana_comentario", "Aceptar"))
        self.boton_cancelar.setText(_translate("ventana_comentario", "Cancelar"))


