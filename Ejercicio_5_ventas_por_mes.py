"""
ANALISIS DE DATOS - VENTAS POR MES
Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año. 
Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la venta y la 
categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos, etc.). 
Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en cada mes. 
Para ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde n es el número de ventas. 
Luego, puedes usar operaciones de NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes.
(Pista 1) Tu array de entrada puede tener un a forma de este tipo:
(Pista 2: puedes cambiar el tipo de dato del array de string a entero usando array[:,i].astype(int) )
"""

import numpy as np
from termcolor import colored

#definimos el array de ventas. Aclaracion: al array se le pueden ir agregando ventas 
ventas = np.array([
    ["2022-01-01", 100, "ropa"],
    ["2022-01-02", 200, "alimentos"],
    ["2022-01-03", 150, "ropa"],
    ["2022-02-01", 120, "alimentos"],
    ["2022-02-02", 180, "electronicos"],
    ["2022-02-03", 200, "alimentos"],
    ["2022-03-01", 90, "ropa"],
    ["2022-03-02", 110, "electronicos"],
    ["2022-03-03", 100, "alimentos"],
    ["2022-12-31", 100, "alimentos"],
])

#guardamos en variables distintas las columnas
fechas = ventas[:,0]
venta_dia = ventas[:,1].astype(int) #convertimos los datos del aray a integer
categoria = ventas[:,2]

#verificamos cuantas filas tiene el array para luego recorrerlo (es la cantida de ventas totales)
num_filas = ventas.shape[0]
print("----- CANTIDAD DE VENTAS TOTALES -----")
print("Se realizaron", num_filas, "ventas")

#iniciliamos el array mes para contar las ventas por mes del array ventas
mes = np.zeros([12]).astype(int) #convertimos los datos del aray a integer para eliminar el ".0"
venta_mes = np.zeros([12])

#recorremos el array fechas para conocer el indice de las fila de las ventas por mes
for i in range(0, num_filas):
    if fechas[i] >= "2022-01-01" and fechas[i] <= "2022-01-31":
        mes[0] += 1 #contamos la cantidad de ventas en el mes
        venta_mes[0] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-02-01" and fechas[i] <= "2022-02-31":
        mes[1] += 1
        venta_mes[1] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-03-01" and fechas[i] <= "2022-03-31":
        mes[2] += 1
        venta_mes[2] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-04-01" and fechas[i] <= "2022-04-31":
        mes[3] += 1
        venta_mes[3] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-05-01" and fechas[i] <= "2022-05-31":
        mes[4] += 1
        venta_mes[4] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-06-01" and fechas[i] <= "2022-06-31":
        mes[5] += 1
        venta_mes[5] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-07-01" and fechas[i] <= "2022-07-31":
        mes[6] += 1
        venta_mes[6] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-08-01" and fechas[i] <= "2022-08-31":
        mes[7] += 1
        venta_mes[7] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-09-01" and fechas[i] <= "2022-09-31":
        mes[8] += 1
        venta_mes[8] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-10-01" and fechas[i] <= "2022-10-31":
        mes[9] += 1
        venta_mes[9] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-11-01" and fechas[i] <= "2022-11-31":
        mes[10] += 1
        venta_mes[10] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-12-01" and fechas[i] <= "2022-12-31":
        mes[11] += 1
        venta_mes[11] += venta_dia[i] #sumamos la cantidad de ventas del mes

#imprimimos las ventas por mes, cantidad y monto total
print("----- VENTAS POR MES -----")
for i in range(0,12):
    print("La cantidad de VENTAS realizadas en el mes" , colored(str(i+1), 'red'), "es de", colored(str(mes[i]), 'red'), "y suma un total de: $", colored(str(venta_mes[i]), 'red'))


""""
RESOLUCION DE ELENA
"""

print("------ RESOLUCION DE ELENA -------")


# Extraer las fechas
fechas = np.array([venta[0] for venta in ventas])
#print(fechas)
# Extraer el mes
meses = np.array([int(fecha[5:7]) for fecha in fechas])
print("Los meses son:", meses)


# sumar los montos de venta por mes
montos_mes = np.zeros(12)
for mes in range(1,13):
    # ventas relacionadas con ese mes
    ventas_mes = ventas[meses == mes] #AL ARRAY VENTAS LE PASAMOS OTROS ARRAY QUE POSEE LOS MESES. CUANDO ESE ARRAY MESES ES IGUAL A UN ENTERO, ES COMO SI LE PASARA 
    print(ventas_mes)
    print("-----")
    # suma de las ventas del mes en cuestion
    montos_mes[mes-1] = np.sum(ventas_mes[:,1].astype(int))

ventas_mes = ventas[meses == 2]
print(ventas_mes)
print("Monto total de ventas por mes:", montos_mes)

"""
Explicacion de ventas_mes = ventas[meses == mes]
 
1. meses == mes: Esta es una condición booleana que compara cada elemento de la matriz meses con el valor de la variable mes. 
La comparación devuelve una matriz booleana del mismo tamaño que meses, que es True en las posiciones donde el valor de meses 
es igual a mes, y False en las demás posiciones.

2. ventas[meses == mes]: Esta expresión utiliza la matriz booleana anterior como índice para la matriz ventas. 
Cuando se utiliza una matriz booleana como índice, se seleccionan los elementos de la matriz correspondientes a las posiciones 
donde la matriz booleana es True. Por lo tanto, la expresión selecciona las ventas en las que el mes es igual al valor de la 
variable mes.
Por ejemplo, si "mes" es igual a 3, la expresión "meses == mes" devuelve un arreglo booleano donde los elementos que 
corresponden al mes de marzo son True y los demás son False.

En resumen, la línea de código ventas_mes = ventas[meses == mes] selecciona las ventas que corresponden al mes actual mes, 
utilizando una condición booleana que compara los valores de meses con mes como índice para la matriz ventas.

"""