lista = [1,2,3,4,5,6,7,8,9,10]
nuevaLista= []
def multiplicarList(num):
    for numero in lista:
        nuevaLista.append(numero * num)

    print(nuevaLista)

multiplicarList(10)
