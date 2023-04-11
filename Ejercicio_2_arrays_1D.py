"""
1. Crea un array con 15 números enteros aleatorios entre 1 y 100
2. Multiplica todos los elementos del array usando un bucle y después usando un
método de numpy. Compara los resultados
3. Crea otro array con 15 números decimales aleatorios entre 0 y 1
4. Suma los elementos de ambos arrays elementos por elemento. 
Resuélvelo usando un operador y después con una función de numpy
(Pista: busca en google que función de numpy hace esto)
5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy 
(Pista: busca en google que función de numpy hace esto)
6. Haz lo mismo con la multiplicación elemento por elemento. 
Usa un operador y después con una función de numpy
(Pista: busca en google que función de numpy hace esto)
7. Encuentra el valor más alto del primer array que has creado.
8. Calcula la media (mean), la mediana (median) y al deviación estandar (standard deviation) de los arrays 
(Nota: No nos importa el significado matemático de estos valores, 
lo importante es que encuentres que función de numpy necesitas. 
Puedes hacer la búsqueda en castellano o en inglés, 
aunque en inglés muchas veces suele haber más resultados).
"""

import numpy as np

#crear un array con numeros aleatorios del 1 al 100 con tamaño 15
array_1 = np.random.randint(1,101, size=15)
print(array_1)

#multiplicar los nuemeros usando un buble
resultado_multiplicacion = 1
for i in range(0,len(array_1)):
    resultado_multiplicacion *= array_1[i]
print("El resultado de la multiplicacion es" ,resultado_multiplicacion)

#multiplicar los numeros usando el metodo de numpy
array_multiplicacion = np.prod(array_1)
print("El resultado de la multiplicacion es" ,array_multiplicacion)

#creamos otro array con numeros aleatorios del 1 al 100 con tamaño 15
array_2 = np.random.uniform(0,3, size=15)
print(array_2)

#otra forma es:
array_decimales = np.random.random(15) #tambien puede ser random.ran pero no se le pasan parametros, siempre es de 0 a 1
print('Array con decimales del 0 al 1: ',array_decimales)

#sumamos los elementos de ambos arrays elemento por elemento
array_resultado_suma = []
print(array_1)
print(array_2)
resultado = 0
for i in range(0, len(array_1)):
    resultado = array_1[i] + array_2[i]
    array_resultado_suma.append(resultado)
print("El resultado de la suma es: ", array_resultado_suma)

#se puede sumar asi 2 arrays pero con menos decimales
array_resultado_suma_2 = array_1 + array_2
print("El resultado de la suma es: ", array_resultado_suma_2)

#se puede sumar asi 2 arrays pero con menos decimales
array_resultado_suma_3 = np.sum([array_1, array_2], axis=0)
print("El resultado de la suma es: ", array_resultado_suma_3)

#se puede sumar asi 2 arrays pero con menos decimales
array_resultado_suma_4 = np.add(array_1, array_2)
print("El resultado de la suma es: ", array_resultado_suma_4)

#restamos los elementos de los arrays
array_resultado_resta = []
print(array_1)
print(array_2)
resultado = 0
for i in range(0, len(array_1)):
    resultado = array_1[i] - array_2[i]
    array_resultado_resta.append(resultado)
print("El resultado de la resta es: ", array_resultado_resta)

#se puede restar asi 2 arrays pero con menos decimales
array_resultado_resta_2 = array_1 - array_2
print("El resultado de la resta es: ", array_resultado_resta_2)

#se puede restar asi 2 arrays pero con menos decimales
array_resultado_resta_3 = np.subtract(array_1, array_2)
print("El resultado de la resta es: ", array_resultado_resta_3)

#multiplicamos los elementos de los arrays
array_resultado_prod = []
print(array_1)
print(array_2)
resultado = 0
for i in range(0, len(array_1)):
    resultado = array_1[i] * array_2[i]
    array_resultado_prod.append(resultado)
print("El resultado de la multiplicacion es: ", array_resultado_prod)

#se puede multiplicar asi 2 arrays pero con menos decimales
array_resultado_prod_2 = array_1 * array_2
print("El resultado de la multiplicacion es: ", array_resultado_prod_2)

#se puede multiplicar asi 2 arrays pero con menos decimales
array_resultado_prod_3 = np.prod([array_1, array_2], axis=0)
print("El resultado de la multiplicacion es: ", array_resultado_prod_3)

#se puede multiplicar asi 2 arrays pero con menos decimales
array_resultado_prod_4 = np.multiply(array_1, array_2)
print("El resultado de la multiplicacion es: ", array_resultado_prod_4)

valor_mas_alto = np.max(array_1)
print("El valor mas alto del array", array_1, "es:", valor_mas_alto)

valor_medio = np.mean(array_1)
print("El valor mas alto del array", array_1, "es:", valor_medio)

valor_mediana = np.median(array_1)
print("La mediana del array", array_1, "es:", valor_mediana)

desviacion_standard = np.std(array_1)
print("La desviacion estandar es", desviacion_standard)

