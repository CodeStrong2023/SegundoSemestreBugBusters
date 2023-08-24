# Definimos una tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')

# Imprimimos la tupla y la cantidad de elementos que tiene con -len-

print(cocina)
print(len(cocina))

# Acceder a un elemento de la tupla, se utilizan los corchetes y no parentesis

print(cocina[0]) # Nos muestra el índice 0 de la tupla

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

