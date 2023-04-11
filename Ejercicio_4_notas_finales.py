"""
CALCULO DE NOTAS FINALES
Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un curso. 
Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una participación 
en clase. Quieres calcular la nota final de cada estudiante, donde los exámenes valen un 30% 
cada uno, el trabajo final vale un 30% y la participación en clase vale un 10%. Para ello, 
puedes usar NumPy para crear un array de 4 columnas y n filas, donde n es el número de estudiantes. 
Cada columna representa una de las calificaciones y cada fila representa un estudiante. 
Luego, puedes usar operaciones de NumPy para calcular la nota final de cada estudiante y 
almacenarla en un nuevo array de una sola columna.
"""
#importamos numpy
import numpy as np

print("------ NOTAS FINALES ------")

#creamos una lista con la cantidad de alumnos a ingresar 
calificaciones = []
#definimos la cantidad de columnas que necesitaremos
columnas = 6
respuesta = False
#con un while repetimos cuantos alumnos quiere ingresar

while True:
    #con un try except agregamos verificamos que los datos ingresados sean correctos
    try:
        #solicitamos por pantalla cuantos alumnos quiere ingresar
        alumnos = int(input("¿Cuantos alumnos quiere ingresar?\n"))
        #colocamos los titulos al array
        #alumno = ["ID", "Examen 1", "Examen 2", "Trabajo Final", "Participacion", "Nota Final"]
        #tenemos en cuenta la cantidad el titulo para la cantidad de filas
        filas = alumnos
        #si se ingresar los alumnos salimos del break
        break
    except ValueError:
        print("Los datos ingresados no son correctos")
#iniciamos la variable en 1
can_alumno = 1
#la condicion es que can_alumno sea menor o igual a los alumnos ingresados.


while can_alumno <= alumnos:
    #controlamos los erroes
    try:   
        #solicitamos por pantalla ID y notas
        id = float(input("Ingrese el id:\n"))
        examen_1 = float(input("Ingrese la nota del examen 1:\n"))
        examen_2 = float(input("Ingrese la nota del examen 2:\n"))
        trabajo_final = float(input("Ingrese la nota del trabajo final:\n"))
        participacion = float(input("Ingrese la nota por la participacion:\n"))
        nota_final = (examen_1 * 0.3) + (examen_2 * 0.3) + (trabajo_final * 0.3) + (participacion * 0.1)
        alumno = [id, examen_1, examen_2, trabajo_final, participacion, round(nota_final, 2)] #redondeamos la nota final
        # hacemos un apend a la lista / otra forma seria crear 1 array por cada ingreso e ir concatenando los arrays
        calificaciones.append(alumno)
        #sumamos en 1 esta variable para ir contando los alumnos ingresados
        can_alumno += 1
    except ValueError:
        print("Los datos ingresados no son correctos.")
#creamos un array y le pasamos la lista, luego hacemos un reshape 
array_calificaciones = np.array((calificaciones)).reshape((filas,columnas))
print("------ NOTAS FINALES ------")
print(array_calificaciones)
print(type(array_calificaciones))

print("------ PROMEDIOS FINALES ------")
promedios = (np.sum(array_calificaciones[:, 5])) / alumnos #el : significa todas las filas de la columna 5
print("El promedio de las Notas Finales es:", round(promedios, 2)) #redondeamos el promedio final

