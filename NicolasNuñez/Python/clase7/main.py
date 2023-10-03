# Funciones Recursivas = caso base / caso recursivo

def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero - 1) # Caso recursivo

resultado = factorial(5)
print(f"El factorial de 5 es {resultado}")