# Ejercicio 6: Tabla de multioplicar
# Hacer un programa que puda un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

numero = int(input("Ingrese un numero: "))
lista = []
for i in range(1,11):
    lista.append(i*numero)
print(f'\n Tabla de multiplicasr del número {numero}: \n {lista}')
print('\n')
for indice,i in enumerate(lista):
    print(f'{numero} X {i} = {lista[indice]}')