# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza:  Elfo Sindar

personajes = []  # Creamos una lista vacía
# Creamos diccionarios
p = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del norte'}
personajes.append(p)  # Agregamos a la lista un personaje
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(p)
p = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(p)
p = {'Nombre': 'Gollum', 'Clase': 'Fuertes', 'Raza': 'Hobbit'}
personajes.append(p)
p = {'Nombre': 'Galadriel', 'Clase': 'Elfa', 'Raza': 'Noldor'}
personajes.append(p)
p = {'Nombre': 'Sauron', 'Clase': 'Señor Oscuro', 'Raza': 'Ainur y Maiar'}
personajes.append(p)
print(personajes)

