"""
Crea pedir_numero(mensaje): pide un número con input, valida con try/except ValueError, repite hasta que sea válido y lo devuelve. 
Úsala dos veces para pedir dos números e imprimir la suma.

"""

def pedir_numero(num):
    while num != 2:
        mensaje = input("Porfavor digita un numero: ")
        try:
            x = int(mensaje)
            num += 1
            return x
        except ValueError:
            print("Escribe solo numeros porfavor")
            continue

      
"""
suma = 0
num = 0

while num != 2:
    mensaje = input("Porfavor digita un numero: ")
    y = pedir_numero(mensaje)
    if y:
        suma += y
        num += 1
    else:
        continue    
"""
a = pedir_numero("Primer numero: ")
b = pedir_numero("Segundo numero: ")
print(a + b)