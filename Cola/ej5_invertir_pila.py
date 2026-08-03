# 5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.

from TDA_queue import Queue
from TDA_stack import Stack
from modulo_agregar_elementos_aleatorios import agregar_numeros

def invertir_pila(stack: Stack):
    queue = Queue()
    while stack.size() > 0:
        queue.arrive(stack.pop())
    while queue.size() > 0:
        stack.push(queue.attention())
    return stack

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
stack = Stack()
agregar_numeros(stack)
print(f'\nPila original: ')
stack.show()
print('\n-------------------------------------------- Inversión del contenido de una Pila ---------------------------------------------')
invertir_pila(stack)
print(f'Pila invertida: ')
stack.show()
