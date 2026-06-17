from validaciones import pedir_texto
from datos import mostrar_paises


def buscar_pais(paises):
    """
    Busca países por nombre, permitiendo coincidencia parcial o exacta.
    """

    print("\n----- BUSCAR PAIS -----")

    nombre_buscado = pedir_texto("Ingrese el nombre o parte del nombre del pais: ")

    resultados = []

    for pais in paises:
        if nombre_buscado.lower() in pais["nombre"].lower(): # permite coincidencia parcial, ignorando mayúsculas/minúsculas
            resultados.append(pais) # si el país coincide con el criterio de búsqueda, lo agregamos a la lista de resultados

    if len(resultados) == 0:
        print("No se encontraron paises con ese criterio de busqueda.")
    else:
        print("\nResultados encontrados:")
        mostrar_paises(resultados) # muestra la lista de países encontrados, formateando números con puntos.