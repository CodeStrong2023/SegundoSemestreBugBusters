# Colecciones

# Listas --> conjunto de elementos (pueden ser de diferentes tipos de datos) son mutables, se pueden modificar

nombres = ["Nicolas", "Santino", "Sofia", "Nazarena", "Tomas"]
print(nombres)

# muestra los nombres contando desde el principio hacia el final:
print(nombres[2])
print(nombres[4])
print(nombres[1])

# muestra los nombres contando desde el final haacia el principio:
print(nombres[-1])
print(nombres[-2])
print(nombres[-5])

# recorrer una serie de indice:
print(nombres[0:2]) # recorre el indice 0 y 1
print(nombres[1:4]) # recorre el indice 1,2,3

print(nombres[ :3]) # recorre desde el principio hasta el indice 2
print(nombres[1: ]) # recorre desde el indice 1 hasta el final

# modificamos un valor:
nombres[1] = "Flor"
nombres[3] = "Oyku"
print(nombres)

# iterar una lista:
for i in nombres:
    print(i)
else:
    print("Se acabaron los elementos en la lista")

# metodos para listas:
print(len(nombres)) # cuantos elementos tiene la lista

nombres.append("Marcelo") # agrega un elemento al final de la lista

nombres.insert(3,"Mariana") # agrega un elemento en el indice especificado

nombres.remove("Sofia") # elimina un valor de la lista

nombres.pop() # elimina el ultimo elemento de la lista

del nombres[2] # elimina el indice indicado

nombres.clear() # elimina todos los elementos de la lista
print(nombres)
del nombres # elimina la lista


# Tuplas --> no son mutables, no se pueden modificar

cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)

print(len(cocina)) # cuantos elementos tiene la tupla

print(cocina[0]) # accedemos a x indice de la tupla

print(cocina[-1])

# accedemos a la tupla mediante un rango de elementos
print(cocina[ :1])
print(cocina[0:3])

# para q sea una tupla si o si necesita una coma, aunque sea un elemento
verduras = ("papas",)
print(verduras)

# iteramos en la tupla
for i in cocina:
    print(i) # print usa \n

for i in cocina:
    print(i, end=" ") # para evitar el salto de linea


# no se puede modificar las tuplas
'''
cocina[2] = "plato"
print(cocina)
'''
# la unica forma de modificarla es convirtiendo la tupla en lista y luego a tupla devuelta (no es buena practica)

cocinaLista = list(cocina)
cocinaLista[2] = "plato"
cocina = tuple(cocinaLista)
print('\n',cocina)

# eliminar la tupla
del cocina
print(cocina)