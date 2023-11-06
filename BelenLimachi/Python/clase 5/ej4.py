# Ejercicio 4= Sumar números pares dentro de un rango 
# hacer un programa para súmar números pares dentro 
# de un rango, por ejemplo:
# Suma de números pares de 2 al 30
# Suma = 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a,b + 1):
    if i % 2 == 0: # Esto es si es un numero par
        suma += i
print(f'\nLa suma de numeros pares dentro del rango es: {suma}')