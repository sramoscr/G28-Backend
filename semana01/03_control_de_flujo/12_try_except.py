def main():
    # Bloque try: Se ejecuta hasta que no se produce una excepción o error
    try:
        division = 10/0
        print("División: ", division)

    # Bloque except: Se ejecuta cuando se produce una excepción
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    except Exception as e:   #-> capturar sin poner el error específico, general.
        print("Exception:", e)

    #Bloque finally: Se ejecuta siempre que se ejecuta el bloque try
    finally:
        print("Completado")

def main2():
    try:
        usuario = {
        "nombre": "Carlos",
        "edad": 17
        }

        # Validamos que el usuario sea mayor de edad
        if usuario["edad"] < 18:
            raise Exception("Debes ser mayor de edad")
        print("Usuario válido")

    except Exception as e:
        print("Error:", e)
    


if __name__ == "__main__":
    main2()