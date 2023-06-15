import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QApplication, QLineEdit, QDialog, \
    QDialogButtonBox, QVBoxLayout, QPushButton, QWidget, QButtonGroup, QScrollArea, QGridLayout, QHBoxLayout, QComboBox

from llenar_Mat import Ventana2


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)

        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: black;")
        self.ancho = 600
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.interna = QWidget()
        self.interna.setContentsMargins(50, 50, 50, 50)

        self.setCentralWidget(self.interna)
        self.vertical = QVBoxLayout()

        self.cuadricula = QGridLayout()
        self.interna.setLayout(self.cuadricula)

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)
        # Creamos el boton de aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)
        self.ventanaDialogo.setWindowTitle("HELP TRAINING")
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("imagenes/img_1.png"))

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilo al label mensaje:
        self.mensaje.setStyleSheet(
            "background-color: #000000; color: #FFFFFF; font-size: 18px; font-family: Poppins; padding: 8px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana de dialogo:
        self.ventanaDialogo.setLayout(self.vertical)


        self.label = QLabel("Bienvenido usuario")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")
        self.cuadricula.addWidget(self.label, 0, 0, 1, 3)

        self.filas_label = QtWidgets.QLabel('Ingrese el número de\nfilas (entre 4 y 22)')
        self.filas_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.filas_label, 1, 0)

        self.filas_edit = QtWidgets.QLineEdit(self)
        self.filas_edit.setFixedWidth(250)
        self.filas_edit.setFixedHeight(50)
        self.filas_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.filas_edit, 1, 1)

        self.columna_label = QtWidgets.QLabel('Ingrese el número de\ncolumnas (entre 4 y 22)')
        self.columna_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.columna_label, 2, 0)

        self.columna_label = QtWidgets.QLabel('')
        self.columna_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.columna_label, 3, 0)

        self.columna_edit = QtWidgets.QLineEdit(self)
        self.columna_edit.setFixedWidth(250)
        self.columna_edit.setFixedHeight(50)
        self.columna_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.columna_edit, 2, 1)

        self.botonAceptar = QPushButton("Continuar")
        self.botonAceptar.setFixedWidth(250)
        self.botonAceptar.setFixedHeight(50)
        self.botonAceptar.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.botonAceptar.clicked.connect(self.aceptar)
        self.cuadricula.addWidget(self.botonAceptar, 4, 0)

    def aceptar(self):

        if (self.columna_edit.text() == ''):
            self.mensaje.setText("Debe ingresar número de columnas válidas.")
            self.ventanaDialogo.exec_()
            self.datosCorrectos = False
        elif (self.filas_edit.text() == ''):
            self.mensaje.setText("Debe ingresar número de filas válidas.")
            self.ventanaDialogo.exec_()
            self.datosCorrectos = False
        else:
            columnas = int(self.columna_edit.text())
            # columnas = int(col)
            filas = int(self.filas_edit.text())
            # filas = int(fil)

            if (filas < 4 or filas > 22):
                self.mensaje.setText("Debe ingresar número de filas válidas.")
                self.ventanaDialogo.exec_()
                self.datosCorrectos = False

            if (columnas < 4 or columnas > 22):
                self.mensaje.setText("Debe ingresar número de columnas válidas.")
                self.ventanaDialogo.exec_()
                self.datosCorrectos = False
            else:
                self.datosCorrectos = True
                self.llenar_Mat = Ventana2(self, columnas, filas)
                self.llenar_Mat.show()
                self.hide()









if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())