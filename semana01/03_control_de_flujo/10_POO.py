""" Programación orientada a objetos """

class Vehiculo:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        """ Atributos privados """
        self.__privado = 0

    def encender(self):
        print(f"Encendiendo el vehiculo {self.marca}...")
        print(self.__privado)
        self.__reiniciar()

    def apagar(self):
        print(f"Apagando el vehiculo {self.marca}...")

    """ Métodos privados (Encapsulamiento) """
    def __reiniciar(self):
        print(f"Reiniciando el vehículo {self.marca}...")

""" Instanciación de las clases """
vw = Vehiculo("rojo", "VW", "Golf")
print(vw.marca)
vw.encender()
#print(vw.__privado) # da error porque es un atributo privado
#vw.__reiniciar() # da error porque es un método privado

honda = Vehiculo("azul", "Honda", "Civic")
print(honda.marca)
honda.encender()

mitsubishi = Vehiculo("verde", "Mitsubishi", "Eclipse")
print(mitsubishi.marca)
mitsubishi.encender()


""" Herencia """
class Pickup(Vehiculo):
    def mostrar_marca(self):
        print(self.marca)

camioneta = Pickup("Rojo", "Ford", "Raptor")
print(camioneta.marca)

""" Polimorfismo """
toyota = Pickup(color="rojo", marca="Toyota", modelo="Hilux")

def mostrar_marca(pickup):
    pickup.nostrar_marca()

mostrar_marca(toyota)

""" Abstracción: Consiste en enfocarse en los aspectos esenciales
de un objeto ignorando los detalles irrelevantes para su uso """

