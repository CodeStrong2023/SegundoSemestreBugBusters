def suma_numeros(*args):
    suma = 0
    for numero in args:
            suma += numero
    return suma

print(suma_numeros(1, 2, 3, 4, 5))

