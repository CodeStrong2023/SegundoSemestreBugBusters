'''
Ejercicio 5: Menú interactivo - cajero automático
Hacer un programa que simule un cajero automatico con un saldo inicial de 1000$
y tendrá el siguiente menú de opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4 Salir
'''

saldo_actual = 1000

while True:
    print("Eliga una opcion del menu: ")
    print("""
    1. Ingresar dinero en la cuenta
    2. Retirar dinero de la cuenta
    3. Mostrar dinero disponible
    4. Salir""")
    opc = int(input())

    if opc == 1:
        ingreso = float(input("Cuanto dinero desea ingresar: "))
        saldo_actual += ingreso
        print(f"Su saldo actual es de {saldo_actual}")

    elif opc == 2:
        retiro = float(input("Cuanto dinero desea retirar: "))
        if retiro > saldo_actual:
            print("No tiene esa cantidad de dinero en su cuenta ")
        else:
            saldo_actual -= retiro
            print(f"Su saldo actual es de {saldo_actual:2f}")

    elif opc == 3:
        print(f"Su saldo actual es de {saldo_actual}")

    elif opc == 4:
        print("Gracias por utilizar el cajero automatico")
        break
    else:
        print("Numero incorrecto.")