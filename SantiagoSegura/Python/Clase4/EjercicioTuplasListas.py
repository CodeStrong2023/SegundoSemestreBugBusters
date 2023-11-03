import math # Improtamos la clase math para hacer uso de la funcion sqrt (raiz cuadrada)
# Dada la siguiente tabla
tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la tupla
# Crear una lista que solo incluya los numeros menores a 5
# e importa por consola [1, 3, 2]

lista = [] # Definimos fila lista
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
        print(lista)

# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un numero positivo: '))
while numero < 0:
    print('Error -> Debería ser un numero positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')