
'''
Ejercicio 3: Agregar personajes a una lista

Escriba un programa donde cree una lista con los siguiente personajes
del señor de los anillos

Nombre: Aragon
Clase: Guerrero
Raza: Dunadan del norte

Nombre: Gandalf
Clase: Mago
Raza: Istar

Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
'''

# creamos una lista vacia
lista_personajes = []

# usamos diccionarios para tener la llave y el valor

pers1 = {
    "Nombre" : "Aragon",
    "Clase" : "Guerrero",
    "Raza" : "Dunadan del norte"
}

pers2 = {
    "Nombre" : "Gandalf",
    "Clase" : "Mago",
    "Raza" : "Istar"
}

pers3 = {
    "Nombre" : "Legolas",
    "Clase" : "Arquero",
    "Raza" : "Elfo Sindar"
}

# agregamos los personajes a la lista
lista_personajes.append(pers1)
lista_personajes.append(pers2)
lista_personajes.append(pers3)

pers4 = {
    "Nombre" : "Sauron",
    "Clase" : "Herrero",
    "Raza" : "Maiar"
}

pers5 = {
    "Nombre" : "Gollum",
    "Clase" : "Hobbit",
    "Raza" : "Hobbit corrompido"
}

pers6 = {
    "Nombre" : "Galadriel",
    "Clase" : "Elfa",
    "Raza" : "Elfos Noldor"
}

lista_personajes.append(pers4)
lista_personajes.append(pers5)
lista_personajes.append(pers6)
print(lista_personajes)

