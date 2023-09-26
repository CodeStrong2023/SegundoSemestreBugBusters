# lista = Santiago , Ariel , Milagros , Osvaldo
'''

nombres = ["Mili", "Santi" , "Ariel"]
print (nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) #Solo muestra el indice 0, 1 pero no el indice 2
# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0, ,1, 2
#Desde el indice indicado hasta el final
print (nombres[1: ])
# Modificamos un valor
nombres[0] = "Milagors"
nombres[1] = "Santiago"
print(nombres)
# Iterrar una lista
for nombre in nombres : # Nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print (len(nombres)) #Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Marcelo")
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, "Alberto")
print(nombres)
nombres.insert(3, "Debora")
print (nombres)

# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
nombres.pop()
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres) # Aqui nos muestra un error
'''
'''
# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
# Ejemplo de ejecucion: 0,3,6,9
print("Rango de 0 a 10 con números divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimelos
# Ejemplo de ejecucion: 2,3,4,5,6
print("Rango con valores de inicio = 2 y fin = 6")
rango = range(2, 7)
for i in rango:
    print(i)

# Ejercicio 3: Crear un rango de 3 a 10 pero con un incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecucion: 3,5,7,9
print("Rango con valores de inicio = 3, fin = 10, incremento = 2")
for i in range(3, 11, 2):
    print(i)


#Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ("papa",) # Una tupla necesita aunque sea de un elemento la coma
# de lo contrario solo seria un tipo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end= " ") # Print esta usando /n para saltos de linea. Usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n" ,cocina)

del cocina
print(cocina)
'''

# Ejercicio Tuplas
#Dada la siguiente tabla
tupla = (13,1,8,3,2,5,8)
# Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 3, 2]

lista = [] # Definimos la lista
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)


