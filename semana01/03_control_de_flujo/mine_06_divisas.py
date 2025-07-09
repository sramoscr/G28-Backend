while True:
    print("="*20)
    print("MAQUINA DE CAMBIOS")
    print("="*20)
    divisa = int(input("Ingresa tu divisa:\nSoles...[1]\nDólares.[2]\n-> "))
    simbolo =  " "

    if divisa == 1:
        cantidad = int(input("Ingresa la cantidad en soles: \n->"))
        cambio = round(cantidad / 3.54, 2)
        simbolo = "$"

    elif divisa == 2:
        cantidad = int(input("Ingresa la cantidad dólares: \n->"))
        cambio = round(cantidad * 3.54, 2)
        simbolo = "s/."
    else: 
        print("Ingresaste una opción errónea, vuelve a intentarlo 😷.\n")
        continue

    print("="*20)
    print(f"El cambio es: {cambio},{simbolo}")
    print("="*20)