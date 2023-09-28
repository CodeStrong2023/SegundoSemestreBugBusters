lista = []
def ingresarNumeros():
    while True:
        numero = round(float(input('Ingrese un numero mayor a 0 o 0 para terminar')))
        if numero == 0:
            break
        lista.append(numero)

    lista.sort()
    print(lista)

ingresarNumeros()