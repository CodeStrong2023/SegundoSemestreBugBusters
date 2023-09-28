
'''
Ejercicio 7: Insertar elementos y ordenarlos.
Pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0,
nuestro programa dejará de insertar. Por ultimo, mostrar los numeros ordenados
de menor a mayor.
'''

lista = []
num = int(input("Ingrese un numero: "))
while num != 0:
    lista.append(num)
    num = int(input("Ingrese otro numero: "))
else:
    print("Se ha introducido un cero. El programa finaliza!")

lista.sort()
for i in lista:
    print(f"{i}", end=",")