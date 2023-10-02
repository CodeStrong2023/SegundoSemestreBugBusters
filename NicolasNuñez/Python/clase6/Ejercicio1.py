
'''
Ejercicio 1: No repetir caracteres
HAcer un programa que pida una cadena por teclado, luego meter los caracteres
en una lista sin repetir caracteres
'''

cadena = input("Ingrese una cadena de texto: ")
list = []

for i in cadena:
    if i not in list:
        list.append(i)

print(f"Lista de caracteres sin repetir ninguno: \n{list}")