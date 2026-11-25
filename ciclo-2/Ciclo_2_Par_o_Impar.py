"""
Crea una función es_par(numero) que devuelva True o False. 
Úsala en un for del 1 al 10 para imprimir "3 es impar", "4 es par", etc.

"""


def es_par(i):
    if i % 2 == 0:
        return True
    return False

for i in range(1,11):
    x = es_par(i)
    if x:
        print("El numero:", i , "Es par")
    else:
        print("El numero:", i , "Es impar")