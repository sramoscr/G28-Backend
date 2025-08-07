import requests            # Librería más popular para pedir peticiones HTTP (páginas web / APIs)
from pprint import pprint  #Pretty Printer -> formatea la salida para obtener un resultado más bonito. 

def main():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    json = response.json() # Convierte los datos en formato JSON y los convierte en diccionario

    for user in json:
        if user["id"] == 2:
            break
        pprint(user)

if __name__ == "__main__":
    main()