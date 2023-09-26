# Repaso de ser o conjunto
# Principal caracteristica: los valores son unicos (es decir, no puede haber duplicados)

conjunto = set()  # forma de inicializar un set vacio
conjunto1 = {'bye'}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)
conjunto1.add(9)
print(conjunto1)
print(3 not in conjunto1)  # Preguntamos si el número 3 está en el conjunto1

# Comparar dos conjuntos
print(conjunto1 == conjunto)  # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto2 = set()
conjunto2.add('Hola')
conjunto2.add('bye')
conjunto3 = conjunto1 | conjunto2  # La linea une los conjuntos
print(conjunto3)

# Elementos en común
conjunto3 = conjunto1 & conjunto2
print(conjunto3)  # Se imprime el elemento repetido en ambos conjuntos

# Elementos diferentes
conjunto3 = conjunto1 - conjunto2
print(conjunto3)  # Se imprime el elemento que está en el conjunto 1 y no en el conjunto 2

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

# Elementos que no comparten o que son diferentes entre ambos conjuntos
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

conjunto3 = conjunto1 | conjunto2

# Subconjuntos dentro de conjuntos
# Funcion issubset
print(conjunto1.issubset(conjunto3))
print(conjunto2.issubset(conjunto3))
print(conjunto.issubset(conjunto3))

# Funcion issuperset
print(conjunto3.issuperset(conjunto1))
print(conjunto2.issuperset(conjunto2))

# Conjuntos disconexos (no comparten elementos en comun)
print(conjunto1.isdisjoint(conjunto2))

# Funcion para que no se pueda agregar, modificar ni
# eliminar elementos del conjunto (frozenset)
conjunto1 = frozenset
