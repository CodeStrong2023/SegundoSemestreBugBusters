import math  # Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluyta los números menores a 5
# e imprima por consola [1, 3, 2]
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio de Matematicas
# PAra sacar la raiz cuadrada de un numero positivo
numero = int(input("Ingrese un número positivo: "))
while numero<0:
    print("Error <- Debería ser un número positivo")
    numero = int(input("Ingrese un número positivo: "))
print(f"\n Su raíz cuadrada es: {math.sqrt(numero):.2f}")  #.2f redondea a los proximos dos decimos
