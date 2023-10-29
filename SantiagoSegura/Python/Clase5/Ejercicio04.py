# Ejercicio 4: Sumar numereos pares dentro de un rango
# Hacer un programa para sumar numeros pares dentro
# Suma de numeros pares del 2 al 30
# suma = 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0: # Esto es si el numero es par
        suma += 1
print(f"\nLa Suma de numeros pares dentro del rango es: {suma}")



