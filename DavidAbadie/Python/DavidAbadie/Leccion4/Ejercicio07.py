# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un número. Para ello se debe generar
# un numero aleatorio entre 1 - 100, y luego ir pidiendo numeros indicando
# "es mayor" o "es menor según sea mayor o menor con respecto a N.
# El proceso termina cuando el usuario acierta y alli se debe mostrar el
# numero de intentos.
import random
print('\t :: JUEGO ADIVINA EL NUMERO ::')
aleatorio = random.randint(0, 100)  # Toma de 0 a 100 literal
intentos = 0
while True:
    numero = int(input('Ingrese un numero: '))
    intentos += 1
    if numero > aleatorio:
        print('\tIngrese un numero menor')
    elif numero < aleatorio:
        print('\tIngrese un numero mayor')
    else:
        print(f'\tFELICIDADES!! Adivinaste el número {aleatorio}')
        break  # rompe el ciclo y el bucle
print(f'\nNumero de intentos: {intentos}')
