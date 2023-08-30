# Definimos una tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')

# Imprimimos la tupla y la cantidad de elementos que tiene con -len-

print(cocina)
print(len(cocina))

# Acceder a un elemento de la tupla, se utilizan los corchetes y no parentesis

print(cocina[0])  # Nos muestra el índice 0 de la tupla

# Mostrar de manera inversa el ultimo elemento

print(cocina[-1])

# Acceder a un rango

print(cocina[0:3])

# Ejemplo

verduras = ('papa', )  # Una tupla necesita la coma aunque solo haya un elemento, si no sería un tipo cadena (str)
print(verduras)

# El comando print está usando saltos de línea, agregamos end para que se ejecute en una línea solamente

for cocinar in cocina:
    print(cocinar, end=' ')

# En caso de tener que modificar una tupla es convertirla en lista (-list-) y luego a tupla nuevamente

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print(cocina)

# Para eliminar la tupla, es igual a eliminar una lista con -del-

del cocina

# Concatenar listas

lista1= [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

# Agregamos más elementos a la lista3
lista3.extend([7, 8, 9, 1])
print(lista3)

# Funcion para ubicar en que índice está el valor ingresado

print(lista3.index(5))

# print(lista3.index(0)) esto daria un error por no ser el elemento parte de la lista // diferencia con arreglos

# Buscar valores repetidos dentro de una lista
print(lista3.count(1))  # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista

lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento > de forma ascendente
lista3.sort()
print(lista3)

lista3.sort(reverse=True)   # Ordena descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')    # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Busca el elemento 4 de la lista

print(5 not in tupla)


