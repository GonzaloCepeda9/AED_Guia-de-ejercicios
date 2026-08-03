# 2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.

from TDA_queue import Queue
from TDA_stack import Stack
from modulo_agregar_elementos_aleatorios import agregar_mayusculas

def invertir_cola(queue: Queue):

    stack_aux = Stack()

    for _ in range(queue.size()):
        element = queue.attention()
        stack_aux.push(element)

    while stack_aux.size() > 0:
        element = stack_aux.pop()
        queue.arrive(element)

    return queue

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
agregar_mayusculas(queue)
print(f'\nCola original: ')
queue.show()
print('\n-------------------------------------------- Inversión del contenido de una Cola ---------------------------------------------')
invertir_cola(queue)
print(f'Cola con su contenido invertido: ')
queue.show()