
# Desempaquetdo de listas o list Unpacking

def show(name, lastName):
    print(name + " " + lastName)

person = ["Nicolas", "Nuñez"]

show(person[0], person[1]) # pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anteriori pero lo pasamos todo junto


persona2 = ("Ariel", "Betancud")
show(persona2[0], persona2[1])
show(*persona2)

persona3 = {"lastName" : "Lucero", "name" : "Natalia"}
show(**persona3)

# Repaso For Else

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica forma de que no se ejecute el else
else:
    print("Esto se termina")

# List comprehension

names = ["Paola", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [ {"name" : "Quilmes", "country" : "Arg"},
            {"name" : "Corona", "country" : "Mx"},
            {"name" : "Stella Artois", "country" : "Belgium"}
           ]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(bottleC)
print(Arg)

# Paso de argumentos (funciones)

def mi_funcion(name, lastName): # parametros
    print("Saludos a todos")
    print(f"Nombre: {name}, Apellido: {lastName}")

mi_funcion("Lionel", "Messi") # argumentos
mi_funcion("Axl", "Rose")
mi_funcion("Paul", "McCartney")

# La palabra retunr en funciones

def sumar(num1, num2):
    return num1 + num2
    # suma = + num1 + num2
    # return suma

# resultado = sumar(21,18)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(78,22)}")

# Valores por default en parametros

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b

resultado = sumar2()
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar2(21,18)}")

# Argumentos, variables en funciones

def listar_nombres(*nombres): # Cuando desconocemos la cantidad de argumentos que va a recibir.
    # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)

listar_nombres("Nico", "Santi", "Vale", "Juli", "Maria")
listar_nombres("Marcos", "Flor", "Franco", "Belen")
