# Ejercicio 6= Tabla de múltiplicar 
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. por ejemplo:
# si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

numero = int(input("Digite un número: "))
lista = []
for i in range(1,11):
    lista.append(i * numero)

print(f'\nTabla de multiplical del {numero} es: \n {lista}')

for indice, i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}')