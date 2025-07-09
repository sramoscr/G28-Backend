""" Programación orientada a objetos """

class Vehiculo:
    color = "rojo"
    marca = "Audi"
    model = "A4"

    def __init__(self, color, marca, modelo): # -> atributos dinámicos, constructor.
        self.color = color
        self.marca = marca
        self.modelo = modelo


    def encender(self):
        print(f"Encendiendo el vehículo {self.marca}")
    
    def apagar(self):
        print(f"Apagando el vehículo {self.marca}")

vw = Vehiculo("rojo", "VW", "Golf")
print(vw.marca)
vw.encender()

honda = Vehiculo("azul", "Honda", "Civic")
print(honda.marca)
honda.encender()

mitsubishi = Vehiculo("verde", "Mitsubishi", "Eclipse")
print(mitsubishi.marca)
mitsubishi.encender()