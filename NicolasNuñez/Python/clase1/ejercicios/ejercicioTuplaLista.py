'''
Dada la siguiente tupla, crear una lista que solo incluta los números menor a 5
e imprima por consola [1,3,2]
'''

tupla = (13, 1, 8, 3, 2, 5, 8)
print("Tupla: ")
print(tupla)

lista = []

for i in tupla:
    if(i < 5):
        lista.append(i)

print("Lista: ")
print(lista)