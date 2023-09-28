
# Colecciones parte 2

# Set o conjunto -> no tiene un orden y no permite almacenar elementos duplicados.
# Es inmutable, pero se puede agregar o eliminar. No mantiene un indice.

# Set -> coleccion sin orden y sin indice.

planetas = {"Marte", "Jupiter", "Saturno"}
print(planetas)

print(len(planetas))

# Revisar si un elemento existe dentro de set. Devuelve un booleano.
print("Jupiter" in planetas)
print("Venus" in planetas)
print("Marte" not in planetas)

# Añadir otro elemento
planetas.add("Tierra")
planetas.add("Tierra")
planetas.add("Tierra") # no añade elementos duplicados
print(planetas)

# Eliminar elementos
planetas.remove("Jupiter") # da error si no ingresamos el elemento correctamente
print(planetas)
planetas.discard("venus") # NO da error si ingresamos mal el elemento y lo elimina
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
# print(planetas) # nos muestra error porque "planetas" ya no existe, no está definido


# Diccionarios

# Key : value

# "Maradona" : 10

diccionario = {
    "IDE" : "Integrated Development Environment",
    "POO" : "Programacion Orientada a Objeto",
    "SQL" : "Structured Query Language"
}
print(diccionario)

print(len(diccionario))

# Acceder a un elemento a traves de la llave (porque no hay indice, como en los Sets)
print(diccionario["IDE"]) # Accedemos al valor de la llave

# Otra forma de acceder a un elemento
print(diccionario.get("POO"))
print(diccionario.get("SQL"))

# Modificar un elemento
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)
print(diccionario.get("IDE"))

# Recorrer los elementos
for key in diccionario: # De esta manera solo recorremos las llaves
    print(key)

for i in diccionario.keys(): # Otra forma de recorrer las llaves
    print(i)

for key, value in diccionario.items(): # De esta forma recorremos las llaves y su valor
    print(key, value)

for valor in diccionario.values(): # Recorre solo los valores, sin las llaves
    print(valor)

# Comprobar la existencia de algun elemento
print("IDE" in diccionario)
print("POO" not in diccionario)

# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("IDE")
print(diccionario)

# Limpiar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
