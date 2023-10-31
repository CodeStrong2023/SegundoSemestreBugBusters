# Ejercicio 3= Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celcius a fahrenheit y viseversa.
# Investigar las formulas

def celcius_a_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

# Ejecutamos las dos funciones
celcius = float(input("Digite el valor de grados celcius: "))
fahrenheit = celcius_a_fahrenheit(celcius)
print(f'El resultado de {celcius} de grados celcius a fahrenheit es: {fahrenheit}')
fahrenheit = float(input("Digite el valor de grados fahrenheit: "))
celcius = fahrenheit_a_celcius(fahrenheit)
print(f'El resultado de {fahrenheit} de grados fahrenheit a celcius es: {celcius}')