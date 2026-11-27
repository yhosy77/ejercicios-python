frase = "el perro y el gato y el loro"
resultado = {}
palabras = frase.split()

for palabra in palabras:
    if palabra in resultado:
        resultado[palabra] += 1
    else:
        resultado[palabra] = 1

print(resultado)