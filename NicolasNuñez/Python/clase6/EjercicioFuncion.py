'''
Ejercicio 3: Crear una funcion para sumar los valores recibidos de tipo numericos,
utilizando argumentos variables *args como parametro de la funcion y agregr como resultado
la suma de todos los valores pasados como argumentos.
'''


def sumar(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

suma = sumar(23,54,1,0,45,23)
print(f"El resultado es: {suma}")