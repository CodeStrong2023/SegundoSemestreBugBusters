# Comenzamos con funciones
# mi_funcion() # No se puede llamar antes de definir una funcion
# Definimos una funcion
def mi_funcion(): # Para identificar a la funcion utilizamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

def show(name, lastName):
    print(name + ' ' + lastName)

person = ['Ariel', 'Betancur']
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto

persona2 = ('Osvaldo', 'Giordanini') # Desempaquetamos a través de una tupla
persona3 = {'lastName': 'Lucero', 'name': 'Natalia'}

numbers = {1, 2, 3, 4, 5, 6} # Aun con el la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3: # Esta es la unica manera para que no se ejecute el else
        break
else:
    print('Esto se termina')

# List comprehension, lista de comprension
names = ['Rodrigo', 'Santiago', 'Pepe', 'Morena']
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{'Name': 'Quilmes', 'Country': 'Arg'},
           {'Name': 'Corona', 'Country': 'Mx'},
           {'Name': 'Stella Artois', 'Country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['Country'] == 'Arg']
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludo a todos los que ven a traves del canal de Youtube")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78,22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print('Resultado de la suma: {resultado')
print(f'Resultado de la suma: {sumar2(22,66)}')

# Argumentos, variables en funciones
def listaNombres(*nombres): # Normalmente se utiliza *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listaNombres('Lucas', 'Santiago', 'Morena')
listaNombres('Marcos', 'Nicolas')











