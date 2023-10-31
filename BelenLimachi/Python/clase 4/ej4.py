import math # Importamos clase math para hacer uso de la función sqrt(raíz cuadrada)
# Ejercicio de matematicas
# Para sacar la raíz cuadrada de un numero positivo 
numero = int(input("Digite un numero positivo: "))
while numero < 0:
    print("Error el numero debe ser un numero positivo")
    numero = int(input("Digite un numero positivo: "))
    
print(f'\nSu raiz cuadrada es:{math.sqrt(numero):.2f}') # .2 para que no nos largue un numero tan largos