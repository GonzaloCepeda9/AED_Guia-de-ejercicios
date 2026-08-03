# 4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

from TDA_stack import Stack
from random import randint

def invertir_pila(stack: Stack):
    stack_aux = Stack()
    while stack.size() > 0:
        number = stack.pop()
        stack_aux.push(number)

    return stack_aux

stack = Stack()

for i in range(5):
    stack.push(randint(1, 9))


#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n------------------------------------------------- Pila con elementos al azar -------------------------------------------------')
stack.show()

stack = invertir_pila(stack)

print('\n----------------------------------------------- Pila con elementos invertidos ------------------------------------------------')
stack.show()