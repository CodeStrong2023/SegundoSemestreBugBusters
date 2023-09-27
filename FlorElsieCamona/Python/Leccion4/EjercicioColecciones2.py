# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# Cree las siguientes listas (en las que no debe haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = ['DF983', 'GH783', 'index', 'code01', 777,  00, 'GD893', 'str', 12, 'GG467']
lista2 = ['code01', 8940, 'string', 12, 00, 'GG467', 15, 47.85, 'boolean', 'object']

# 1
for element in lista1:
    print(element, end=' ')
print(' ')
for element in lista2:
    print(element, end=' ')

# 2
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = conjunto1 - conjunto2
print(' ')
print('Lista de palabras que se encuentran solamente en el conjunto1: ', conjunto3)

# 3
conjunto4 = conjunto2 - conjunto1
print(conjunto4)

# 4
conjunto5 = conjunto1 & conjunto2
print(conjunto5)


# Otra forma de resolverlo -->

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

# 1
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)










