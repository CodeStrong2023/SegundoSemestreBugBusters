
'''
Ejercicio 1: Eliminar duplicadoas de una lista.
Escriba un programa donde tenga una lista y que elimine los elementos
repetidos, por ultimo mostrar la lista.
'''

lista = [1,5,2,6,1,3,6,3,1,7,4,2,5]

conjunto = set(lista)
lista = list(conjunto)
print(lista)

