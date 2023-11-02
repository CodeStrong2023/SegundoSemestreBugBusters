# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viseversa.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


temp_celsius = 20
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius} grados Celsius son {temp_fahrenheit} grados Fahrenheit")

temp_fahrenheit = 68
temp_celsius = fahrenheit_a_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit} grados Fahrenheit son {temp_celsius} grados Celsius")
