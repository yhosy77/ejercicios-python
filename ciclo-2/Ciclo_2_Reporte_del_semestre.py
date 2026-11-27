def promedio(lista):
    suma = 0
    for nota in lista:
        suma += nota
    return round(suma / len(lista), 2)

def estado(nota):
    if nota >= 3:
        return "aprobada"
    else:
        return "perdida"

def reporte(notas):
    for materia,calificaciones in notas.items():
        nota = promedio(calificaciones)
        resultado = estado(nota)
        print(f"{materia}: {nota} ({resultado})")

notas = {
    "Cálculo": [3.5, 4, 4.5],
    "Fisica": [2.8, 3.2, 2.5],
    "POO": [4.5, 4.8]
}

reporte(notas)