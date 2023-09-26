#Operaciones de conjunto de listas

lista1 = ['zapallo','tomates','cebolla','queso']
lista2 = ['queso','batata','zapallo','atun']

#Cree las siguientes listas
#1 Lista con palabras que aparecen en las listas
lista3 = lista1+lista2
print(lista3)

#2 lista de palabras que aparecen en la primer lista pero no en la segunda
lista4=[palabra for palabra in lista1 if palabra not in lista2]
print(lista4)

#3 lista de palabras que aparecen en la segunda lista pero no en la primera
lista5 = [palabra for palabra in lista2 if palabra not in lista1]
print(lista5)

#3 lista de palabras que aparecen en ambas listas
lista6 = [palabra for palabra in lista2 if palabra in lista1]
print(lista6)

