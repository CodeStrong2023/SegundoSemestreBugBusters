# Colecciones en Python
# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

# lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Nati', 'Osvaldo', 'Lily', 'Ariel']
# Lista nombres
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])

# Lista nombres inverso
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[0])

print(nombres)
print(nombres[:2])  # Muestra desde el índice 0 al 2 pero no lo incluye
print(nombres[0:3])
print(nombres[1:])  # Muestra desde el índice indicado hasta el final

nombres[2] = "Liliana"
print(nombres)

nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista

for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print("No hay mas nombres en la lista")

# Calcular cantidad de elementos de una lista

print(len(nombres))  # le pasamos como parametro la lista con -len-

# Agregamos un elemento al final de la lista con -append-

nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append(7)
print(nombres)

# Insertar un elemento en un índice específico con -insert-

nombres.insert(1, 'Alberto')
print(nombres)

nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento con -remove-

nombres.remove('Alberto')
print(nombres)

# Eliminamos el último elemento de la lista con -pop-

nombres.pop()
print(nombres)

# Eliminamos un índice específico con -del-

del nombres[2]
print(nombres)

# Eliminar, borrar o limpiar todos los elementos con -clear-
nombres.clear()
print(nombres)

# Eliminar la lista con -del-

del nombres
