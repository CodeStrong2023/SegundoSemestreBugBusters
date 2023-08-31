# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluyta los números menores a 5
# e imprima por consola [1, 3, 2]
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)