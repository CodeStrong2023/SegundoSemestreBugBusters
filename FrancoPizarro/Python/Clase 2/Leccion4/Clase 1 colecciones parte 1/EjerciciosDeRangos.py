# Ejercicio 1: iterar un rango de 0 a 10 e imprimir numero divisibles entre 3
# Ejemplo de ejecucion: 0, 3, 6 ,9
print('Ejercicio 1: 0 3 6 9')
for i in range(0,10):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: crear un rango de numeros de 2 a 6 e imprimelos
# Ejemplo de ejecucion 2, 3, 4, 5, 6
print('Ejercicio 2: 2 3 4 5 6')
for i in range(2,7):
    print(i)

# Ejercicio 3: crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecucion: 3, 5, 7, 9
print('Ejercicio 3: 3, 5, 7, 9')
for i in range(3,10,2):
    print(i)
