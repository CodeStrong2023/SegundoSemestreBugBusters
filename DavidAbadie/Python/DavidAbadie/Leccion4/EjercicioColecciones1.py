# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetido, por último mostrar la lista

# Creamos una lista
lista = [1, 2, 3, 4, "David", 8, 2, "Pepe", 1, "David"]
# conjunto = set(lista)  # Convertimos la lista a un conjnunto de tipo set
# lista = list(conjunto)  # Convertimos el conjunto en una lista
lista = list(set(lista))  # La conversion hecha en una sola linea de codigo (eficiente)
print(lista)
