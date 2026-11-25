"""
1. Analizador de frase (strings)
Guarda una frase en una variable e imprime:

cuántos caracteres tiene
la frase en mayúsculas
su primera y su última letra
si contiene la palabra “python”, sin importar mayúsculas o minúsculas

"""
while True:
    frase = input("Ingrese una frase: ")
    if len(frase) > 0:
        break
    print("La frase no puede esatr vacia")

caracteres = len(frase)
print("La frase tiene", caracteres, "caracteres.")
print(frase.upper())
print("La primera letra de tu frase es: ", frase[0], " y la ultima es: ", frase[-1])
if "python" in frase.lower():
    print("La frase SI tiene la palabra python incluida")
else: 
    print("La frase NO tiene la palabra python incluida")

 