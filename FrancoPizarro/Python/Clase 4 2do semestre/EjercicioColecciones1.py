# Ejercicio 1: eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por último mostrar la lista

# Creamos la lista
lista = [1 ,2 ,3 , "Franco", 7, 7, 3, "Alberto", 5, "Franco", 2, "Alberto"]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
#print(conjunto)
#lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista))
print(lista)
