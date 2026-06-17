# Trabajo Práctico Integrador - Programación 1

## Gestión de Datos de Países en Python

### Tecnicatura Universitaria en Programación a Distancia

### Materia: Programación 1

---

## Integrante

* Mariano Popolo

Modalidad de trabajo: individual.

---

## Descripción del proyecto

Este proyecto consiste en una aplicación de consola desarrollada en Python para gestionar información de países a partir de un archivo CSV.

El sistema permite cargar datos desde un archivo, mostrar países, agregar nuevos registros, actualizar información, realizar búsquedas, aplicar filtros, ordenar datos y calcular estadísticas básicas.

Cada país se representa mediante un diccionario con los siguientes campos:

* nombre
* población
* superficie
* continente

Todos los países se almacenan dentro de una lista de diccionarios.

---

## Objetivo

El objetivo del trabajo es aplicar los conceptos vistos en Programación 1, especialmente:

* listas
* diccionarios
* funciones
* estructuras condicionales
* estructuras repetitivas
* lectura y escritura de archivos CSV
* validaciones
* filtros
* ordenamientos
* estadísticas básicas
* modularización del código

---

## Estructura del proyecto

```plaintext
TPI_Paises_Programacion1/
│
├── main.py
├── datos.py
├── validaciones.py
├── busquedas.py
├── filtros.py
├── ordenamientos.py
├── estadisticas.py
├── paises.csv
└── README.md
```

---

## Archivos principales

### main.py

Contiene el menú principal del sistema y coordina las distintas funcionalidades.

### datos.py

Contiene funciones relacionadas con la carga, visualización, agregado, actualización y guardado de países en el archivo CSV.

### validaciones.py

Contiene funciones para validar entradas del usuario, evitando campos vacíos y errores al ingresar números.

### busquedas.py

Contiene la función que permite buscar países por coincidencia parcial o exacta del nombre.

### filtros.py

Contiene las funciones para filtrar países por continente, rango de población y rango de superficie.

### ordenamientos.py

Contiene las funciones para ordenar países por nombre, población o superficie, tanto de forma ascendente como descendente.

### estadisticas.py

Contiene las funciones para calcular estadísticas generales sobre los países cargados.

### paises.csv

Archivo de datos utilizado como base del sistema.

---

## Funcionalidades del sistema

El programa permite:

1. Mostrar todos los países cargados.
2. Agregar un nuevo país.
3. Actualizar la población y la superficie de un país existente.
4. Buscar un país por nombre, usando coincidencia parcial o exacta.
5. Filtrar países por:

   * continente
   * rango de población
   * rango de superficie
6. Ordenar países por:

   * nombre
   * población
   * superficie
7. Mostrar estadísticas:

   * país con mayor población
   * país con menor población
   * promedio de población
   * promedio de superficie
   * cantidad de países por continente
8. Guardar los cambios realizados en el archivo CSV.

---

## Requisitos

Para ejecutar el programa se necesita:

* Python 3.x instalado
* Editor de código, por ejemplo Visual Studio Code
* Terminal o consola

No se utilizan librerías externas. Solo se utilizan módulos estándar de Python, como `csv` y `os`.

---

## Instrucciones de ejecución

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code o en una terminal.
3. Verificar que el archivo `paises.csv` esté en la misma carpeta que `main.py`.
4. Ejecutar el programa con el siguiente comando:

```powershell
python main.py
```

---

## Ejemplo de uso

Al iniciar el programa se muestra el siguiente menú:

```plaintext
========== SISTEMA DE GESTION DE PAISES ==========
1. Mostrar paises
2. Agregar pais
3. Actualizar pais
4. Buscar pais
5. Filtrar paises
6. Ordenar paises
7. Mostrar estadisticas
8. Salir
```

Ejemplo de búsqueda parcial:

```plaintext
Ingrese el nombre o parte del nombre del pais: mar

Resultados encontrados:

Nombre: Marruecos
Poblacion: 38.701.000
Superficie: 712.550 km2
Continente: Africa
```

Ejemplo de estadísticas:

```plaintext
Pais con mayor poblacion:
China - 1.412.000.000 habitantes

Pais con menor poblacion:
Uruguay - 3.426.260 habitantes

Promedio de poblacion:
189.220.396 habitantes

Promedio de superficie:
2.710.818 km2
```

---

## Validaciones implementadas

El sistema incluye validaciones para:

* evitar campos vacíos
* evitar valores numéricos inválidos
* evitar población o superficie menor o igual a cero
* evitar países duplicados
* controlar opciones inválidas en los menús
* manejar errores al leer el archivo CSV
* informar búsquedas o filtros sin resultados

---

## Datos utilizados

Los datos se almacenan en el archivo `paises.csv`, con la siguiente estructura:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
```

---

## Repositorio

Link al repositorio de GitHub:

PENDIENTE

---

## Video demostrativo

Link al video demostrativo:

PENDIENTE

---

## Documentación PDF

Link o archivo PDF del informe:

PENDIENTE

---

## Conclusión

El desarrollo de este trabajo permitió integrar varios conceptos fundamentales de Programación 1 en una aplicación funcional. Se trabajó con listas, diccionarios, funciones, archivos CSV, validaciones, búsquedas, filtros, ordenamientos y estadísticas.

La modularización del código permitió organizar mejor el proyecto, separando responsabilidades en distintos archivos. Esto facilitó el desarrollo, las pruebas y la comprensión general del sistema.

El proyecto también permitió comprender la importancia de validar datos, manejar errores y documentar correctamente una aplicación para que pueda ser utilizada y evaluada por otras personas.
