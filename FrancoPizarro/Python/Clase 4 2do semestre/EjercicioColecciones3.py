'''
Ejercicio 3: Agregar personajes a una lista
Escriba un programa donde cree una lista con los siguientes personajes del
señor de los anillos
- Nombre: Aragon -Clase: Guerrero -Raza: Dúnadan del norte
- Nombre: Gandalf -Clase: Mago -Raza: Istar
- Nombre: Legolas - Clase: Arquero - Raza: Elfo Sindar
'''
personajes = [] # Creamos una lista vacia
# Creamos diccionarios
P1 = {'NOMBRE': 'Aragon', 'CLASE': 'Guerrero', 'RAZA': 'Dúnadan del Norte'}
personajes.append(P1)
P2 = {'NOMBRE': 'Gandalf', 'CLASE': 'Mago', 'RAZA': 'Istar'}
personajes.append(P2)
P3 = {'NOMBRE': 'Legolas', 'CLASE': 'Arquero', 'RAZA': 'Elfo Sindar'}
personajes.append(P3)
P4 = {'NOMBRE': 'Frodo Bolsón', 'CLASE': 'Espadachín', 'RAZA': 'Hobbit'}
personajes.append(P4)
P5 = {'NOMBRE': 'Radagast', 'CLASE': 'Mago', 'RAZA': 'Istari'}
personajes.append(P5)
P6 = {'NOMBRE': 'Samsagaz Gamyi', 'CLASE': 'Espadachín', 'RAZA': 'Hobbit'}
personajes.append(P6)
print(personajes)