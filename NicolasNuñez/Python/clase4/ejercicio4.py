
'''
Ejercicio 4: Sacar la raiz cuadrada de un nunero positivo
'''

import math

num = int(input("Ingrese un numero: "))

while num <= 0:
    print("Error. Debes ingresar un numero positivo")
    num = int(input("Ingrese un numero: "))

raiz = math.sqrt(num)
print(f"La raiz cuadrada de {num} es {raiz:.2f}")