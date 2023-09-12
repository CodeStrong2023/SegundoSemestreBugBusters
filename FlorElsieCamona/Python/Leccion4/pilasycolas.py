# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
pila.pop()
print(pila)

# Quitamos otro elemento y lo guardamos en una variable
elementoBorrado = pila.pop()
print(pila)
print('Sacamos el elemento: ', elementoBorrado)

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output# )
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']
cola.append('Natalia')
cola.append('Juan')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0) # Se elimina el primer elemento
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)