# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a
# continuation elimine los elementos repetidos, por último
# mostrar la lista

# Ejemplo 1
listaSuper = ['zanahoria', 'leche', 'manteca', 'queso', 'fideos', 'cereales', 'jamon', 'manteca', 'queso']
set_listaSuper = set(listaSuper)
print(set_listaSuper)

# Ejemplo 2
lista_numeros = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9, 0, 9]
lista_sin_duplicados = []

for numero in lista_numeros:
    if numero not in lista_sin_duplicados:
        lista_sin_duplicados.append(numero)

print(lista_sin_duplicados)

# Ejemplo 3
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 5, "Ariel", 2, "Alberto"]
# conjunto = set(lista)
# print(conjunto)  # Convertimos la lista a un conjunto de tipo set
# lista = list(conjunto)  # Convertimos el conjunto a una lista
lista = list(set(lista))  # La conversion hecha en una sola línea de código
print(lista)
