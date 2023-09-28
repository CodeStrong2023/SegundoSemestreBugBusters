'''
Ejercicio 2: Factorial de un numero positivo.
Hacer un programa para calcular el factorial de un numero positivo
EJ: 5! = 5x4x3x2x1 = 120
'''

num = int((input("Ingrese un numero: ")))

factorial = 1

for i in range(num, 0, -1):
    factorial *= i

print(f"El factorial de {num} es {factorial}")