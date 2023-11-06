def listaTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir argumentos
    for llave, valor in terminos.items(: # kwargs significa: key word argument

        print(f'{llave} : {valor}')
listaTerminos() # Nada se muestra
listaTerminos(IDE ='Integrated Develoment Enviroment', PX= 'Primaruy Key')
listaTerminos(Nombre= 'Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
desplegarNombres(10) #No es un objeto iterable
desplegarNombres((10, 11)) #Convertimos en una tupla, es un elemento flexible, no olvidar la coma
desplegarNombres([22, 23]) # La convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo
numeroFactorial = int(input('Digite el numero para calcular el factorial: '))
resultado = factorial(numeroFactorial) # Lo hacemos en codigo duro
print(f'El factorial del numero {numeroFactorial} es: {resultado}')


