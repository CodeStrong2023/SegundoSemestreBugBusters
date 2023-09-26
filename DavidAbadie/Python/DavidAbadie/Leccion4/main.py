# lista

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
"""
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])  # Muestra el último elemento
print(nombres[-2])  # penultimo
"""
print(nombres)
print(nombres[0:2])  # Solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])  # indices a mostrar 0, 1, 2
# desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[3] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# iterar una lista
for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# preguntamos cuantos elementos tiene
print(len(nombres))  # le pasamos como parametros la lista

# Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

# Insertamos un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]  # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar lista
del nombres

# TUPLA
# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto se usa corchetes no parentesis
print(cocina[0])
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ('papa',)  # una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo seria un tipo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=" ")  # Imprimir sin salto de linea
# No es una buena práctica convertir de tupla a lista y viceversa
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

# del cocina: Esto es para eliminar la tupla
