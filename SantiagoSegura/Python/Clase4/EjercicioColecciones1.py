# Ejercicio1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# eliminar los elementos repetidos, por ultimo mostrar la lista

# Creamos la lista
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 1, "Ariel", 2, "Alberto"]
#conjunto = set(lista) # Convertimos la lista a un conjunto set
#lista = list(conjunto) # Convertimos el conjunto en una lista
lista = list(set(lista)) # La conversion hecha en una sola linea de codigo (eficiente)
print(lista)




