#Ejercicio 1= Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
for numero in range(11):
    if numero % 3 == 0:
        print(numero)

#Crear un rango de numeros de 2 a 6 e imprimelos

for numero in range(2, 7):
    print(numero)

#Ejercicio 3= Crear un rango de 3 a 10 pero con incremento de 2 en 2
for numero in range(3, 11, 2):
    print(numero)

#Dada la siguiente tupla
tupla= (13,1,8,3,2,5,8) #definimos la tupla
# crear una lista que solo incluta los números menores a 5
lista_resultado = [numero for numero in tupla if numero < 5]
#e imprima por consola [1,3,2]
print(lista_resultado)

