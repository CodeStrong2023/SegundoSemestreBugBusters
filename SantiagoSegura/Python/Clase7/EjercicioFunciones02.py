# Ejercicio 2: Funcion con * args para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numerico, utilizando argumentos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumentos


# Definimos la funcion para multiplicar

def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

resultado = multiplicar(2, 3, 4)
print(resultado)  # Esto imprimirá 24, que es el resultado de 2 * 3 * 4
