"""
Tienes a = 10, b = 3 y operacion = "*". 
Usa match para que el programa sume, reste, multiplique o divida según el valor de operacion. 
Si no es ninguna de las cuatro, imprime “Operación no válida”. 
Prueba cambiando operacion varias veces.

"""

a = input("Digite un numero: ")
while True:
    if a.isdigit():
        break
    print("Debes escribir un numero")
    a = input("Digite un numero: ")

b = input("Digite el segundo numero: ")
while True:
    if b.isdigit():
        break
    print("Debes escribir un numero")
    b = input("Digite un numero: ")

a = int(a)
b = int(b)
operacion = input("Digite la operacion que quieras hacer (+,-,*,/): ")


match operacion:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b == 0:
            print("No puedes dividir por 0")
        else: 
            print(a / b)
    case _:
        print("Operación no válida")
        