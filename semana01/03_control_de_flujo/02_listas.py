""" Listas en Python """
lista = ["Python", "Rust", "Go", "Typescript", "Javascript", "C++"]

""" Acceder a elementos """
print(lista[0])

""" Rango de elementos """
print(lista[0:3]) 
# 0: primer indice incluido (0)
# 3: primer indice excluido (3)

""" Acceso a rango de elementos con salto """
print(lista[0:4:2])
# 0 (inicio): primer indice incluido (0)
# 4 (fin): primer indice excluido (4)
# 2 (paso): toma cada 2 elementos

""" Acceso negativo """
print(lista[-1])

""" Acceso a rango desde el final/final """
print(lista[3:])

""" Agregar elementos """
lista.append("C#")

""" Eliminar elementos por índice """
lista.pop(0)

""" Eliminar elementos por valor """
lista.remove("Rust")

""" Eliminar todos los elementos """
lista.clear()

""" Invertir la lista """
lista.reverse()

""" Ordenar la lista """
lista.sort()


