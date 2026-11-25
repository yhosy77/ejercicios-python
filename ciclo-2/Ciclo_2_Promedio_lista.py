"""
Con notas = [3.5, 4.2, 2.8, 4.8, 3.9]
crea una función promedio(lista) que devuelva el promedio (no que lo imprima). 
Luego imprime cuántas notas son menores a 3.0.

"""

def promedio (notas):
    Perdidas = 0
    suma = 0
    for nota in notas:
        suma += nota
        if nota < 3:
            Perdidas += 1
    prom = suma / len(notas)
    return prom , Perdidas

notas = [3.5, 4.2, 2.8, 4.8, 3.9, 2.0]
prom = promedio(notas)

print("La cantidad de materias perdidas (por debajo de 3) es:", prom[1])
