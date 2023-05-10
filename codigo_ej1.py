import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget

# CODIGO CREADO POR MIGUEL VALLADARES

class prueba(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Mi Aplicación para la prueba")
        self.setGeometry(100, 100, 600, 600)

        # Creación de los layouts
        disenho_pricipal = QVBoxLayout()
        parte_superior = QHBoxLayout()
        botones = QHBoxLayout()

        # Creación de componentes
        texto1 = QLabel("Texto 1")
        texto2 = QLabel("Texto 2")
        boton1 = QPushButton("Botón 1")
        boton2 = QPushButton("Botón 2")

        # Agregar componentes a los layouts
        parte_superior.addWidget(texto1)
        parte_superior.addWidget(texto2)
        botones.addWidget(boton1)
        botones.addWidget(boton2)

        # Agregar los layouts al layout principal
        disenho_pricipal.addLayout(parte_superior)
        disenho_pricipal.addLayout(botones)

        # Crear un widget central y establecer el layout principal
        widget_central = QWidget()
        widget_central.setLayout(disenho_pricipal)
        self.setCentralWidget(widget_central)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = prueba()
    window.show()
    sys.exit(app.exec())
