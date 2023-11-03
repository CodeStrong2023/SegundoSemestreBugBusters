# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro de un rango,
# Por ejemplo:
# Suma de numeros pares del 2 al 30
# suma = 240

a = int(input("Ingrese de donde va comenzar la suma: "))
b = int(input("Ingrese hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a, b+1):
    if i % 2 == 0:  # Esto es si es par
        suma += i
print(f"\nLa suma de numeros pares dentro del rango es: {suma}")
