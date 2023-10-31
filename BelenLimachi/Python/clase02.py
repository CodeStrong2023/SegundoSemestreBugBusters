# Tipo set 
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len (planetas)) # Usamos la funcion len (nos muestra el largo)

# Revisar si un elemento existe dentro de set
print( 'Marte' in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una funcion
print(planetas)

# Eliminar un elemento
planetas.remove("Jupiter") # Esta funcion si ingresas mal el elemento, la funcion no se ejecuta
print(planetas)

# Ingresas mal elemento se ejecuta igual 
planetas.discard('Tierra') # Esta funcion si ingresas mal el elemento, la funcion se ejecuta de todas maneras no presenta ningun error
print('tierra')

# Limpiar set
planetas.clear()
print(planetas)

# Elimar set o conjuntos
# del planetas
# print(planetas)

# Diccionario
# "Kun Aguero" : 10 Un diccionario esta compuestro por dos elementos una llave y un valor
# dict(key,value)
diccionario = { 
    "IDE" : "Integrated Development Environment" ,
    "POO" : "Programacion orientadas a objetos" ,
    "SABD" : "Sistema de administracion de base de datos"
}
# Verificiar la cantidad de elementos del diccionario
print(len(diccionario))

print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])

# Otra forma de recupar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# Modificamos elementos
diccionario["IDE"] = "Entorno de desarrollo integrado"
print(diccionario)

# Recorrer los elementos de un diccionario 
for termino in diccionario: # Recorrer mostrando solo las llaves
    print(termino)

for termino , valor in diccionario.items(): 
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algun elemento
print("IDE" in diccionario)

# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Para eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar diccionario 
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
# print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6 , 1]
lista3 = lista1 + lista2 # Concatenacion
print(lista3)

lista3.extend([7, 8 ,9, 1])
print(lista3) # Agrega mas elementos a la lista

print(lista3.index(5)) # Funcion para indicar en que indice esta el valor ubicado

# print(lista3.index(0)) Esto da un error por ser el elemento parte de la lista 

# Como saber cuantos valores repetidos hay en una lista 
print(lista3.count(1))

# Poner una lista al reves 
lista3.reverse()
print(lista3)

# Multiplicar una lista
lista3 = [lista3] * 2
print(lista3)

# Metodo de ordenamiento
lista3.sort() # Ordena los elementos ascendemente 
print(lista3)
lista3.sort(reverse = True) # Ordena los elementos descredentemente 
print(lista3)

# Repaso de tuplas 
tupla = (4, "hola mundo", 6.78, [1, 2 ,3 ], 4, "hola mundo") # Puede tener diferntes tipos de datos dentro
print(tupla)
print(4 in tupla) # Accion booleana 
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tuplas a listas, y de listas a tuplas 