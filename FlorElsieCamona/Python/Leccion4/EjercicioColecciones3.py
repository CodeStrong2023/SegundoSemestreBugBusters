# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes
# personajes del senior de los anillos

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []  # Se crea una lista vacía
# Creamos diccionarios

P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del Norte'}
personajes.append(P)
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
print(personajes)
print("")
# Tarea: Agregar por lo menos otro tres personajes

P = {'Nombre': 'Galadriel', 'Clase': 'Princesa', 'Raza': 'Elfa Noldor'}
personajes.append(P)
P = {'Nombre': 'Saruman', 'Clase': 'Mago', 'Raza': 'Maia'}
personajes.append(P)
P = {'Nombre': 'Haldir', 'Clase': 'Guerrero', 'Raza': 'Elfo Silvan'}
personajes.append(P)


for personaje in personajes:
    print(personaje,  "")

