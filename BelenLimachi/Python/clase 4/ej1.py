# Ejercicio1: Eliminar duplicados de una lista 
# Escribir un programa donde tenga una lista y que a continuacion 
# elimine los elementos repetidos, por último mostrar la lista

lista = [1, 2, 3, "Ariel", "Natalia", 3, 7, 3, "Ariel"]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # Conversion hecha en una sola linea
print(lista)