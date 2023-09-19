
# Repaso de set o conjuntos

# Para definir un conjunto vacio
conjunto = set() # Para inicializar un conjunto vacio

conjunto1 = {} # no se puede añadir elementos con la funcion add si el conjunto a sido inicializado como vacio con las llaves {}
conjunto2 = {"hola",}
conjunto.add(7)
conjunto.add("Hola")
print(conjunto)

# conjunto1.add(9) # no se puede añadir elementos a un conjunto que ya a sido inicializado como vacio con las llaves
print(conjunto1)

conjunto2.add("Bye")
print(conjunto2)

print(3 not in conjunto1)

print(conjunto == conjunto1) # igualdad de dos conjuntos

# Operaciones en conjuntos
conjunto3 = conjunto | conjunto2 # Unir dos conjuntos
print(conjunto3)

conjunto3 = conjunto & conjunto2 # que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto - conjunto2 # Asigna el valor que esta en el conjunto y no en el conjunto 2
print(conjunto3)

conjunto3 = conjunto2 - conjunto
print(conjunto3)

conjunto3 = conjunto ^ conjunto2
print(conjunto3) # Elementos que no comparten o son diferentes entre ambos

conjunto3 = conjunto | conjunto2
print(conjunto2.issubset(conjunto3)) # si un conjunto es un subconjunto dentro de otro
print(conjunto.issubset(conjunto3))
print(conjunto3.issubset(conjunto))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto)) # Preguntamos si los elementos del conjunto estan dentro del 3
print(conjunto3.issuperset(conjunto2)) #  Preguntamos si los elementos del conjunto2 estan dentro del 3

# como saber si los conjuntos son disconexos, que no comparten elementos
print(conjunto.isdisjoint(conjunto2))

# convertir un conjunto totalmente en inmutable
conjunto = frozenset # Esto hace que el conjunto sea inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso de Diccionarios

diccionario_nuevo = {
    "Azul" : "Blue",
    "Rojo" : "Red",
    "Verde" : "Green",
    "Amarillo" : "Yellow"
}
print(diccionario_nuevo)

# como eliminar
del(diccionario_nuevo["Azul"])
print(diccionario_nuevo)

# Los diccionarios puede almacenar diferentis tipos de datos
diccionario2 = { "Nicolas" : {"Edad" : 21, "Altura" : 1.80}, "Osvaldo" : [45, 1.85], "Natalia" : [35,1.67]}
print(diccionario2)