""" Strings en Python """   
texto = "python 🐍 es un lenguaje de programación muy potente"

""" Recorrer un string """
for caracter in texto:
    print(caracter)

""" Concatenar strings """
texto_concatenado = texto + " y facil de aprender"
print(texto_concatenado)

""" Formatear strings """
nombre = "pepito"
edad = 30
saludo = "Hola {}, tu edad es {} años".format(nombre, edad) #forma 1
print(saludo)
segundo_saludo = f"Hola {nombre}, tu edad es {edad} años" #forma 2 - RECOMENDADA
print(segundo_saludo)
tercer_saludo = "Hola %s, tu edad es %d años" % (nombre, edad) #forma 3
print(tercer_saludo)

""" Métodos de strings """
# .upper()
print("upper()", texto.upper()) #Todo a mayúscula

print("lower()", texto.lower()) #Todo a minúscula

print("capitalize()", texto.capitalize()) #Primer caracter en mayúscula

print("count()", texto.count("pyhton")) #cuantas veces se repite "python"

print("replace()", texto.replace("python", "Rust")) # Reemplaza Python por Rust.

print("split()", texto.split(" ")) # separa cada palabra y devuelve una lista.

print("join()", texto.join(" ")) # Lo contrario a split

print("strip()", texto.strip()) # Elimina espacios al inicio y al final








# SUBIR TU PROYECTO A UN REPOSITORIO DE GITHUB
# abrir terminal dentro de tu carpeta padre
# abres terminal -> git init (se crea carpeta invisible)
# git add . / git add --all / git add "carpetaespecifica" (se agrega todo lo que es)
# git commit -m "firts commit"

# git branch -M main (establecer conexión con repo de la web)

# git remote add origin "ruta de la repo" (enter y lo sube)

# git push -u origin main