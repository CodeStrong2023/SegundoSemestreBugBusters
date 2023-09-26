# Repaso diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Eliminar un elemento
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

# Otro ejemplo de diccionario
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '9 Millones', 'Posicion': 'Extremo derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media punta'},
    19: {'Nombre': 'Nico Otamendi', 'Edad': 28, 'Altura': 1.77, 'Precio': '3 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
}

# Imprimir un dato del diccionario
print(seleccionArgentina[10])

# Imprimir todos los valores de un diccionario
print(seleccionArgentina.values())

# Ciclo for para imprimir datos del diccionario
# Solo llaves
for numero in seleccionArgentina:
    print(numero)

# Todos los valores
for valor in seleccionArgentina.values():
    print(valor)

# Llaves y valores
for numero, valor in seleccionArgentina.items():
    print(numero, valor)

# Tarea: agregar por lo menos 4 jugadores más al diccionario seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de: ', end=' ')
print(len(seleccionArgentina))

seleccionArgentina2 = {
    9: {'Nombre': 'Julián Álvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '13 Millones', 'Posicion': 'Delantero'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 29, 'Altura': 1.77, 'Precio': '22 Millones', 'Posicion': 'Mediocampista'},
    23: {'Nombre': 'Emiliano Martinez', 'Edad': 3, 'Altura': 1.95, 'Precio': '29 Millones', 'Posicion': 'Portero'},
    22: {'Nombre': 'Lautaro Martinez', 'Edad': 26, 'Altura': 1.77, 'Precio': '10 Millones', 'Posicion': 'Delantero'},
}

seleccionArgentina = seleccionArgentina | seleccionArgentina2
print(len(seleccionArgentina))

for numero, valor in seleccionArgentina.items():
    print(numero, valor)

