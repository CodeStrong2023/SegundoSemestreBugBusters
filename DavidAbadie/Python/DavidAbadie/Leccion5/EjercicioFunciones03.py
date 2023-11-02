'''
Ejercicio 3: Funcion recursiva
Imprimir números del 5 al 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, por ejemplo, si pasaos el valor de 5, debe imprimir:
5
4
3
2
1
En caso de ingresar números negativos no imprime nada.
'''

def imprimir_numeros(numero):
    if numero >= 1: # Caso base
        print(numero)
        imprimir_numeros(numero - 1) # Caso recursivo

imprimir_numeros(5)

# Tarea: que el usuario ingrese el número

def imprimir_numeros2(num):
    if num >= 1:
        print(num)
        imprimir_numeros2(num - 1)
    elif num == 0:
        return
    elif num <= 0:
        print("Valor ingresado invalido")

numero = int(input("Ingrese un número: "))
imprimir_numeros2(numero)