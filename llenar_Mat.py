import math
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QApplication, QLineEdit, QDialog, \
    QDialogButtonBox, QVBoxLayout, QPushButton, QWidget, QButtonGroup, QScrollArea, QGridLayout, QHBoxLayout, QComboBox


class Ventana2(QMainWindow):
    def __init__(self, anterior, columnas, filas):
        super(Ventana2, self).__init__(anterior)

        self.columnas = columnas
        self.filas = filas
        self.ventanaAnterior = anterior
        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: white;")
        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.setStyleSheet("background-color: black;")

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.interna = QWidget()
        self.interna.setContentsMargins(20, 20, 20, 20)

        self.setCentralWidget(self.interna)

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("LLENE LA MATRIZ")

        self.letrero1.setFont(QFont("Waree", 20))

        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background-color: #FFFFFF; color: #000000; padding: 5px;"
                                    "border:solid; border-width:2px; border-color: #FFFFFF;"
                                    "border-radius: 15px; margin-bottom: 10px;")
        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()

        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)
        self.vertical.addWidget(self.scrollArea)

        self.numeroElementos = self.filas * self.columnas

        self.contador = 0

        self.elementosPorColumna = self.filas

        self.numeroFilas = self.filas

        self.interna.setLayout(self.vertical)

        self.botones = QButtonGroup()

        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas + 1):
            for columna in range(1, self.elementosPorColumna + 1):
                if self.contador < self.numeroElementos:
                    self.ventanaAux = QWidget()
                    self.ventanaAux.setFixedHeight(200)
                    self.ventanaAux.setFixedWidth(200)

                    self.verticalCuadricula = QVBoxLayout()
                    #self.verticalCuadricula(Qt.AlignCenter)

                    self.verticalCuadricula.addStretch()

                    self.labelNombre = QLabel('Item n. ' + str(self.contador + 1))

                    self.labelNombre.setStyleSheet("color: white; font-size: 20px; font-family: Warre;")
                    #self.self.labelNombre(Qt.AlignCenter)
                    self.verticalCuadricula.addWidget(self.labelNombre)

                    self.verticalCuadricula.addStretch()

                    self.ventanaAux.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accion_boton)

    def metodo_accion_boton(self, idBoton):
        print(idBoton)
