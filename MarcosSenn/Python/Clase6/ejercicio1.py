#pedir una cadena por teclado y meter los caracteres en una lista sin repetirlos
cadena = str(input("Ingrese una frase"))
def cadenaSinRepetir(cadena):
    lista = []
    for letra in cadena:
       lista.append(letra)

    listaSinRepetir = set(lista)
    print(listaSinRepetir)

cadenaSinRepetir(cadena)