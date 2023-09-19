'''
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
