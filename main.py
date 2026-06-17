import os  # módulo estándar para trabajar con rutas y archivos del sistema operativo

# Los otros módulos (.py) se importan para usar sus funciones.
# Esto es lo que permite que main.py use código de datos.py, busquedas.py, etc.
from datos import cargar_paises_desde_csv, mostrar_paises, agregar_pais, actualizar_pais, guardar_paises_en_csv
from busquedas import buscar_pais
from filtros import menu_filtros
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    print("\n========== SISTEMA DE GESTION DE PAISES ==========")
    print("1. Mostrar paises")
    print("2. Agregar pais")
    print("3. Actualizar pais")
    print("4. Buscar pais")
    print("5. Filtrar paises")
    print("6. Ordenar paises")
    print("7. Mostrar estadisticas")
    print("8. Salir")


def main():
    # obtener la carpeta donde está este archivo main.py
    ruta_actual = os.path.dirname(__file__)

    # construir la ruta completa a paises.csv usando la carpeta del script
    # esto evita errores si el usuario ejecuta el programa desde otra carpeta
    ruta_csv = os.path.join(ruta_actual, "paises.csv")

    # cargar los datos desde el archivo CSV usando la ruta correcta
    paises = cargar_paises_desde_csv(ruta_csv)

    print("\nDatos cargados correctamente.")
    print(f"Paises cargados: {len(paises)}")

    # El programa ejecuta un menú en bucle para que el usuario elija qué hacer.
    # Cada opción llama a una función importada de otro archivo, excepto la salida.
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_paises(paises) # muestra la lista de países cargados en memoria, formateando números con puntos.

        elif opcion == "2":
            if agregar_pais(paises): # agrega un nuevo país a la lista en memoria, validando que no esté vacío ni duplicado, y que los números sean correctos.
                guardar_paises_en_csv(ruta_csv, paises) # guarda la lista actualizada de países en el archivo CSV, sobrescribiendo el contenido anterior para mantenerlo sincronizado con la memoria.

        elif opcion == "3":
            if actualizar_pais(paises): # actualiza los datos de un país existente en la lista en memoria, buscando por nombre y validando los nuevos datos.
                guardar_paises_en_csv(ruta_csv, paises)

        elif opcion == "4":
            buscar_pais(paises) # busca un país por nombre en la lista en memoria y muestra sus datos si lo encuentra, o un mensaje de error si no lo encuentra.

        elif opcion == "5":
            menu_filtros(paises) # muestra un submenú para aplicar diferentes filtros a la lista de países en memoria, como por continente, población o superficie, y muestra los resultados encontrados. No modifica la lista original.

        elif opcion == "6": # muestra un submenú para ordenar la lista de países en memoria por diferentes criterios, como nombre, población o superficie, y muestra la lista ordenada. No modifica la lista original.
            ordenar_paises(paises)

        elif opcion == "7":
            mostrar_estadisticas(paises) # muestra estadísticas generales sobre la lista de países en memoria, como el país más poblado, el país más grande, el continente con más países, etc. No modifica la lista original.

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Error: opcion invalida.")


main()