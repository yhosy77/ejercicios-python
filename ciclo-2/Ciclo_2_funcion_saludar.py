"""
Crea una función que devuelva el texto "Hola, " seguido del nombre.

Sin input dentro de la función.
Fuera de ella, úsala dos veces con nombres escritos en el código, e imprime lo que devuelve.

Idea clave: el parámetro es lo que le entregas a la función cuando la llamas.

"""

def saludar (nombre):
    x = f"hola {nombre}"
    return x

print(saludar("Pepito"))
print(saludar("Lisa"))
print("")
print(saludar(input("Ingresa tu nombre: ")))

