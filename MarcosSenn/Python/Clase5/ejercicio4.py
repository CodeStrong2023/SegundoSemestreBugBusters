import random
def juegoNumAleatorio():
    numeroAleatorio = random.randint(0, 100)
    numUsuario = int(input('Adivine el numero entre 0 y 100'))

    while True:
        if (numUsuario == numeroAleatorio):
            print('ADIVINASTE')
            break
        elif (numUsuario > numeroAleatorio):
            print('El numero ingresado es mayor que el numero a adivinar')
            numUsuario = int(input('Intenta con un numero menor'))

        else:
            print('El numero ingresado es menor que el numero a adivinar')
            numUsuario = int(input('Intenta con un numero mayor'))

juegoNumAleatorio()