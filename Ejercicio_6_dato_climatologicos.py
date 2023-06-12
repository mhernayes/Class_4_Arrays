"""
ANALISIS DE DATOS CLIMÁTICOS
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la temperatura, 
a humedad y la presión atmosférica en una ciudad durante un año. Quieres analizar estos datos para determinar 
cuál fue la temperatura promedio de cada mes, cuál fue la humedad promedio y la presión atmosférica promedio 
durante todo el año. Para ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, 
donde n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los datos por mes y 
calcular las medias de temperatura, humedad y presión atmosférica correspondientes.
(Pista 1) Tu array de entrada podría ser algo como esto, con datos de temperatura, humedad, presión y mes del año:
"""

import numpy as np

#definimos el array de clima.
clima = np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])

#contamos la cantidad de filas
num_filas = clima.shape[0]

#creamos un array mes con los 12 meses
mes = np.arange(1,13)

#creamos un array para ir sumando la temperatura, la humedad y la presion
suma_temp = np.zeros(12)
suma_hum = np.zeros(12)
suma_presion = np.zeros(12)
                        
#creamos los arrays para guardar los promedios                        
promedio_temp = np.zeros(12)
promedio_hum = np.zeros(12)
promedio_presion = np.zeros(12)

#inicializamos la variable cant_mes para ir contando los meses
cant_mes = 0

#recorremos con 2 for el array clima y los array de las sumas 
for j in range(0,12):
    for i in range(0, num_filas):
        if clima[i, 3] == mes[j]:
            #vamos sumando el total de la temperatura, humedad y presion
            suma_temp[j] += clima[i, 0]
            suma_hum[j] += clima[i, 1]
            suma_presion[j] += clima[i, 2]
            #cada vez que suma incrementamos en 1 esta variable para despues dividir por el total y calcular el promedio
            cant_mes += 1
    #calculamos los promedios y los guardamos en sus correspondientes arrays
    promedio_temp[j] = round((suma_temp[j] / cant_mes), 2)
    promedio_hum[j] = round((suma_hum[j] / cant_mes), 2)
    promedio_presion[j] = round((suma_presion[j] / cant_mes), 2)
    cant_mes = 0 #reiniciamos cant_mes

#imprimimos los resultados

print("----- SUMAS TOTALES -----")
print("La suma de las temperaturas es:", suma_temp)
print("La suma de la humedad es:" , suma_hum)
print("La suma de las presion es:", suma_presion)

print("----- PROMEDIO POR MES -----")
print("El promedio de las temperaturas por mes es:", promedio_temp)
print("El promedio de la humedad por mes es:", promedio_hum)
print("El promedio de las presiones por mes es:", promedio_presion)


# guardamos datos en arrays independientes
meses = clima[:,3]
temperaturas = clima[:,0]
humedad = clima[:,1]
presion = clima[:,2]

# inicializamos arrays de valores promedio por mes
temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

# recorrer los valores para cada mes
for i in range(12):
    # calculamos valores medios
    temp_mes[i] = np.mean(temperaturas[meses == i+1])
    humedad_mes[i] = np.mean(humedad[meses == i+1])
    presion_mes[i] = np.mean(presion[meses == i+1])

    # imprimimos resultados para cada mes
    print("La temperatura promedio en el mes", i+1, " fue de", temp_mes[i], "grados")
    print("La humedad promedio en el mes", i+1, " fue de", humedad_mes[i])
    print("La presion promedio en el mes", i+1, " fue de", presion_mes[i], "bar")
