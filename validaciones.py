def pedir_texto(mensaje):
    """
    Solicita un texto al usuario y valida que no esté vacío.
    """
    texto = input(mensaje).strip()

    while texto == "":
        print("Error: el campo no puede estar vacio.")
        texto = input(mensaje).strip()

    return texto


def pedir_entero_positivo(mensaje):
    """
    Solicita un número entero positivo y valida errores de ingreso.
    """
    while True:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("Error: el numero debe ser mayor que cero.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un numero entero valido.")