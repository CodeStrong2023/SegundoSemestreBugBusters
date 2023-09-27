# lista
# Colecciones en Python

# Las listas se conoce en otro lenguajes como arreglos o vectores

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
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
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

# Tipo set o conjunto
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas))  # Usamos la funcion len = length significa largo

# Revisar si un elemento existe dentro de set
print("Marte" in planetas)

# Agregar un elemento
planetas.add("Tierra")  # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Jupiter")  # Esta función ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard("tierra")  # Esta función no nos presenta nungun error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas


# DICCIONARIO
# 'Maradona':10 Un diccionario está compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
# Verificar la cantida de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))  # Get = Obtener
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:  # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():  # Estamos usando una función
    print(termino)  # Muestra solo las llaves

for valor in diccionario.values():  # Usamos una función para acceder al valor
    print(valor)

# Comprobaos la existencia de elementos
print('IDE' in diccionario)  # Devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un dicionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario  # el diccionario se borró


# CONCATENAR LISTAS
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1])  # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # Funcion para ubicar en que indice esta el valor en la lista, si no está da error

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))

# Poner al reves la lista
lista3.reverse()
print(lista3)

# Para que una  lista se multiplique repitiendo sus elementos
lista = lista3 * 2
print(lista)

# Métodos de ordenamiento
lista3.sort()  # Ordena ascendentemente
print(lista3)
lista3.sort(reverse=True)  # Ordena Descendentemente
print(lista3)

tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, "Hola")
print(tupla)

print(4 in tupla)  # Acción booleana, respuesta tipo booleana
"""
Podemos usar dentro de tuplas: index, count, len
En tuplas se puede convertir de tupla a lista y de lista a tupla
"""

# Repaso de set o conjuntio
# para definir un conjunto -> Grupos de elementos desordenados
conjunto1 = set()
conjunto2 = {'bye', }
conjunto1.add(7)
conjunto1.add('Hola')
print(conjunto1)
conjunto2.add('hola')
print(conjunto2)
print(3 not in conjunto2)  # Preguntamos si el numero 3 NO está en conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)  # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2  # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  # Que elemento tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2  # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))  # asi preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, eso es si no comparten elementos en común
print(conjunto1.isdisjoint((conjunto2)))  # No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset  # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto
"""
"""
# REPASO DICCIONARIO
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)
# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'David': {'Edad': 22, 'Altura': 1.73}, 'Ariel': [40, 1.83], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    24: {'Nombre': 'Enzo Fernandez', 'Edad': 22, 'Altura': 1.78, 'Precio': '80 Millones', 'Posicion': 'Pivote'},
    9: {'Nombre': 'Julian Álvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '60 Millones', 'Posicion': 'Delantero Centro'},
    20: {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.76, 'Precio': '65 Millones', 'Posicion': 'Mediocentro'},
}
#otra forma de añadir elementos
seleccionArgentina[22] = {'Nombre': 'Lautaro Martinez', 'Edad': 26, 'Altura': 1.74, 'Precio': '85 Millones', 'Posicion': 'Delantero Centro'}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario una cantidad de ', (len(seleccionArgentina)), ' jugadores. ')

# METODO CON LISTAS LLAMADO PILAS
# Pilas usando Listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()  # Quitamos el ultimo elemento y lo guardo en la variable
print(f'Scamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedó así: {pila}')

# METODO CON LISTAS LLAMADO COLA
# Colas con Listas
# Estructura de datos de tipo fifo( first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
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



