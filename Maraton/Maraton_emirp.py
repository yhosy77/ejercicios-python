"""
Un numero primo es el que solo se puede dividir por si mismo y por uno.
un emirp (en español seria omirp) es un numero primo que al reves tambien es primo
ej: 17 es primo y al reves 71 es primo entonces es un emirp 
Hacer un programa que verifique si un numero  es primo o es emirp o no es primo
"""

def primo(n):
    if n == 1:
        return False
    N = int(n/2)
    for i in range(2,N + 1):
        if n % i == 0:
            return False
    return True

while True:
    x = input("Digite un numero (entero) para saber si es primo o no: ")
    try:
        x = int(x)
    except ValueError:
        print("Debes ingresar un numero entero")
        continue
    if x <= 0:
        print("El numero debe ser positivo y diferente a 0")
        continue
    break


es_primo = primo(x)
inverso = []
numero = x
if es_primo:
    while numero != 0:
        inverso.append(str(numero % 10))
        numero = numero // 10
    resultado = "".join(inverso)
    resultado = int(resultado)
    es_emirp = primo(resultado)
    if es_emirp:
        if resultado == x:
            print(f"El numero {x} es primo y palindromo")
        else:
            print(f"El numero {x} es emirp")
    else:
        print(f"El numero {x} es primo")
else:
    print(f"El numero {x} no es primo")