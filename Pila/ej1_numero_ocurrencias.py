# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.

from TDA_stack import Stack
from random import randint

stack = Stack()

for i in range(10):
    number = randint(1, 9)
    stack.push(number)


#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n------------------------------------------------- Pila con elementos al azar -------------------------------------------------')
stack.show()

elemento_buscado = int(input(f'\nIngrese el elemento que desea determinar sus ocurrencias en la pila: '))
ocurrencias = 0

while stack.size() > 0:
    elemento = stack.pop()
    print(f'Comparando elemento {elemento} con {elemento_buscado}') # Solo para debug
    if elemento == elemento_buscado:
        ocurrencias += 1

print(f'\nEl número {elemento_buscado} tiene {ocurrencias} ocurrencias en la pila.')