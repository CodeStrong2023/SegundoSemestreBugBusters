def contadorLetras(frase):
    fraseSinEspacios = frase.replace(' ','')
    print('La frase tiene ' + str(len(fraseSinEspacios)) + ' letras')

frase = str(input('Ingresar frase'))
contadorLetras(frase)