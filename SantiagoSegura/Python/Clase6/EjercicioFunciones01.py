# Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
# numericos, utilizando argumentos variables *args como parametro de la
# Funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos
# Definimos una funcion
def sumar_valor(*args): # Recibimos una cantidad de parametros indefinidos
    resultado = 0
    # Iteramoscada elemento
    for valor in args:
        resultado += valor
    return resultado


#Llamamos a la funcion
print(sumar_valor(3,5,9, 2, 5,4))