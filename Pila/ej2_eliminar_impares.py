# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.

from TDA_stack import Stack
from random import randint

def eliminar_impares(stack):
    stack_aux = Stack()
    while stack.size() > 0:
        number = stack.pop()
        if number % 2 == 0:
            stack_aux.push(number)

    while stack_aux.size() > 0:
        number = stack_aux.pop()
        stack.push(number)

    return stack

stack = Stack()

for i in range(5):
    number = randint(1, 50)
    stack.push(number)

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n------------------------------------------------- Pila con elementos al azar -------------------------------------------------')
stack.show()

eliminar_impares(stack)

print('\n---------------------------------------------- Pila original con elementos pares ---------------------------------------------')
stack.show()