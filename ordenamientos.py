from datos import mostrar_paises


def obtener_nombre(pais):
    """
    Devuelve el nombre del pais para usarlo como criterio de ordenamiento.
    """
    return pais["nombre"].lower()


def obtener_poblacion(pais):
    """
    Devuelve la poblacion del pais para usarla como criterio de ordenamiento.
    """
    return pais["poblacion"]


def obtener_superficie(pais):
    """
    Devuelve la superficie del pais para usarla como criterio de ordenamiento.
    """
    return pais["superficie"]


def ordenar_paises(paises):
    """
    Permite ordenar la lista de paises por nombre, poblacion o superficie,
    en forma ascendente o descendente.
    """

    if len(paises) == 0:
        print("No hay paises cargados para ordenar.")
        return

    while True:
        print("\n========== MENU DE ORDENAMIENTOS ==========")
        print("1. Ordenar por nombre")
        print("2. Ordenar por poblacion")
        print("3. Ordenar por superficie")
        print("4. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "4": # vuelve al menú principal, saliendo del bucle de ordenamientos.
            break

        if opcion not in ["1", "2", "3"]: # si la opción no es válida, mostramos un mensaje de error y volvemos a mostrar el menú.
            print("Error: opcion invalida.")
            continue # si la opción es válida, seguimos con el proceso de ordenamiento.

        print("\nTipo de orden:")
        print("1. Ascendente")
        print("2. Descendente")

        tipo_orden = input("Seleccione una opcion: ")

        if tipo_orden == "1":
            descendente = False # si el usuario elige orden ascendente, la variable descendente se establece en False para que la función sorted ordene de menor a mayor.
        elif tipo_orden == "2":
            descendente = True # si el usuario elige orden descendente, la variable descendente se establece en True para que la función sorted ordene de mayor a menor.
        else:
            print("Error: opcion invalida.")
            continue # si el tipo de orden no es válido, mostramos un mensaje de error y volvemos a mostrar el menú de ordenamientos.

        if opcion == "1": # si el usuario elige ordenar por nombre, usamos la función obtener_nombre como clave para ordenar la lista de países, y pasamos el valor de descendente para determinar el orden.
            paises_ordenados = sorted(
                paises,
                key=obtener_nombre,
                reverse=descendente
            )

        elif opcion == "2": # si el usuario elige ordenar por población, usamos la función obtener_poblacion como clave para ordenar la lista de países, y pasamos el valor de descendente para determinar el orden.
            paises_ordenados = sorted(
                paises,
                key=obtener_poblacion,
                reverse=descendente
            )

        elif opcion == "3": # si el usuario elige ordenar por superficie, usamos la función obtener_superficie como clave para ordenar la lista de países, y pasamos el valor de descendente para determinar el orden.
            paises_ordenados = sorted(
                paises,
                key=obtener_superficie,
                reverse=descendente
            )

        print("\n----- PAISES ORDENADOS -----")
        mostrar_paises(paises_ordenados) # muestra la lista de países ordenados, formateando números con puntos. No modifica la lista original en memoria.