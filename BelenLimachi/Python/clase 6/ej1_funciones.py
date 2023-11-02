# Ejercicio 01= Crear una función para sumar los valores recibidos de tipo 
# numéricos, utilizando argumentos variables *args como parametro de la 
# Función y agregar como resultado la suma de todos los valores pasados
# como argumentos.

def sumar_valor(*args): # Recibimos una cantidad de parámetros indefinidos
    # pass # Cuando no queremos agregar detalles de la función usamos la palabra reservada pass
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

# Llamos a la función 
print(sumar_valor(3, 5, 9, 2, 1))