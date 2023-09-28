# Un diccionario está compuesto por dos elementos:
# una llave y un valor
# ejemplo
# 'Maradona': 10
# dict(key, value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación orientada a objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}

# Verificar la cantidad de elementos del diccionario

print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de acceder a un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
# Ciclo for

for termino in diccionario:
    print(termino)  # Nos muestra las llaves

# Necesitamos una funcion para recorrer un diccionario

for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario

for termino in diccionario.keys():
    print(termino)  # Muestra solo las llaves

for valor in diccionario.values():
    print(valor)  # Usamos una función para acceder al valor

# Comprobar la existencia de algun elemento
print('IDE' in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)


# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario  # el diccionario se borro






