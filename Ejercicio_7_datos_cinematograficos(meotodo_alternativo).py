"""
DATOS CINEMATOGRÁFICOS
Supongamos que tienes un conjunto de datos de películas que contiene información 
sobre su título, género, duración, año de lanzamiento y calificación. 
Quieres analizar estos datos para determinar cuál es el género de película más popular, 
cuántas películas se lanzaron en cada década y cuál es la duración promedio de cada 
género de película.
(Pista 1: Tu array de entrada puede tener la forma...)
(Pista 2: puede ser util investigar np.unique, np.argsort y np.count_nonzero)
"""
import numpy as np

peliculas = np.array([
    ["Pelicula 1", "Comedia", 120, 1990, 8.5],
    ["Pelicula 2", "Accion", 110, 2005, 7.8],
    ["Pelicula 3", "Drama", 95, 2010, 6.9],
    ["Pelicula 4", "Comedia", 100, 1985, 7.5],
    ["Pelicula 5", "Accion", 130, 2015, 8.1],
    ["Pelicula 6", "Drama", 115, 2000, 6.7],
    ["Pelicula 7", "Comedia", 90, 1995, 8.2],
    ["Pelicula 8", "Accion", 105, 2010, 7.4],
    ["Pelicula 9", "Drama", 125, 1980, 6.8],
    ["Pelicula 10", "Comedia", 95, 2000, 8.0],
    ["Pelicula 10", "Comedia", 95, 2020, 8.0],
])

# Obtener los índices de las películas de cada categoría
accion_indices = np.where(peliculas[:, 1] == 'Accion')[0]
comedia_indices = np.where(peliculas[:, 1] == 'Comedia')[0]
drama_indices = np.where(peliculas[:, 1] == 'Drama')[0]

# Crear arrays separados para cada categoría
peliculas_accion = peliculas[accion_indices]
peliculas_comedia = peliculas[comedia_indices]
peliculas_drama = peliculas[drama_indices]

# Imprimir los arrays separados
print("----- INFO DE PELICULAS DE COMEDIA -----")
print(peliculas_comedia)
print('')

#calculamos el promedio redondeado a 2 digitos (hay que convertir a un float la columna)
duracion_promedio_com = round(np.average(peliculas_comedia[:, 2].astype(float)), 2)
print("La duracion promedio de las peliculas de COMEDIA es:", duracion_promedio_com)

puntaje_promedio_com = round(np.average(peliculas_comedia[:, 4].astype(float)), 2)
print("El puntaje promedio de las peliculas de COMEDIA es:", puntaje_promedio_com)

print("----- INFO DE PELICULAS DE ACCION -----")
print(peliculas_accion)
print('')

#calculamos el promedio redondeado a 2 digitos (hay que convertir a un float la columna)
duracion_promedio_acc = round(np.average(peliculas_accion[:, 2].astype(float)), 2)
print("La duracion promedio de las peliculas de ACCION es:", duracion_promedio_acc)

puntaje_promedio_acc = round(np.average(peliculas_accion[:, 4].astype(float)), 2)
print("El puntaje promedio de las peliculas de COMEDIA es:", puntaje_promedio_acc)

print("----- INFO DE PELICULAS DE DRAMA -----")
print(peliculas_drama)
print('')

#calculamos el promedio redondeado a 2 digitos (hay que convertir a un float la columna)
duracion_promedio_dra = round(np.average(peliculas_drama[:, 2].astype(float)), 2)
print("La duracion promedio de las peliculas de DRAMA es:", duracion_promedio_dra)

puntaje_promedio_dra = round(np.average(peliculas_drama[:, 4].astype(float)), 2)
print("El puntaje promedio de las peliculas de COMEDIA es:", puntaje_promedio_dra)

#creamos el array puntaje maximo
array_puntaje_maximo = np.array([
    ["Comedia", puntaje_promedio_com], 
    ["Accion", puntaje_promedio_acc], 
    ["Drama", puntaje_promedio_dra]
])

#nos quedamos con la posicion del puntaje promedio maximo
puntaje_maximo = np.argmax(array_puntaje_maximo[:, 1].astype(float))
print("El genero de peliculas con puntaje maximo es", array_puntaje_maximo[puntaje_maximo, 0], "con", array_puntaje_maximo[puntaje_maximo, 1], "puntos")

#definimos un array con las decadas
"""
Si se desea dividir el rango de los valores en 12 bins, uno para cada mes, entonces 
el arreglo bin_meses debe tener una longitud de 13, de modo que haya 12 intervalos 
entre los 13 valores de bin_meses.
"""
bin_array = np.arange(1980, 2040, 10)

#nos quedamos con los años 
array_años = peliculas[:, 3]

#utilizamos el metodo histogram para contar la cantidad de peliculas por año.
array_histograma, bin_array = np.histogram(array_años, bin_array)

# Imprimimos los resultados
for i in range(len(array_histograma)):
    print("Década {}: {}".format(bin_array[i], array_histograma[i]))

