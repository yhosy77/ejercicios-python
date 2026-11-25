"""
Con un diccionario {"Cálculo integral": 4.1, "Física mecánica": 2.7, "POO": 4.5}, 
imprime cada materia con su nota y si la aprobó (≥ 3.0).

"""

boletin = {
    "Cálculo integral": 4.1,
    "Física mecánica": 2.7,
    "POO": 4.5
}

for materia,nota in boletin.items():
    if nota < 3:
        print("El estudiante reprobo:",materia,"Con:",nota)
    else: 
        print("El estudiante aprobo:",materia,"Con:",nota)