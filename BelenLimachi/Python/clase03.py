# Para definir un conjunto
conjunto2 = set()
conjunto1 = {'Bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print( 3 not in conjunto1) # Preguntamos si el numero 3 no esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve un valor booleano

# Operaciones en conjunto
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos 
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Muestra el elemento que tienen en comun 
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el cojunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Son los elementos que estan en los conjuntos pero no estan en ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Preguntamos si un conjunto es un subconjunto del otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto


# Repaso de diccionario
diccionario = {'Azul' : 'Blue', 'Rojo' : 'Red', 'Verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionario)

# Eliminamos un elemento
diccionario.pop('Azul')
print(diccionario)

# Los diccionarios pueden almacenar diferentes tipos de datos 
diccionario2 = {'Ariel' : {'Edad' : 40, 'Altura' : 1.83 }, 'Osvaldo' : [52, 1.85], 'Natalia' : [38, 1.65]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre' : 'Lionel Messi', 'Edad' : 36, 'Altura': 1.70, 'Precio': '70 Millones', 'Posicion' : 'Medio Campista Ofensivo'},
    11: {'Nombre' : 'Angel DiMaria', 'Edad': 35, 'Altura': 1.80, 'Precio': '40 Millones', 'Posicion': 'Extremo'},
    9: {'Nombre': 'Julian Alvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '150 Millones', 'Posicion': 'Delantero'},
    5: {'Nombre': 'Rodrigo De Paul', 'Edad': 29, 'Altura': 1.80, 'Precio' : '60 Millones', 'Posicion': 'Medio Campista'},
    20: {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.76, 'Precio': '90 Millones', 'Posicion': 'Medio Campista'},
    8: {'Nombre': 'Enzo Fernandez', 'Edad': 22, 'Altura': 1.78, 'Precio': '120 Millones', 'Posicion': 'Medio Campista'},
    26: {'Nombre': 'Nahuel Molina', 'Edad': 25, 'Altura': 1.75, 'Precio': '50 Millones', 'Posicion': 'Lateral Derecho'},
    13: {'Nombre': 'Cristian Romero', 'Edad': 25, 'Altura': 1.85, 'Precio': '70 Millones', 'Posicion': 'Defensa Central'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 35, 'Altura': 1.83, 'Precio': '10 Millones', 'Posicion': 'Defensa Central'},
    3: {'Nombre': 'Nicolas Tagliafico', 'Edad': 31, 'Altura': 1.72, 'Precio': '30 Millones', 'Posicion': 'Lateral Izquierdo'},
    23: {'Nombre': 'Emiliano Martinez', 'Edad': 31, 'Altura': 1.95, 'Precio': '50 Millones', 'Posicion': 'Arquero'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print("Tenemos cargado en el diccionario la cantidad de jugadores: ", end = " ")
print(len(seleccionArgentina))


# Pilas usando lista
pila = [1, 2, 3]
# Agregar elementos a la pila por el final 
pila.append(4)
pila.append(5)
print(pila)
# Eliminamos el ultimo elemento
elementoBorrado = pila.pop()
print(f'Borramos el ultimo elemento {elementoBorrado}')
print(f'Ahora la pila quedo asi: {pila}')

# Colas con lista
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Gabriel']
# Agregamos elementos al final de la cola
cola.append('Lionel')
cola.append('Julian')
print(cola)
# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Otra forma de ejecutar el diccionario, con el ciclo for 
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')