"""
El programa elige un número secreto del 1 al 20. 
Tú tienes 5 intentos para adivinarlo. 
Después de cada intento te dice “Más alto” o “Más bajo”. 
Si aciertas, muestra en cuántos intentos lo lograste. 
Si se acaban, revela el número.
"""

import random

adivinar = random.randint(1,20)
intentos = 0
ganar = False

while intentos < 5:
    x = input("Elige un numero entre 1-20: ")
    try:
        x = int(x)
    except ValueError:
        print("Debe ser un numero")
        continue

    if x < 1 or x > 20: 
        print("Porfavor selecciona un numero dentro de los parametros 1-20")
        continue

    intentos += 1
    if x == adivinar:
        ganar = True
        break
    if x < adivinar:
        print("el numero esta mas arriba")
    else: 
        print("el numero esta mas abajo")
    print("Intentos: ",intentos)
        

if ganar:
    print("Felicidades, ganaste con: ", intentos, "intentos")
else:
    print("Perdiste el numero era: ", adivinar)
