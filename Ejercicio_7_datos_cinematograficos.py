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
])

#determinamos el largo del array peliculas
num_filas = peliculas.shape[0]

#creamos array vacios para despues ir concatenandolo
array_comedia = np.zeros(3).reshape((1,3))
array_accion = np.zeros(3).reshape((1,3))
array_drama = np.zeros(3).reshape((1,3))

for i in range(0, num_filas):
    #separamos la duracion, año de estreno y puntaje por categoria
     
    if peliculas[i, 1] == "Comedia":
        #creamos un array para ir agregandolo al array comedia
        com_row = np.zeros(3).reshape((1,3))
        #agreamos a la fila la duracion, el año de estreno y el puntaje
        com_row[0, 0] = peliculas[i,2]
        com_row[0, 1] = peliculas[i,3]
        com_row[0, 2] = peliculas[i,4]
        #concatenamos el array_comedia con la fila com_row
        array_comedia = np.concatenate((array_comedia, com_row), axis=0)
    
    elif peliculas[i, 1] == "Accion":
        #creamos un array para ir agregandolo al array comedia
        acc_row = np.zeros(3).reshape((1,3))
        #agreamos a la fila la duracion, el año de estreno y el puntaje
        acc_row[0, 0] = peliculas[i,2]
        acc_row[0, 1] = peliculas[i,3]
        acc_row[0, 2] = peliculas[i,4]
        #concatenamos el array_comedia con la fila com_row
        array_accion = np.concatenate((array_accion, acc_row), axis=0)
    
    elif peliculas[i, 1] == "Drama":
        #creamos un array para ir agregandolo al array comedia
        dra_row = np.zeros(3).reshape((1,3))
        #agreamos a la fila la duracion, el año de estreno y el puntaje
        dra_row[0, 0] = peliculas[i,2]
        dra_row[0, 1] = peliculas[i,3]
        dra_row[0, 2] = peliculas[i,4]
        #concatenamos el array_comedia con la fila com_row
        array_drama = np.concatenate((array_drama, dra_row), axis=0)

#printeamos los resultados
print("\n----- INFO DE PELICULAS DE COMEDIA -----")
array_comedia = np.delete(array_comedia, 0, axis = 0) #borramos la fila inicial que era igual 0
print(array_comedia)

print("\n-- Duracion promedio de las peliculas de COMEDIA --")
duracion_promedio_com = np.mean(array_comedia[:,0]) #todas las filas (:) de la columna 0
print(round(duracion_promedio_com, 2))

print("\n-- Puntaje promedio de las peliculas de COMEDIA --")
puntaje_promedio_com = np.mean(array_comedia[:,2]) #todas las filas (:) de la columna 0
print(round(puntaje_promedio_com, 2))

print("\n----- INFO DE PELICULAS DE ACCION -----")
array_accion = np.delete(array_accion, 0, axis = 0) #borramos la fila inicial que era igual 0
print(array_accion)

print("\n-- Duracion promedio de las peliculas de ACCION --")
duracion_promedio_acc = np.mean(array_accion[:, 0]) #todas las filas (:) de la columna 0
print(round(duracion_promedio_acc, 2))

print("\n-- Puntaje promedio de las peliculas de ACCION --")
puntaje_promedio_acc = np.mean(array_accion[:,2]) #todas las filas (:) de la columna 0
print(round(puntaje_promedio_acc, 2))

print("----- INFO DE PELICULAS DE DRAMA -----")
array_drama = np.delete(array_drama, 0, axis = 0) #borramos la fila inicial que era igual 0
print(array_drama)

print("\n-- Duracion promedio de las peliculas de DRAMA --")
duracion_promedio_dra = np.mean(array_drama[:, 0]) #todas las filas (:) de la columna 0
print(round(duracion_promedio_dra, 2))

print("\n-- Puntaje promedio de las peliculas de DRAMA --")
puntaje_promedio_dra = np.mean(array_drama[:,2]) #todas las filas (:) de la columna 0
print(round(puntaje_promedio_dra, 2))

#creamos un array con el genero y el puntaje maximo
array_puntaje_maximo = np.array([
    ["Comedia", str(puntaje_promedio_com)], 
    ["Accion", str(puntaje_promedio_acc)], 
    ["Drama", str(puntaje_promedio_dra)]]).reshape(3,2)

#nos quedamos unicamente con los numeros
array_puntaje_maximo_num = np.delete(array_puntaje_maximo, 0, axis = 1)

#buscamos la posicion del numero mayor
puntaje_maximo_posicion = np.argmax(array_puntaje_maximo_num)

#obtenemos la posicion del array creado que tiene el puntaje mas alto
puntaje_maximo = array_puntaje_maximo[puntaje_maximo_posicion]

#imprimimos el resultado
print("\nEl genero de pelicula con puntaje maximo es:", puntaje_maximo[0], "con", puntaje_maximo[1], "puntos.")

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
