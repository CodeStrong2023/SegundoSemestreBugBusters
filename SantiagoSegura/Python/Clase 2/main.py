# Tipo set

planetas = {'Marte', 'Júpiter', 'Venus'}

print(len(planetas)) # Usamos la función len = lenght significa largo

# Revisar si un elemento existe dentro de set
print('Júpiter' not in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') # Esta funcion ante un mal ingreso u inexistencial del elemento da error
print(planetas)
planetas.discard('tierra') # Esta funcion no nos presenta ningun error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas)

# 'Maradona' : 10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value)
diccionario = {
    'IDE':'Integrated Develoment Enviromment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Baste de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos solo las llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una funcion
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): #Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # Devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'

# Elimianr un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # El diccionario se borro

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenación
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para indicar en que indice esta el valor ingresado
#print(lista3.index(0)) # Esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores hay repetidos en una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de una lista

# Para poner nuestra lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [lista3] * 2
print(lista)

# Metodo de ordenamiento, en python es una función
lista3.sort() # Oredena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

# Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla






















