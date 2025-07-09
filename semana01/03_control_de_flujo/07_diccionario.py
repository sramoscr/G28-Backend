usuario = {
    "id":1,
    "nombre": "Jhon Doe",
    "email": "jhon@gmail.com",
    "edad": 25,
    "estado": True
}
print(usuario)

""" Constructor de diccionarios """
usuario_2 = dict(id=2, nombre="Anna Doe", email="anna@gmail", edad=30, estado=False)
print(usuario_2)

""" Acceder a los valores de un diccionarios """
#print(usuario["apellidos"]) #si no lo encuentra, da error y rompe la ejecución del código.
print(usuario.get("apellidos", "No se encontro")) # devuelve None si no hay esa propiedad en el diccionario, le puedes poner mensaje o valor.

""" Cambiar el valor de un diccionario """
usuario["nombre"] = "Jhon Doe Jr"
usuario["genero"] = "Masculino"
print(usuario)

""" Eliminar un valor de un diccionario """
del usuario["genero"]
usuario.pop("edad")
print(usuario)

""" Métodos de diccionarios """
print(usuario.keys()) # devuelve un array de todas las claves
print(usuario.values()) # devuelve un array con los valores
print(usuario.items()) # devuelve un array con pares clave-valor dentro de una tupla

""" Iterar sobre un diccionario """
for key, value in usuario.items():
    print(f"{key}: {value}")

for key in usuario:
    print(f"{key}: {usuario[key]}")