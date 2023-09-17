
'''
Ejercicio 2: Operaciones de conjuntos con listas
Escriba un programa que tenga 2 listas y que cree las siguientes listas
(en las que no deben haber repetición)

1- Lista de palabras que aparecen en las listas
2- Lista de palabras que aparecen en la primera lista, pero no en la segunda
3- Lista de palabras que aparecen en la segunda lista, pero no en la primera
4- Lista de palabras que aparecen en ambas listas
'''

lista1 = [21, "Java", 45, True, "12", 21, "IDE"]
lista2 = ["Python", True, 21, "JavaScript", 21, "Java", "Python"]

# Eliminamos los elementos duplicados pasanado las listas a conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)
print(f"Lista de palabras que aparecen en las listas: {union}")

primer_lista = list(conjunto1 - conjunto2)
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {primer_lista}")

segunda_lista = list(conjunto2 - conjunto1)
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {segunda_lista}")

ambas_listas = list(conjunto1 & conjunto2)
print(f"Lista de palabras que aparecen en ambas listas: {ambas_listas}")
