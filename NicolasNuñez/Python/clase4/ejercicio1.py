
'''
Ejercicio 1: Eliminar dupolicados de una lista.
Escriba un programa donde tenga una lista y que elimine los elementos
repetidos, por ultimo mostrar la lista.
'''

# creamos la lista
lista = [23, "hola", 34.56, "Hola", True, 23, "Python", False, "hola"]

# convertimos la lista a un conjunto para que los elementos duplicados se eliminen
conjunto = set(lista)

# volvemos a convertir el conjunto a lista
lista = list(conjunto)
print(lista)






