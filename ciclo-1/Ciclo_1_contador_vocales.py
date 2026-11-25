"""
Dada una frase, cuenta cuántas vocales tiene y cuántas palabras.

Frase: "Estoy aprendiendo Python en La Sabana"
Vocales: 13
Palabras: 6

"""

frase = input("Digite una frase: ")
conteo = frase.lower()

verificacion = "aeiou"
vocales = 0

for letras in conteo:
    if letras in verificacion:
        vocales += 1

print("La frase tiene: ", vocales, " vocales")
print("La frase tiene: ", len(frase.split()), " palabras")