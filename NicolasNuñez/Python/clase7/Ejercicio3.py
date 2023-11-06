
'''
Ejercicio 3: Convertidor de temperaturas
Realizar dos funciones para convertir de grado celsius a fahrenheit y viseversa.
Investigar las formulas

celsius a fahrenheit = (grados celsius * 1,8) + 32
fahrenheit a celsius = (fahrenheit - 32) / 1,8
'''

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return  celsius

grados_celsius = 34
fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(f"Grados centígrados (celsius): \"{grados_celsius}°\" a grados Fahrenheit da: {fahrenheit}°")

grados_fahrenheit = 99.6
celsius = fahrenheit_a_celsius(grados_fahrenheit)
print(f"Grados Fahrenheit: \"{grados_fahrenheit}°\" a grados centígrados (celsius) da: {celsius :.1f}°")