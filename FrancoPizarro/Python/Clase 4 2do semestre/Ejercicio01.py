# Ejercicio 1: llenar una lista
'''
Llenar una lista con los números del 1 al 50, luego mostra
la lista con el bucle for, los elementos deben mostrarse
de la siguiente forma:
1-2-3-4-5-...50

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i, end='-')
'''
lista = list(range(1, 51))
for i in lista:
    print(i, end='-')
