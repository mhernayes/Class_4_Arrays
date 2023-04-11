"""
ARRAYS 2D
9. Crea un arrays lleno de 1s con una longitud dada por el usuario
10.Cambia la forma del array para que tenga una estructura de tipo (filas, columnas) 
11.Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)
12.Concatena ambas estructuras horizontalmente y verticalmente
(Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy)
"""

import numpy as np

"""CONCATENAR ARRAYS"""
print("--------------")
len = int(input("Por favor ingrese la longitud del array:\n"))
my_array_1 = np.zeros(len)
my_array_1.fill(1)
print(my_array_1)

print("--------------")
my_array_1 = my_array_1.reshape((3,3))
print(my_array_1)

print("--------------")
my_array_2 = np.eye(3, k = 1)
print(my_array_2)

#Para concatenar 2 arrays deben tener el mismo tamaño excepto en la dimension correspondiente al axis
print("--------------")
my_array_3 = np.concatenate((my_array_1,my_array_2), axis=1)
print(my_array_3)

#Otra forma de hacerlo es con vstack y con hstack dependiendo que eje quisiera unir
print("--------------")
my_array_4 = np.vstack((my_array_1,my_array_2))
print(my_array_4)

print("--------------")
my_array_5 = np.hstack((my_array_1,my_array_2))
print(my_array_5)
