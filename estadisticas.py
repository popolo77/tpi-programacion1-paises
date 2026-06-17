from datos import formatear_numero

from datos import formatear_numero


def mostrar_estadisticas(paises):
    """
    Muestra estadísticas generales sobre los países cargados.
    """

    if len(paises) == 0:
        print("No hay paises cargados para calcular estadisticas.")
        return

    pais_mayor_poblacion = paises[0] # inicializamos la variable pais_mayor_poblacion con el primer país de la lista para compararlo con los demás países y encontrar el país con mayor población.
    pais_menor_poblacion = paises[0]    # inicializamos la variable pais_menor_poblacion con el primer país de la lista para compararlo con los demás países y encontrar el país con menor población.

    suma_poblacion = 0 
    suma_superficie = 0

    cantidad_por_continente = {} # diccionario para contar la cantidad de países por continente, donde la clave es el nombre del continente y el valor es la cantidad de países que pertenecen a ese continente.

    for pais in paises:
        suma_poblacion += pais["poblacion"] # sumamos la población de cada país a la variable suma_poblacion para calcular el total de población de todos los países.
        suma_superficie += pais["superficie"]

        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]: # si la población del país actual es mayor que la población del país almacenado en pais_mayor_poblacion, actualizamos la variable pais_mayor_poblacion para que apunte al país actual, ya que ahora es el país con mayor población encontrado hasta el momento.
            pais_mayor_poblacion = pais

        if pais["poblacion"] < pais_menor_poblacion["poblacion"]: # si la población del país actual es menor que la población del país almacenado en pais_menor_poblacion, actualizamos la variable pais_menor_poblacion para que apunte al país actual, ya que ahora es el país con menor población encontrado hasta el momento.
            pais_menor_poblacion = pais

        continente = pais["continente"] # obtenemos el continente del país actual para contar la cantidad de países por continente. Si el continente ya existe como clave en el diccionario cantidad_por_continente, incrementamos su valor en 1. Si el continente no existe como clave, lo agregamos al diccionario con un valor inicial de 1, indicando que hemos encontrado un país perteneciente a ese continente. Al finalizar el bucle, tendremos un conteo de cuántos países pertenecen a cada continente.

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\n========== ESTADISTICAS ==========")

    print("\nPais con mayor poblacion:")
    print(
        f"{pais_mayor_poblacion['nombre']} - "
        f"{formatear_numero(pais_mayor_poblacion['poblacion'])} habitantes"
    )

    print("\nPais con menor poblacion:")
    print(
        f"{pais_menor_poblacion['nombre']} - "
        f"{formatear_numero(pais_menor_poblacion['poblacion'])} habitantes"
    )

    print("\nPromedio de poblacion:")
    print(f"{formatear_numero(int(promedio_poblacion))} habitantes")

    print("\nPromedio de superficie:")
    print(f"{formatear_numero(int(promedio_superficie))} km2")

    print("\nCantidad de paises por continente:")
    for continente, cantidad in cantidad_por_continente.items():
        print(f"{continente}: {cantidad}")