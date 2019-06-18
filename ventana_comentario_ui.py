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
        ventana_comentario.resize(561, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventana_comentario.sizePolicy().hasHeightForWidth())
        ventana_comentario.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(ventana_comentario)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.formLayout.setVerticalSpacing(22)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ventana_comentario)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(ventana_comentario)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_comentario = QtWidgets.QLabel(ventana_comentario)
        self.label_comentario.setObjectName("label_comentario")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_comentario)
        self.texto_comentario = QtWidgets.QPlainTextEdit(ventana_comentario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto_comentario.sizePolicy().hasHeightForWidth())
        self.texto_comentario.setSizePolicy(sizePolicy)
        self.texto_comentario.setObjectName("texto_comentario")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.texto_comentario)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.botones_comentario = QtWidgets.QSplitter(ventana_comentario)
        self.botones_comentario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botones_comentario.setFrameShadow(QtWidgets.QFrame.Plain)
        self.botones_comentario.setOrientation(QtCore.Qt.Horizontal)
        self.botones_comentario.setHandleWidth(20)
        self.botones_comentario.setObjectName("botones_comentario")
        self.boton_aceptar = QtWidgets.QPushButton(self.botones_comentario)
        self.boton_aceptar.setObjectName("boton_aceptar")
        self.boton_cancelar = QtWidgets.QPushButton(self.botones_comentario)
        self.boton_cancelar.setObjectName("boton_cancelar")
        self.horizontalLayout.addWidget(self.botones_comentario)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ventana_comentario)
        QtCore.QMetaObject.connectSlotsByName(ventana_comentario)

    def retranslateUi(self, ventana_comentario):
        _translate = QtCore.QCoreApplication.translate
        ventana_comentario.setWindowTitle(_translate("ventana_comentario", "Insertar Comentario"))
        self.label.setText(_translate("ventana_comentario", "Título"))
        self.label_comentario.setText(_translate("ventana_comentario", "Comentario"))
        self.boton_aceptar.setText(_translate("ventana_comentario", "Aceptar"))
        self.boton_cancelar.setText(_translate("ventana_comentario", "Cancelar"))
