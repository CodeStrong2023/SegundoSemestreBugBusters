# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprime nada



def imprimir_descendente(numero):
    if numero <= 0:
        return
    else:
        print(numero)
        imprimir_descendente(numero - 1)

imprimir_descendente(5)  # Imprimirá los números de 5 a 1
