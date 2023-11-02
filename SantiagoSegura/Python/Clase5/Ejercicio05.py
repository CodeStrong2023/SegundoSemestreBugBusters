# Ejercicio 5: Factorial de un numero positivo
# Hacer un programa para calcular el factorial de un numero positivo

numero = int(input("Digite un numero: "))
while numero < 0: # Mientras el numero sea negativo
    print("Error -> El numero tiene que ser positivo")
    numero = int(input("Digite un numero: "))
factorial = 0 # La variable para calcular el factorial
for i in range(1, numero+1):
    factorial *= i
print(f"\nEl factorial del {numero} positivo ingresado es: {factorial}")
