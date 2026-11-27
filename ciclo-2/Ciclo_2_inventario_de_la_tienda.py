inventario = {
    "manzanas": 10,
    "peras": 0,
    "bananos": 5
}

print(inventario)
for producto,cantidad in inventario.items():
    if cantidad == 0:
        print(f"{producto}: {cantidad} (agotado)")
    else:
        print(f"{producto}: {cantidad}")

inventario["manzanas"] -= 3
inventario["uvas"] = 8
print(inventario)

peticion = input("Dime un producto para ver si esta en el inventario: ")
if peticion in inventario:
    print("Tu producto esta en el inventario")
else:
    print("El producto no esta en el inventario")