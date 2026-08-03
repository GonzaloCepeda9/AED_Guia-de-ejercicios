# Extra: Dada una pila de números aleatorios, separarlos en dos pilas nuevas, una con los pares y otra con los impares.

from TDA_stack import Stack
from random import randint

stack = Stack()

for i in range(5):
    number = randint(1, 100)
    stack.push(number)

stack_pares = Stack()
stack_impares = Stack()

while stack.size() > 0:
    number = stack.pop()
    if number % 2 == 0:
        stack_pares.push(number)
    else:
        stack_impares.push(number)

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n------------------------------------------- Separación de números pares e impares --------------------------------------------')
print(f'Pila original de números: ')
stack.show()
print(f'Pila de números pares: ')
stack_pares.show()
print(f'Pila de números impares: ')
stack_impares.show()