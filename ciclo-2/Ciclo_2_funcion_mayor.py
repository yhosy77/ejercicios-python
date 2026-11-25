"""
Crea una función que devuelva el mayor de dos números.

Pruébala con mayor(3, 8) y mayor(10, 2).
Experimento: pon un print("hola") después del return, dentro de la función. Antes de correrlo, adivina: ¿se imprime o no? Luego compruébalo.

"""

def mayor(a,b):
    if a > b:
        return a
    else:
        return b

x = mayor(3,8)
print(x)
y = mayor(10,2)
print(y)
z = mayor(mayor(8,3),5)
print(z)
a = mayor(4,4)
print(a)