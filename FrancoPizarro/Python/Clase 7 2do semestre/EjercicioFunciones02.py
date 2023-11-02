'''
Ejercicio 2: funcion con * args apra multiplicar, crear una funcion para multiplicar
los valores recibidos de tipo númerico, utilizando argumentos variables *args
como parámetro de la función y regresar como resultado, la multiplicacion
de todos los valores pasados como argumentos
'''
# Definimos la funcion
def multiplicar_valores(*numeros): # El mas utilizado es *args
    resultado = 1 # El cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado

# Llamamos a la funcion
print(multiplicar_valores(3 ,5, 15, 3)) # le pasamos los argumentos