# Colecciones

# Listas --> conjunto de elementos (pueden ser de diferentes tipos de datos) son mutables, se pueden modificar
# Listas -> Arreglos y vectores en otros lenguajes

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
# Podemos agregar diferentes tipos de datos
nombres.append([1,2,3]) # podemos tener otra lista dentro de la lista
nombres.append(True)
nombres.append(2.45)
nombres.append([5,22])
nombres.append(356)
print(nombres)

nombres.insert(3,"Mariana") # agrega un elemento en el indice especificado

nombres.remove("Sofia") # elimina un valor de la lista

nombres.pop() # elimina el ultimo elemento de la lista

del nombres[2] # elimina el indice indicado

nombres.clear() # elimina todos los elementos de la lista
print(nombres)
del nombres # elimina la lista

# Concatenar listas

lista1 = [1,2,3]
lista2 = [4,1,6]
lista3 = lista1 + lista2
print(lista3)

# Extender la lista
lista3.extend([7,8,1])
print(lista3)

print(lista3.index(7)) # en que indice se encuentra x elemento

# Como saber cuantos valores repetidos hay en una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay en la lista

# Para poner nuestra lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista4 = [1,2,3] * 2
print(lista4)

# Métodos de ordenamiento
lista3.sort() # ordena ascendentemente la lista
print(lista3)

lista3.sort(reverse = True) # Ordena descendentemente la lista
print(lista3)



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

# La tupla puede almacenar diferentes tipos de datos
tupla = (24,"Hola", 64.021, False, ["Hello", "Goodbye"], 24, "letra")
print(tupla)

# Buscar un elemento
print(24 in tupla)
print("letra" not in tupla)

print(len(tupla)) # metodo len

print(tupla.index("Hola")) # metodo index. En que indice se encuentra el valor que le pasamos

print(tupla.count(24)) # metodo count. Cuenta cuantos valor iguales hay en la tupla
