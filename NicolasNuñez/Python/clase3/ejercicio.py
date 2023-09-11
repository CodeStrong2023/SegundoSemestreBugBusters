
seleccion_argentina = {
    10 : {
        "Nombre" : "Lionel Messi",
        "Edad" : 35,
        "Altura" : 1.70,
        "Precio" : "50 Millones",
        "Posicion" : "Extremo Derecho"
    },
    11 : {
        "Nombre" : "Angel Di Maria",
        "Edad" : 34,
        "Altura" : 1.80,
        "Precio" : "12 Millones",
        "Posicion" : "Extremo Derecho"
    },
    24 : {
        "Nombre" : "Paulo Dybala",
        "Edad" : 28,
        "Altura" : 1.77,
        "Precio" : "35 Millones",
        "Posicion" : "Media Punta"
    },
    19 : {
        "Nombre" : "Nicolas Otamendi",
        "Edad" : 34,
        "Altura" : 1.83,
        "Precio" : "3.5 Millones",
        "Posicion" : "Defensa Central"
    },
    1 : {
        "Nombre" : "Franco Armani",
        "Edad" : 35,
        "Altura" : 1.89,
        "Precio" : "3.5 Millones",
        "Posicion" : "Portero"
    },
    23 : {
        "Nombre" : "Emiliano Martinez",
        "Edad" : 31,
        "Altura" : 1.95,
        "Precio" : "28 Millones",
        "Posicion" : "Portero"
    },
    7 : {
        "Nombre" : "Rodrigo De Paul",
        "Edad" : 29,
        "Altura" : 1.80,
        "Precio" : "37 Millones",
        "Posicion" : "Centrocampista"
    },
    4 : {
        "Nombre" : "Gonzalo Montiel",
        "Edad" : 26,
        "Altura" : 1.75,
        "Precio" : "11 Millones",
        "Posicion" : "Defensor"
    },
    27 : {
        "Nombre" : "Julian Alvarez",
        "Edad" : 23,
        "Altura" : 1.70,
        "Precio" : "10 Millones",
        "Posicion" : "Delantero"
    }
}

for llave,valor in seleccion_argentina.items():
    print(llave, valor)

jugadores = len(seleccion_argentina)

print(f"Tenemos cargado en el diccionario de la selección a {jugadores} jugadores")

