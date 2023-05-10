import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal
from ventanasecundaria import VentanaSecundaria

# CODIGO CREADO POR MIGUEL VALLADARES
#
# No pude hacer que se muestre la informacion :(
# Pero algo pude hacer. Cuando le doy a guardar se muestra la ventana de informacion y se cierra al segundo 


class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)

        # Conectar el botón "Guardar" a la función guardar_mascota()
        self.pushButton.clicked.connect(self.guardar_mascota)
        
    
    def guardar_mascota(self):
        # Obtener la información de los componentes
        nombre = self.entrada_nombre.text()
        especie = self.entrada_especie.text()
        edad = int(self.entrada_edad.value())
        peso = float(self.entrada_peso.value())
        
        # Crear un objeto de clase Mascota
        mascota = Mascota(nombre, especie, edad, peso)
        
        # Mostrar la información de la mascota en la ventana secundaria
        ventana_secundaria = QtWidgets.QMainWindow()
        ui = VentanaSecundaria()
        ui.setupUi(ventana_secundaria)
        ui.label_2.setText(str(mascota))
        ventana_secundaria.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    vista = Ventana()
    vista.show()
    app.exec()