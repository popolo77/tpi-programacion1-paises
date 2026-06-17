# Trabajo Practico Integrador - Programacion 1

## Gestion de Datos de Paises en Python

Proyecto desarrollado en Python para gestionar datos de paises a partir de un archivo CSV. El sistema permite cargar datos, mostrar registros, agregar paises, actualizar informacion, buscar, filtrar, ordenar y calcular estadisticas basicas.

## Datos del trabajo

- Institucion: Universidad Tecnologica Nacional
- Carrera: Tecnicatura Universitaria en Programacion a Distancia
- Materia: Programacion 1
- Estudiante: Mariano Popolo
- Modalidad: Trabajo individual
- Fecha: Junio de 2026

## Objetivo

Integrar los contenidos trabajados durante la materia Programacion 1 mediante una aplicacion funcional de consola, aplicando funciones, listas, diccionarios, condicionales, bucles, manejo de archivos CSV, validaciones, busquedas, filtros, ordenamientos y estadisticas.

## Estructura del proyecto

```text
TPI_Paises_Programacion1_Mariano_Popolo/
|
|-- main.py
|-- datos.py
|-- validaciones.py
|-- busquedas.py
|-- filtros.py
|-- ordenamientos.py
|-- estadisticas.py
|-- paises.csv
|-- README.md
|-- Informe_TPI_Programacion1_Mariano_Popolo.pdf
|-- .gitignore
```

## Responsabilidad de cada archivo

- `main.py`: contiene el menu principal y coordina la ejecucion del sistema.
- `datos.py`: carga datos desde CSV, guarda cambios, muestra paises, agrega paises y actualiza poblacion/superficie.
- `validaciones.py`: valida entradas del usuario, evitando campos vacios y numeros invalidos.
- `busquedas.py`: permite buscar paises por nombre completo o coincidencia parcial.
- `filtros.py`: permite filtrar por continente, rango de poblacion y rango de superficie.
- `ordenamientos.py`: ordena por nombre, poblacion o superficie, en forma ascendente o descendente.
- `estadisticas.py`: calcula estadisticas generales del conjunto de paises.
- `paises.csv`: archivo base de datos en formato CSV.

## Estructura de datos utilizada

El programa trabaja con una lista de diccionarios. Cada pais se representa como un diccionario con las siguientes claves:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

La lista permite almacenar varios paises y recorrerlos para mostrarlos, buscarlos, filtrarlos, ordenarlos y calcular estadisticas.

## Ejecucion

Abrir la carpeta del proyecto en una terminal y ejecutar:

```bash
python main.py
```

## Funcionalidades

- Mostrar todos los paises cargados.
- Agregar un pais nuevo.
- Evitar paises duplicados.
- Actualizar poblacion y superficie de un pais existente.
- Buscar paises por coincidencia parcial o exacta.
- Filtrar por continente.
- Filtrar por rango de poblacion.
- Filtrar por rango de superficie.
- Ordenar por nombre, poblacion o superficie.
- Elegir orden ascendente o descendente.
- Mostrar estadisticas basicas.
- Guardar cambios en el archivo CSV.

## Validaciones implementadas

- No permite campos de texto vacios.
- No permite poblacion o superficie menor o igual a cero.
- Controla errores cuando se ingresan valores no numericos.
- Evita cargar paises duplicados.
- Controla opciones invalidas en menus.
- Valida que los rangos de poblacion o superficie sean coherentes.
- Maneja errores de lectura o escritura del archivo CSV.

## Ordenamientos

Para los ordenamientos se utiliza `sorted()` junto con funciones auxiliares que devuelven el criterio de ordenamiento: nombre, poblacion o superficie. No se utilizaron funciones `lambda`, para mantener el codigo mas explicito y acorde a los contenidos trabajados.

## Repositorio

Repositorio GitHub publico:

https://github.com/popolo77/tpi-programacion1-paises.git

## Video demostrativo

Pendiente de carga.

Importante: el video demostrativo es un requisito excluyente segun la rubrica. Debe agregarse el link cuando este disponible.

## Documentacion

El informe PDF se incluye en este repositorio con el nombre:

`Informe_TPI_Programacion1_Mariano_Popolo.pdf`

## Conclusiones

Este proyecto permitio integrar los principales conceptos de Programacion 1 en una aplicacion funcional. El uso de listas y diccionarios permitio representar los datos de paises de forma clara. La modularizacion ayudo a organizar el codigo en responsabilidades especificas, facilitando la lectura, el mantenimiento y la explicacion del programa.
