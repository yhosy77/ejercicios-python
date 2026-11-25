"""
Con un while, imprime los números del 1 al 30 excepto los múltiplos de 3. 
Al final, imprime la suma de los números que sí se imprimieron.

"""

x = 0
suma = 0

while x < 30 :
    x += 1
    if x % 3 == 0:
        continue
    print(x)
    suma += x

print()
print(suma)