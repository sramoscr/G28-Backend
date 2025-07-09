while True:
    print("\nMINI CALCULADORA")
    print("="*20)
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operacion (SUMA, RESTA, MULTIPLICACION, DIVISION): ")

    if operacion == "SUMA":
        resultado = primer_numero + segundo_numero
    elif operacion == "RESTA":
        resultadp = primer_numero - segundo_numero
    elif operacion == "MULTIPLICACION":
        resultado = primer_numero * segundo_numero
    elif operacion == "División":
        resultado = primer_numero * segundo_numero
    else:
        print("Operación incorrecta")
        continue # todo lo que lleva debajo, ya no lo ejecuta.
    
    print(f"El resultado es: {resultado}")
    
    #Tarea hacer un progrma que convierta divisas de soles a dólares.