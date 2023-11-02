'''
Ejercicio 1: Función con *args para multiplicar
Crear una funcion para multiplicar los valores recibidos de tipo numericos,
utilizando argumentos variables *args como parametro de la funcion y regresar como resultado
la multiplicación de todos los valores pasados como argumentos.
'''
# Definimos la funcion para multiplicar
def multiplicar(*args): # El mas utilizado es *args
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado
# Llamamos a la funcion
print(multiplicar(3, 5, 15, 3)) # Le pasamos los argumentos