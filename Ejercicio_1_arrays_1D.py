"""

ARRAYS 1D PARTE 1:
1. Crea un array_1 lleno ceros con una longitud de 8 elementos.
2. Haz que todos los elementos de este array sean igual a 2
3. Crea un array_2 que contenga todos los números pares del 1 al 10.
4. Suma todos los elementos del array_2 usando un bucle y después usando un método de numpy. Compara los resultados
5. Revierte array_2 y guárdalo en una variable independiente.
6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_2_revertido
(Pista: Investiga el uso de intersect1d() de numpy)
7. Crea un arrays lleno de 1s con una longitud dada por el usuario

"""
#importamos numpy como np
import numpy as np

#creamos un array lleno de 0 de elementos
print("---------------")
array_1 = np.zeros(8)
print(array_1)

#todos los elementos de este array deben ser igual a 2
print("---------------")
array_1[:] = 2
print(array_1)

#creamos un array que contenga los numero pares de 1 al 10
print("---------------")
array_2 = np.arange(2,12,2)
print(array_2)

#METDOS PARA SUMAR EN UN ARRAY
#sumamos con un bucle todos los elementos del array
print("---------------")
total = 0
for i in range(0, len(array_2)):
    total += array_2[i]
print(total)

#usamos el metodo de numpy para sumar
print("---------------")
suma_array_2 = np.ndarray.sum(array_2)
print(suma_array_2)

#sumamos sin np
print("---------------")
suma_2_array_2 = array_2.sum()
print(suma_2_array_2)

import numpy as np

array_2 = np.arange(2,11,2)
print("El array original es:", array_2)

# creamos array revertido independiente
#inicializacion
array_2_reverse = np.zeros(len(array_2), dtype=int)
array_2_reverse[:] = array_2[::-1] #Indicamos array_2reverse[:] para independizar los arrays (hay que iniciarlo previamente). luego, todos los elementos del array_2 se recorren al reves.
print("El array revertido es:", array_2)
array_2_reverse[:] = 2
print("El array revertido es:", array_2_reverse)
print("El array original es:", array_2)

#comparamos 2 arrays y vemos que valores estan repetidos
print("---------------")
elemento_comunes_1 = np.intersect1d(array_1, array_2)
print(array_1)
print(array_2)
print(elemento_comunes_1)

print("---------------")
elemento_comunes_2 = np.intersect1d(array_2, array_2_reverse)
print(array_2)
print(array_2_reverse)
print(elemento_comunes_2)

#crear un array llenos de 1 de longitud ingresada por el usuario
long = int(input("Ingrese un numero"))
array_usuario = np.ones(long)
print(array_usuario)

