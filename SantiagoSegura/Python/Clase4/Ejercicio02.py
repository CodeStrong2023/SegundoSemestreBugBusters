# Ejercicio 2: Modificar los elementos de una lista
# Lllenar una lista con los numeros del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
print('Lista Origianl')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar: '))
# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista): # Funcion para modificar los indices de la lista
    lista[indice] *= valor # El iterador solo recorre los indices de la lista
print(f'lista final con los elmentos multiplicados por {valor}')
for i in lista:
    print(i, end='-')

