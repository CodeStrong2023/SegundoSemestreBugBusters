'''
# COLECCIONES EN PYTHON
# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores
# lista, = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Nati','Osvaldo','Liliana','Ariel']
print(nombres)
print(nombres[0])
print(nombres[3])
print(nombres[-1]) #para mostrar el ultimo elemento si no sabemos cuanto elementos hay
print(nombres[-2])

print(nombres[0:2]) #para recorrer hasta un determinado numero de indices -1
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1: ])

# MODIFICAMOS UN VALOR
#nombres[3] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# ITERAR UNA LISTA
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los nombres de la lista')

# PREGUNTAMOS CUANTOS ELEMENTOS TIENE UNA LISTA | FUNCION LEN
print(len(nombres)) # le pasamos como parametro la lista
# la funcion len se uiliza para devolver el numero de elementos en un objeto

# AGREGAMOS UN ELEMENTO | FUNCION APPEND
nombres.append('Marcelo') # append significa 'agregar' sirve para añadir elementos a una lista o estructura pero se agrega al final
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

# INSERTAR UN ELEMENTO EN UN INDICE ESPECIFICO
nombres.insert(1,'Alberto') # El primer argumento (entero) es el indice del elemento antes del cual se insertara el nuevo elemento
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

# ELIMINAMOS UN ELEMENTO
nombres.remove('Alberto') # Se utliza para eliminar el primer elemento de una lista que coincida con el valor especificado
print(nombres)

# ELIMINAMOS EL ULTIMO ELEMENTO
nombres.pop() # Elimina el ultimo elemento de la lista
print(nombres)

# ELIMINAR UN INDICE ESPECIFICO
del nombres[2] # DEL significa delete (eliminar)
print(nombres)

# ELIMINAR, BORRAR O LIMPIAR TODOS LOS ELEMENTOS
nombres.clear()
print(nombres)

# ELIMINAR LA LISTA
del nombres # Nos mostrara un error en consola como que la variable no esta definida
print(nombres)
'''

# Tupla:
# Definimos una tupla
cocina = ('Cuchara','Cuchillo','Tenedor')
#print(len(cocina))
'''
# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea un elemento, la coma.
# de lo contrario seria un tipo string o cadena
'''
# Recorremos los elementos de la tupla
for cocinar in cocina:
    # print(cocinar) # Print esta usando \n para saltos de lineas
    print(cocinar, end=' ') # Con la funcion end y colocando espacios dentro de las comillas eliminamos los saltos de lineas

ListaCocina = list(cocina) # La tupla pasa a ser una lista
ListaCocina[0] = 'Plato' # Le modificamos el dato que queremos
cocina = tuple(ListaCocina) # Lo pasamos de lista a tupla nuevamente
print('\n', ListaCocina) # Imprimimos el resultado, con \n volvemos a ponerlo en forma de columna
# Esto no es una buena practica dentro de programacion

# Para eliminar la tupla
# del cocina
# print(cocina)

# TIPO SET
'''Los conjuntos o sets son un tipo de coleccion que permite almacenar varios elementos de forma desordeanda, unica e inmutale
Es decir que no se puede acceder a los elementos por indices, que no se pueden repetir elementos y que no pueden modificar una vez
creados. Los conjuntos se pueden crear usando llaves {} o el constructor set(). En este conjunto no se pueden repetir elementos'''

planetas = {'Marte','Júpiter','Venus'}
print(len(planetas))

# Revisar si un elemento existe dentro del set
print('Marte' in planetas)
print('Júpiter' in planetas)

# Agregar un elemento | FUNCION ADD
planetas.add('Tierra')
print(planetas)

# Eliminar elementos | FUNCION REMOVE (puede arrojar un error si el elemnto no existe)
planetas.remove('Júpiter') # Esta funcion ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard('tierra') # Esta funcion no nos presenta ningun error
print(planetas)

# Limpiar set | FUNCION CLEAR
planetas.clear()
print(planetas)

# Eliminar set | FUNCION DEL
# del planetas
# print(planetas)

# DICCIONARIOS
'''Los diccionarios son colecciones sin orden, modificables e indexadas que no permiten elementos duplicados. Se crean
especificando los elementos como pares de clave-valor entre llaves y separados por comas. dict(key,value)'''
# Ejemplo Maradona: 10
diccionario = {
    "IDE" : "Integrated Development Enviroment",
    "POO" : "Programacion Orientada a Objetos",
    "SABD" : "Sistema de Administracion De Datos"
}
print(len(diccionario))
print(diccionario)

# Accedemos a un elemento del diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario .get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los terminos
for termino in diccionario: # Recorremos mostrando las llaves
    print(termino)

for termino, valor in diccionario.items():
    print(termino,valor)

# Otras maneras de accerder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # Devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminamos un elemento
diccionario.pop('SABD')
print(diccionario)

# vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
# del diccionario
# print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) # Esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de la lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves la lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento en listas
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

# Repaso de tuplas
tupla = (4, 'hola', 6.78, [1,2,78], 'Como estas?')
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
'''Lo que podemos usar dentro de las tuplas son: index, count, len
En tuplas se puede convertir de tupla a lista y  de lista a tupla'''
