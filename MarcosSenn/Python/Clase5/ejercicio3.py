#Ejercicio 3: Pedir un numero por teclado y guardar en una lista su tabla de multiplicar.
num = int(input('Ingrese un numero'))
tabla = []
for i in range(11):
    print(num*i, end=(' '))