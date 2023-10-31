# Desempaquetado de listas o list Unpacking
def show(name, lastname):
    print(name + '' + lastname)
person = ["Gabriel", " Gonzalez"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función
show(*person)
person2 = ("Ariel", " Betancud") # Desempaquetamos atravez de una Tupla
show(*person2)
person3 = {"name" : "Natalia" , "lastname" : " Lucero"}
show(**person3)

# List comprehension, lista comprensión
names = ["Paola", "Rodrigo", "Lupe", "Pepe"]
alongp = [p for p in names if p [0] == "P"] # Esto regresa una nueva lista
print(alongp)

bottleC = [{"name" : "Quilmes", "country" : "Arg"},
           {"name" : "Corona" , "country" : "Mx"},
           {"name" : "Stella Artois" , "country" : "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

Mx = [c for c in bottleC if c["country"] == "Mx"]
print(Mx)

# Paso de argumentos (funciones)
def mi_Funcion2(name, lastname):
    print("Saludo a tutores")
    print(f'Nombre: {name} Apellido: {lastname}')
mi_Funcion2('Osman', 'Herrera')
mi_Funcion2('Tamara', 'Piccini')
mi_Funcion2('Francisco', 'Rodeles')

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a,b):
    return a + b
# resultado = sumar(78 , 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(30, 25)}')

#repaso para else
numbers = [1, 2, 3, 4, 5] # Aun con el la lista vacia se va ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")


