import csv  # módulo para leer y escribir archivos CSV
from validaciones import pedir_texto, pedir_entero_positivo  # funciones para pedir datos seguros al usuario

def cargar_paises_desde_csv(nombre_archivo):
    """
    Lee los datos de países desde un archivo CSV.
    Devuelve una lista de diccionarios.
    """

    paises = []  # aquí guardaremos cada país cargado desde el archivo

    try:
        # Abrimos el archivo en modo lectura y con codificación UTF-8
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Cada fila del CSV se convierte en un diccionario
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)  # agregamos el país convertido a la lista

                except ValueError:
                    # Si algún dato numérico no se puede convertir, avisamos y seguimos
                    print("Error: hay un dato numerico invalido en el CSV.")

                except KeyError:
                    # Si faltan columnas esperadas, devolvemos lista vacía
                    print("Error: el CSV no tiene las columnas esperadas.")
                    return []

    except FileNotFoundError:
        # Si el archivo no existe, devolvemos lista vacía
        print("Error: no se encontro el archivo CSV.")
        return []

    return paises

def formatear_numero(numero):
    """
    Formatea un numero entero con puntos como separadores de miles.
    Ejemplo: 1234567 -> 1.234.567
    """
    return f"{numero:,}".replace(",", ".")


def mostrar_paises(paises):
    """
    Muestra todos los paises cargados en la lista.
    """

    if len(paises) == 0:
        print("No hay paises cargados.")
    else:
        print("\n----- LISTA DE PAISES -----")

        for pais in paises:
            print(f"Nombre: {pais['nombre']}")
            print(f"Poblacion: {formatear_numero(pais['poblacion'])}")
            print(f"Superficie: {formatear_numero(pais['superficie'])} km2")
            print(f"Continente: {pais['continente']}")
            print("--------------------------")

def agregar_pais(paises):
    """
    Agrega un país nuevo a la lista de países.
    Valida campos vacíos, valores numéricos correctos y evita países duplicados.
    Devuelve True si se agregó correctamente y False si no se agregó.
    """

    print("\n----- AGREGAR PAIS -----")

    nombre = pedir_texto("Ingrese nombre del pais: ")

    # Verificamos si el país ya existe, ignorando mayúsculas/minúsculas
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: el pais ya se encuentra cargado.")
            return False

    # Pedimos datos numéricos usando validación segura
    poblacion = pedir_entero_positivo("Ingrese poblacion: ")
    superficie = pedir_entero_positivo("Ingrese superficie en km2: ")
    continente = pedir_texto("Ingrese continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)  # agregamos el país a la lista en memoria

    print("Pais agregado correctamente.")
    return True

def actualizar_pais(paises):
    """
    Actualiza la población y la superficie de un país existente.
    Devuelve True si se actualizó correctamente y False si no se encontró.
    """

    print("\n----- ACTUALIZAR PAIS -----")

    nombre_buscado = pedir_texto("Ingrese el nombre del pais a actualizar: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre_buscado.lower():
            print("\nPais encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Poblacion actual: {formatear_numero(pais['poblacion'])}")
            print(f"Superficie actual: {formatear_numero(pais['superficie'])} km2")

            nueva_poblacion = pedir_entero_positivo("Ingrese nueva poblacion: ")
            nueva_superficie = pedir_entero_positivo("Ingrese nueva superficie en km2: ")

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("Datos del pais actualizados correctamente.")
            return True

    # Si no encontramos el país, informamos al usuario
    print("Error: no se encontro un pais con ese nombre.")
    return False

def guardar_paises_en_csv(nombre_archivo, paises):
    """
    Guarda la lista de países en el archivo CSV.
    """

    try:
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]

            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)  # escribimos todas las filas de la lista

        print("Cambios guardados correctamente en el archivo CSV.")

    except Exception as error:
        # Cualquier error al guardar se muestra por pantalla
        print(f"Error al guardar los datos en el CSV: {error}")