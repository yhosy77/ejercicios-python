"""
Un menú que se repite: 1. Agregar 2. Eliminar 3. Ver lista 4. Salir.

"""

menu = []

while True:
    x = input("Elige tu menu, selecciona el numero que represente la accion que quieras realizar: 1. Agregar 2. Eliminar 3. Ver lista 4. Salir. : ")
    match x:
        case "1":
            agregar = input("Selecciona que quieres agregar a tu menu(puedes repetir opciones): ")
            menu.append(agregar)
            print("se agrego:",agregar,"al menu")
        case "2":
            remover = input("Escribe el elemento que quieras eliminar de tu lista: ")
            try: 
                menu.remove(remover)
                print("se elimino:",remover,"del menu")
            except ValueError:
                print("Porfavor selecciona un elemento que este dentro de la lista")
        case "3":
            print("Tu menu actual es: ", menu)
        case "4":
            print("Tu menu es termino asi: ", menu)
            break
        case _:
            print("Porfavor selecciona una opcion valida")
    