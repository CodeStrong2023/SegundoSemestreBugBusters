# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el numero 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta bolueano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tiene ne común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Son los elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto 3 es un subconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en común

# Convertir un conjunto totalmente inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso de Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Santiago': {'Edad': 19, 'Altura': 1.68}, 'Ariel': [40, 1.83], 'Victoria': [18, 1.65]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posición': 'Extremo' },
    11: {'Nombre': 'Ángel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '40 Millones', 'Posición': 'Extremo Derecho' },
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posición': 'Media Punta' },
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '25 Millones', 'Posición': 'Defensa' },
    1:  {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '4 Millones', 'Posición': 'Arquero' },
    4:  {'Nombre': 'Gonzalo Montiel', 'Edad': 26, 'Altura': 1.75, 'Precio': '12 Millones', 'Posición': 'Defensor' },
    9:  {'Nombre': 'Julián Álvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '30 Millones', 'Posición': 'Delantero' },
    8:  {'Nombre': 'Enzo Fernández', 'Edad': 22, 'Altura': 1.78, 'Precio': '45 Millones', 'Posición': 'Medio Campista' },
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#  Como tarea agregar 3 jugadores
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end= '' )
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la fila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora queda así: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo (first input / first output
cola = ['Ariel', 'Santiago', 'Milagros', 'Bruno']

# Agregamos elementos al final de la cola
cola.append('Candela')
cola.append('Maxi')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')












