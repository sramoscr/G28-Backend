""" Crear un programa que simule el funcionamiento de un cajero automático.
Deberá tener un menú con las siguientes opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar saldo disponible
Iniciar con un saldo de $1000.00 """

import os
import time

class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar_saldo(self, monto):
        if monto <= 0:
            print("Monto incorrecto")
            return
        self.saldo += monto
        print("Depósito exitoso")
        self.mostrar_saldo()
        time.sleep(4)

    def retirar_saldo(self, monto):
        if monto <= 0:
            print("Monto incorrecto")
            return
        if monto > self.saldo:
            print("Saldo insuficiente")
            return 
        self.saldo -= monto
        print("Retiro Exitoso")
        self.mostrar_saldo()
        time.sleep(4)
         
    def mostrar_saldo(self):
        print(f"\nTu saldo actual es {self.saldo}")
        time.sleep(4)

def main():
    cajero_bcp = Cajero(saldo=1000)

    while True:
        print("\n\n1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo disponible")
        print("4. Salir\n")

        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            monto = float(input("Ingresa el monto a depositar: "))
            cajero_bcp.ingresar_saldo(monto)
        elif opcion == 2:
            monto = float(input("Ingresa el monto a depositar: "))
            cajero_bcp.retirar_saldo()
            time.sleep(4)
        elif opcion == 3:
            cajero_bcp.mostrar_saldo()
        elif opcion == 4:
            print("Gracias por visitarnos...")
            time.sleep(2)
            os.system("cls")
            os.system("clear")
            break
        else: 
            print("Opción incorrecta")
            time.sleep(2)


if __name__ == "__main__":
    main()