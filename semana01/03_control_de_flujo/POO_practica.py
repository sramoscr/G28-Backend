class Vehiculo:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        """ Atributo privado """
        self.__privado = 0

    def encender(self):
        print(f"Encendiendo el vehículo {self.marca}...")
        print(self.__privado)
        self.__reiniciar()

    def apagar(self):
        print(f"Apagando el vehículo {self.marca}...")

    """ Encapsulamiento: tener métodos en privado, solo pueden usarse dentro de la misma clase """
    def __reiniciar(self):
        print(f"Reiniciando el vehículo {self.marca}")


""" Intanciación de clases """
vw = Vehiculo("Rojo", "VW", "Golf")
#print(vw.modelo)
#print(vw.__privado)

""" Herencia """
class Pickup(Vehiculo):
    def mostrar_marca(self):
        print(self.marca)

ford = Pickup("blanco", "Ford", "F150")
ford.mostrar_marca()
#print(ford.color)
#ford.encender()

""" Polimorfismo: dos objetos de diferentes clases pueden tener métodos con el mismo nombre, y ambos métodos pueden ser llamados con el mismo código, dando respuestas diferentes. """
toyota = Pickup(color="negro", marca="Toyota", modelo="Hilux")

def mostrar_marca(pickup):
    pickup.mostrar_marca()

mostrar_marca(toyota)

""" Abstracción: Consiste en enfocarse en los aspectos esenciales
de un objeto ignorando los detalles irrelevantes para su uso """