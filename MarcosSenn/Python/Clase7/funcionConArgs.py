#Crea una funcion para multiplicar valores recibidos de tipo numerico utilizando args

def sumarTodo(*args):
    sumaTotal = 0
    for numero in args:
        sumaTotal += numero
    print(sumaTotal)


sumarTodo(1,23,4,5,6)