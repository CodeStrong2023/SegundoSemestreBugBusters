#Ejercicio 1: Sumar numeros pares dentro de un rango

num1 = int(input('Ingrese un numero'))
num2 = int(input('Ingrese otro numero'))
print('Los numeros pares dentro de ese rango son:')

for i in range(num1,num2):
    if(i%2==0):
        print(i, end=' ')
