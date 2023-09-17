
'''
Ejercicio 5: LLenar una lista con los numeros del 1 al 50.
Luego mostrar la lista con un bucle for, los elementos deben
mostrarse de la siguiente manera: 1-2-3-4-5...-50
'''

lista = []

# llenamos la lista
for i in range(1,51):
    lista.append(i)

# mostramos la lista
for num in lista:
    print(f"{num}-", end="")

'''
lista = list(range(1,51))
for i in lista:
    print(f"{i}, end"-"
'''