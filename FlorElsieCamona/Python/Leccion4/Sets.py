# Tipo Set
# manejo de datos que no pueden estar duplicados

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
print('Marte' not in planetas)
print('Jupiter' in planetas)

# Agregar un elemento
planetas.add('Tierra')  # add es una función
print(planetas)

# Eliminar elementos

planetas.remove('Jupiter')
print(planetas)
planetas.discard('Tierra')
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas














