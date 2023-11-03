'''
Ejercicio 3: insertar elementos y ordenarlos
pedir números y meterlos en una lista, cuando el usuario
Introduzca un número 0, nuestro programa dejaría de insertar
Por último, mostrar los números ordenados de menor a mayor
'''
lista = []
salir = False
while not salir:
    numero = int(input('Digite un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista esta ordenada con esta función
print(f'\nLista ordenada: \n{lista}')
