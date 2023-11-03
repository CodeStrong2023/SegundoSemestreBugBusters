'''
Ejercicio 1: Crear una funcion para sumar los valores  recibidos de tipo númericos,
utlizando argumentos variables *args como parametro  de la funcion y agregar
como resultado la suma de todos los valores pasados, como argumentos
'''
#Definimos una funcion
def sumar_valor(*args): # Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    #iteramos elemento
    for valor in args:
        resultado += valor
    return resultado

# llamamos a la funcion
print(sumar_valor(3, 5, 9, 2, 1))