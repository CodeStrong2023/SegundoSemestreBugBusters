def imprimirDescendente(num):
    if(num == 1): print(1)
    else:
        print(num)
        imprimirDescendente(num-1)




imprimirDescendente(10)