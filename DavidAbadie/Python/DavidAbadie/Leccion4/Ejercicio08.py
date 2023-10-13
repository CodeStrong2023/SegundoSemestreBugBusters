# Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# inicial de $1000 y tendrá el siguiente menu de opciones:
#   1. Ingresar dinero en la cuenta
#   2. Retirar dinero de la cuenta
#   3. Mostrar dinero disponible
#   4. Salir
saldo = 1000
while True:
    print('\n\t:: MENU ::')
    print('\t1. Ingresar dinero en la cuenta')
    print('\t2. Retirar dinero de la cuenta')
    print('\t3. Mostrar dinero disponible')
    print('\t4. Salir')
    opcion = int(input('\nIngrese una opción: '))

    if opcion == 1:
        ingresa = int(input('\nIngrese cantidad de dinero a depositar: '))
        saldo += ingresa
    elif opcion == 2:
        retira = int(input('\nIngrese cantidad de dinero a retirar: '))
        saldo -= retira
    elif opcion == 3:
        print(f'\nDinero disponible: ${saldo}')
    elif opcion == 4:
        print('\nSaliendo...')
        break
    else:
        print('\nOpcion incorrecta')
        print()


