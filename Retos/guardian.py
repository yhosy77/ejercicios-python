contrasenas_comunes = ["123456", "password", "123456789", "qwerty", "12345678","111111", "abc123", "contraseña", "iloveyou", "admin"]

def evaluar_contrasena(contrasena):
    puntaje = 0 
    sugerencias = []
    if contrasena.lower() in contrasenas_comunes:
        return {"puntaje" : puntaje, "nivel":"muy débil", "sugerencias":["Es una contraseña comun, intenta con otra"]}
    
    if len(contrasena) >= 8:
        puntaje += 1
        if len(contrasena) >= 12:
            puntaje += 1
        else:
            x = 12 - len(contrasena)
            sugerencias.append(f"Tu contraseña deberia tener {x} mas caracteres")
    else:
        y = 8 - len(contrasena)
        sugerencias.append(f"Tu contraseña deberia tener {y} mas caracteres")

    mayuscula = False
    minuscula = False
    digito = False
    simbolo = False
    for caracter in contrasena:
        if caracter.isupper():
            mayuscula = True
        if caracter.islower():
            minuscula = True
        if caracter.isdigit():
            digito = True
        if not caracter.isalnum():
            simbolo = True

    if mayuscula:
        puntaje += 1
    else:
        sugerencias.append("La contraseña deberia tener al menos una mayuscula")

    if minuscula:
        puntaje += 1
    else:
        sugerencias.append("La contraseña deberia tener al menos una minuscula")

    if digito:
        puntaje += 1
    else:
        sugerencias.append("La contraseña deberia tener al menos un dígito")

    if simbolo:
        puntaje += 1
    else:
        sugerencias.append("La contraseña deberia tener al menos un simbolo")

    if puntaje <= 2:
        nivel = "débil"
    elif puntaje <= 4:
        nivel = "media"
    else:
        nivel = "fuerte"

    return {"puntaje": puntaje, "nivel": nivel, "sugerencias": sugerencias}

def main():
    while True:
        contrasena = input("Digite su contraseña para combrobar su nivel o digita salir para salir del programa: ")
        match contrasena:
            case "salir":
                break
            case _:
                respuesta = evaluar_contrasena(contrasena)
                print(f"Nivel: {respuesta["nivel"]} ({respuesta["puntaje"]}/6)")
                print("Sugerencias:")
                if len(respuesta["sugerencias"]) == 0:
                    print("No hay sugerencias, tu contraseña es fuerte")
                else:
                    for sugerencia in respuesta["sugerencias"]:
                        print(sugerencia)


assert evaluar_contrasena("123456")["nivel"] == "muy débil"
assert evaluar_contrasena("Password")["puntaje"] == 0
assert evaluar_contrasena("hola")["puntaje"] == 1
assert evaluar_contrasena("Bogota2026")["nivel"] == "media"
assert evaluar_contrasena("Bogota2026!")["puntaje"] == 5
assert evaluar_contrasena("Cafe#Sabana_2026")["nivel"] == "fuerte"
assert evaluar_contrasena("")["nivel"] == "débil"
print("Todas las pruebas pasaron")


main()