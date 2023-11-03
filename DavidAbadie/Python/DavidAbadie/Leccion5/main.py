# Comenzamos con funciones

# definimos una funcion
def mi_funcion():
    print('Hola como estás?')

mi_funcion()  # Estamos llamando a la funcion
mi_funcion()  # Se pede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["David", "Abadie"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la funcion
show(*person)  # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini")  # desempaquetamos a través de una tupla
show(*person2)
person3 = {"name": "Natalia", "lastName": "Lucero"}
show(**person3)  # Muestra clave y valor

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == len(numbers):
        break  # Se muestra toda la lista y se salta el else
        # Sin el break se ejecuta el else
else:
    print("Esto se terminó")

# list comprehesion, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P']  # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'78 + 22 = {resultado}')
print(f'55 + 45 = {sumar(55, 45)}')

def sumar2(a = 0, b = 0):  # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones
def listarNombres(*nombres):    #  * Cuando no conocemos la cantidad de argumentos a recibir
                                #  normalmente se utiliza: *args
    for nombre in nombres:  # Se convierte en una tupla
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe')

def listarTerminos(**terminos): # **keyword es mas utilizado para recibir los argumentos (llave valor)
    for llave, valor in terminos.items(): # kwargs = key word argument
        print(f'{llave} : {valor}')

listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primary Key')
listarTerminos(Nombre='Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10) # No es un objeto iterable
# Conversion de elementos para pasar a la función:
desplegarNombres((10, 11)) # Es una tupla iterable # En un solo elementos no olvidar la coma ,
desplegarNombres([22, 55]) # Lista iterable

# FUNCIONES RECURSIVAS
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero - 1) # Caso recursivo


numero = int(input("Ingrese un numero para conocer su factorial: "))

print(f"El factorial de {numero} es {factorial(numero)}")
