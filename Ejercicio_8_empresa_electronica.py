"""
EMPRESA DE ELECTRONICA
Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y 
quieres analizar los datos de calidad de los componentes utilizados en la producción 
de dichos dispositivos. Tienes un conjunto de datos que contiene información sobre 
la fecha de producción, el tipo de componente, el lote al que pertenece el componente 
y la puntuación de calidad del componente (un número entre 0 y 100). 
Quieres analizar estos datos para determinar cuál es el tipo de componente con la 
puntuación de calidad más alta, cuántos componentes se produjeron en cada mes y cuál es 
la puntuación de calidad promedio de cada tipo de componente.
(Pista 1: Tu array de entrada puede tener la forma...)
(Pista 2: puede ser util investigar np.unique y np.argmax)
"""

import numpy as np

componentes = np.array([
    ["2022-01-01", "Componente 1", "Lote A", 80],
    ["2022-01-15", "Componente 1", "Lote B", 90],
    ["2022-02-01", "Componente 2", "Lote C", 85],
    ["2022-02-15", "Componente 2", "Lote D", 95],
    ["2022-03-01", "Componente 1", "Lote E", 75],
    ["2022-03-15", "Componente 2", "Lote F", 90],
    ["2022-12-15", "Componente 2", "Lote F", 90],
])

print("\n----- LISTADO COMPONENTE 1 -----")
#separamos este array por tipo de componente
componente_1 = np.where(componentes[:,1] == "Componente 1")[0] #nos quedamos con los indices del componente

#guardamos el array en otra variable
array_componente_1 = componentes[componente_1]

#imprimimos el array
print(array_componente_1)

#averiguamos cual es el indice con la maxima calidad (columna 3)
punt_max_1 = np.argmax(array_componente_1[:, 3])
print("El componente con la calidad más alta es", array_componente_1[punt_max_1, 2], "con un puntaje de", array_componente_1[punt_max_1, 3])

#calculamos el promedio
puntaje_1 = array_componente_1[:,3].astype(int)
prom_1 = round(np.average(puntaje_1), 2)
print("El promedio es:", prom_1)

"""
INFORMACION DEL COMPONENTE 2
"""

print("\n----- LISTADO COMPONENTE 2 -----")
#separamos este array por tipo de componente
componente_2 = np.where(componentes[:,1] == "Componente 2")[0] #nos quedamos con los indices del componente

#guardamos el array en otra variable
array_componente_2 = componentes[componente_2]

#imprimimos el array
print(array_componente_2)

#averiguamos cual es el indice con la maxima calidad (columna 3)
punt_max_2 = np.argmax(array_componente_2[:, 3])
print("El componente con la calidad más alta es", array_componente_2[punt_max_2, 2], "con un puntaje de", array_componente_2[punt_max_2, 3])

#calculamos el promedio
puntaje_2 = array_componente_2[:,3].astype(int)
prom_2 = round(np.average(puntaje_2), 2)
print("El promedio es:", prom_2)

print("\n----- CANTIDAD PRODUCIDA POR MES -----")
#creamos el array bin que es el array contenedor
"""
Si se desea dividir el rango de los valores en 12 bins, uno para cada mes, entonces 
el arreglo bin_meses debe tener una longitud de 13, de modo que haya 12 intervalos 
entre los 13 valores de bin_meses.
"""
bin_array = np.arange(1,14)

#nos quedamos con el array fecha
fechas = componentes[:, 0]

#recorremos el array fecha y nos quedamos con los meses
meses = np.array([int(fecha[5:7]) for fecha in fechas]) #convierto los numeros a enteros

#llenamos el array histograma y le pasamos el array meses y el bin_array que son la cantidad de meses
array_histograma, bin_array = np.histogram(meses, bin_array)

for i in range(0, len(array_histograma)):
    print("En el mes {} se fabricaron {} componentes.".format(bin_array[i], array_histograma[i]))


