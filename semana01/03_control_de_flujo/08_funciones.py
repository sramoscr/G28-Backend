def suma(a, b):
    c = a + b
    return c
operando = suma(1, 2)
print(operando)

""" Funciones con argumentos arbitrarios """
def suma_arbitrarios(*args):
    print(args)

suma_arbitrarios(1, "dos", True)

""" Función con argumentos con clave """
def suma_clave(a, b, c=0):
    return a + b + c

print(suma_clave(a=3, b=5))

""" Función con argumentos arbitrarios y con clave """
def suma_arbitrarios_clave(**kwargs):
    print(kwargs)
    print(kwargs["a"])

suma_arbitrarios_clave(a=1, b=2, c=3)