#Ejercicio 2: Calcular el factorial de un numero

num= int(input('De que numero queres calcular el factorial? '))
def encontrarFactorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * encontrarFactorial(num-1)

print(encontrarFactorial(num))