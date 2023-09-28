
'''
Ejercicio 1: Sumar numeros pares dentro de un rango.
Hacer un programa para sumar numeros pares dentro de un rango, por ejemplo:
suma de numeros pares del 2 al 30
suma = 240
'''

num1 = int((input("Ingrese el primer numero del rango: ")))
num2 = int((input("Ingrese el segundo numero del rango: ")))

suma = 0

for i in range(num1 - 1, num2 + 1):
    if i % 2 == 0:
        suma += i


print(f"La suma da {suma}")