'''
Ejercicio 1: Función con *args para multiplicar
Crear una funcion para multiplicar los valores recibidos de tipo numericos,
utilizando argumentos variables *args como parametro de la funcion y regresar como resultado
la multiplicación de todos los valores pasados como argumentos.
'''

def multiplicar(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

resultado = multiplicar(2,56,8)
print(f"El resultado de la multiplicación es: {resultado}")
