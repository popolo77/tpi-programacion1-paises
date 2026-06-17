from validaciones import pedir_texto, pedir_entero_positivo
from datos import mostrar_paises


def filtrar_por_continente(paises):
    """
    Filtra los paises segun el continente ingresado por el usuario.
    """

    print("\n----- FILTRAR POR CONTINENTE -----")

    continente = pedir_texto("Ingrese continente: ")

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises para ese continente.")
    else:
        mostrar_paises(resultados)


def filtrar_por_rango_poblacion(paises):
    """
    Filtra los paises cuya poblacion se encuentre dentro de un rango.
    """

    print("\n----- FILTRAR POR RANGO DE POBLACION -----")

    minimo = pedir_entero_positivo("Ingrese poblacion minima: ")
    maximo = pedir_entero_positivo("Ingrese poblacion maxima: ")

    if minimo > maximo:
        print("Error: la poblacion minima no puede ser mayor que la maxima.")
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo: # si la población del país está dentro del rango definido por el usuario, lo agregamos a la lista de resultados
            resultados.append(pais)

    if len(resultados) == 0: # si no se encontró ningún país dentro del rango de población, mostramos un mensaje indicando que no se encontraron resultados.
        print("No se encontraron paises dentro de ese rango de poblacion.")
    else:
        mostrar_paises(resultados) # muestra la lista de países encontrados, formateando números con puntos.


def filtrar_por_rango_superficie(paises):
    """
    Filtra los paises cuya superficie se encuentre dentro de un rango.
    """

    print("\n----- FILTRAR POR RANGO DE SUPERFICIE -----")

    minimo = pedir_entero_positivo("Ingrese superficie minima: ")
    maximo = pedir_entero_positivo("Ingrese superficie maxima: ")

    if minimo > maximo:
        print("Error: la superficie minima no puede ser mayor que la maxima.")
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises dentro de ese rango de superficie.")
    else:
        mostrar_paises(resultados)


def menu_filtros(paises):
    """
    Muestra el menu de filtros y ejecuta la opcion seleccionada.
    """

    while True:
        print("\n========== MENU DE FILTROS ==========")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de poblacion")
        print("3. Filtrar por rango de superficie")
        print("4. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            filtrar_por_continente(paises) # filtra los países por continente, pidiendo al usuario que ingrese el nombre del continente y mostrando los países que coincidan, sin modificar la lista original.

        elif opcion == "2":
            filtrar_por_rango_poblacion(paises) # filtra los países por rango de población, pidiendo al usuario que ingrese una población mínima y máxima, validando que la mínima no sea mayor que la máxima, y mostrando los países que tengan una población dentro de ese rango, sin modificar la lista original.

        elif opcion == "3":
            filtrar_por_rango_superficie(paises) # filtra los países por rango de superficie, pidiendo al usuario que ingrese una superficie mínima y máxima, validando que la mínima no sea mayor que la máxima, y mostrando los países que tengan una superficie dentro de ese rango, sin modificar la lista original.

        elif opcion == "4": 
            break # vuelve al menú principal, saliendo del bucle de filtros.

        else:
            print("Error: opcion invalida.")