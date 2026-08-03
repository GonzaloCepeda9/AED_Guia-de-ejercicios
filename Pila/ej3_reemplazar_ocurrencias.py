# 3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from TDA_stack import Stack
from random import randint

def reemplazar_ocurrencias(stack, num_a_reemplazar, num_nuevo):
    stack_aux = Stack()
    while stack.size() > 0:
        number = stack.pop()
        if number == num_a_reemplazar:
            stack_aux.push(num_nuevo)
        else:
            stack_aux.push(number)

    while stack_aux.size() > 0:
        number = stack_aux.pop()
        stack.push(number)

    return stack

stack = Stack()

for i in range(9):
    number = randint(1, 9)
    stack.push(number)

print('\n------------------------------------------------- Pila con elementos al azar -------------------------------------------------')
stack.show()

num_a_reemplazar = int(input('\nIngrese el número que desea reemplazar en caso de que se encuentre en la pila: '))
num_nuevo = int(input('\nIngrese el número por el cuál desea reemplazarlo: '))


reemplazar_ocurrencias(stack, num_a_reemplazar, num_nuevo)

print('\n------------------------------------------ Pila original con elementos reemplazados ------------------------------------------')
stack.show()