# Comenzamos con Funciones

# Definimos una funcion
#mi_funcion() # No se puede llamar antes de definir a una funcion
def mi_funcion(): # Para identificar a la funcion utilizamos parentesis
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ['Franco','Pizarro']
show(person[0], person[1]) # pasamos uno por uno los datos de la lista a la funcion
show(*person)# Esto es lo mismo que la anterior pero la pasamos todo junto
persona2 = ('Juan Cruz', 'Cogo') # Desempaquetamos a traves de una tupla
show(*persona2)
persona3 = {"lastName": "Guzman", "name": "Sebastian"}
show(**persona3)

numbers = [1, 2, 3 ,4 ,5]
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se termino')

# List comprehension, lista de comprension
names = ["Paolo","Rodrigo","Lupe","Pepe"]
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongP)

bottleC = [{'name':'Quilmes', 'Country':'Argentina'},
           {'name':'Corona', 'Country': 'Mexico'},
           {'name':'Stella Artois', 'Country':'Belgium'},
           ]
Argentina = [b for b in bottleC if b['Country'] == 'Argentina']
print(Argentina)
print(bottleC)

# Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print('Saludos a todos los que ven a través del canal de youtube')
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Bentacud')
mi_funcion2('Analia','Pedrosa')

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a + b
resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0): #le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones
def listaNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listaNombres('Lucas', 'Jose', 'Claudia','Rosa', 'Maria')
listaNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos): # lo mas utilizado es **kwargs para recibir los argumentos
    for llave,  valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos() # no se recibe nada, nada se va a mostrar
listarTerminos(IDE = 'Integrated Development Enviroment', PK = 'Primary Key')
listarTerminos(Nombre='Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito','Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10) # No es un objeto iterable
desplegarNombres((10, 11)) # la convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # la convertimos en una lista

# FUNCIONES RECURSIVAS
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo

resultado = factorial(5) # lo hacemos en codigo duro
print(f'El factorial del número 5 es: {resultado}')
 # Tarea: que el usuario ingrese el número para calcular el factorial
numFactorial = int(input("Digite un número para sacar el factorial: "))
resultado = factorial(numFactorial) # Lo hacemos en código duro
print(f'El factorial del número: {numFactorial} es: {resultado}')
