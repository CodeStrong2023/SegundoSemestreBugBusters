'''
Ejercicio 6: Modificar los elementos de una lista.
Llenar una lista con los numeros del 1 al 10, luego modificar los elementos
de la lista multiplicandolos por un valor ingresado por el usuario
'''

lista = list(range(1,11))

print(f"Lista original: {lista}")

num = int(input("Digite un valor a multiplicar: "))

# multiplicamos los elementos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= num

print(f"lista final con los elmentos multiplicados por {num}")
for i in lista:
    print(i, end="-")