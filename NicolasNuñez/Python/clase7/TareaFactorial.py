
# Tarea que el usuario ingrese el número para calcular el factorial.

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


numero = int(input("Ingrese un numero para conocer su factorial: "))

resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")