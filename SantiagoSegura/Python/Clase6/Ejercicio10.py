# Ejercicio 10: no repetir caracteres
# hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

cadena = input ('Digite una cadena: ')
lista = []
for i in cadena:
    if i not in lista: # Si el caracter aun no esta en la lista
        lista.append(i) # Lo agregamos a la lista
print (f'\Lista de caracteres sin repetir ninguno: \n {lista}')



