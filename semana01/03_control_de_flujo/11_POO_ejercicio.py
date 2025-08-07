""" Crear un programa que simule um cajero automático 
Deberá tener un menú con las siguientes opciones
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar saldo disponible
Iniciar con un saldo de $1000.00 """

import time
import os

class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo
        
    def ingresar_saldo(self, monto):
        if monto <= 0:
            print("\nMonto incorrecto")
            return
        self.saldo += monto
        print("\nDepósito exitoso")
        self.mostrar_saldo()

    def retirar_saldo(self, monto):
        if monto <= 0:
            print("\nMonto incorrecto")
            return
        
        if monto > self.saldo:
            print("\nSaldo insuficiente")
            return
        self.saldo -= monto
        print("\nRetiro exitoso")
        self.mostrar_saldo()
    
    def mostrar_saldo(self):
        print(f"\nSaldo disponible: {self.saldo}")

def main():
    cajero_bcp = Cajero(saldo=1000)
    condicion = True
    while condicion:
        print(""" 
        =====================================
                Cajero - Automático
        =====================================
            [1] Ingresar dinero en la cuenta
            [2] Retirar dinero de la cuenta
            [3] Mostrar saldo disponible 
            [4] Salir
        =====================================
        """)

        opcion = int(input("Ingrese la opción deseada: "))
    
        if opcion == 1:
            monto = float(input("Ingrese el monto a depositar: "))
            cajero_bcp.ingresar_saldo(monto)
            time.sleep(5)
        
        elif opcion == 2:
            monto = float(input("Ingrese el monto a retirar: "))
            cajero_bcp.retirar_saldo(monto)
            time.sleep(5)

        elif opcion == 3:
            cajero_bcp.mostrar_saldo()
            time.sleep(5)
        
        elif opcion == 4:
            print("Gracias por visitarnos")
            time.sleep(2)
            break

        else:
            print("Opción incorrecta 🙂")

        time.sleep(2)  
        os.system("cls")
        os.system("clear")

if __name__ == "__main__":
    main()
