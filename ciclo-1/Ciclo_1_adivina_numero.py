"""
El programa elige un número secreto del 1 al 20. 
Tú tienes 5 intentos para adivinarlo. 
Después de cada intento te dice “Más alto” o “Más bajo”. 
Si aciertas, muestra en cuántos intentos lo lograste. 
Si se acaban, revela el número.

"""

import random

print("Intenta adivinar un numero del 1-20, tienes 5 intentos")

x = random.randint(1, 20)
intentos = 0
ganar = False

while intentos < 5:
    jugada = input("DI un numero: ")
    while True:
        if jugada.isdigit():
            break
        print("Digina un numero valido")
        jugada = input("DI un numero: ")

    jugada = int(jugada)

    if jugada < 1 or jugada > 20:
        print("Debes digitar un numero entre 1-20")
        continue

    intentos += 1
    if jugada == x:
        ganar = True
        break
    if jugada < x:
        print("el numero esta mas arriba")
    else:
        print("el numero esta mas abajo")
    print("Intentos: ", intentos)



if ganar:
    print("Felicidades, Adivinaste el numero: ", x , " en ", intentos, " intentos")
else:
    print("No adivinaste el numero, era el: ", x)
