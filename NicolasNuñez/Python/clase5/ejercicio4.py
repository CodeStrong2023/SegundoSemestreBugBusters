'''
Ejercicio 4: Juego adivina el número
Realizar un juego para adivinar un número. Para ello se debe generar un número aleatorio entre
1-100 y luego ir pidiendo números indicando "es mayor" o "es menor" segun corresponda.
El proceso termina cuando el usuario acierta y allí se debe mostrar el número de intentos.
'''

import random

num_aleatorio = random.randint(1,100)

intentos = 0

print("¡¡Adivina el numero!!")
num = int((input("Ingrese un numero: ")))
while num != num_aleatorio:
    if num > num_aleatorio:
        print("Es menor")
        intentos += 1
        num = int((input("Ingrese un numero: ")))
    elif num < num_aleatorio:
        print("Es mayor")
        intentos += 1
        num = int((input("Ingrese un numero: ")))
else:
    intentos += 1
    print("ADIVINASTE!!")
    print(f"Adivinaste en {intentos} intentos")