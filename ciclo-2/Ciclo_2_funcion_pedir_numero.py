"""
Usa mensaje como el texto del input.
Si el usuario escribe algo que no es número, muestra un aviso y vuelve a preguntar.
Cuando sea válido, lo devuelve.

"""

def mayor(a,b):
    if a > b:
        return a
    else: 
        return b

def pedir_numero(mensaje):
    while True:
        respuesta = input(mensaje)
        try:
            respuesta = int(respuesta)
            return respuesta
        except ValueError:
            print("Digite un numero")
            continue


a = pedir_numero("Primer numero: ")
b = pedir_numero("Segundo numero: ")
print(mayor(a,b))