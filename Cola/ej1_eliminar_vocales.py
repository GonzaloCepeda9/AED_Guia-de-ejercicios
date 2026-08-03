# 1. Eliminar de una cola de caracteres todas las vocales que aparecen

from TDA_queue import Queue
from modulo_agregar_elementos_aleatorios import agregar_mayusculas

def eliminar_vocales(queue: Queue):
    for _ in range(queue.size()):
        letter = queue.on_front()
        if letter in vowels:
            queue.attention()
        else:
            queue.move_to_end()
    return queue

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
vowels = ['A', 'E', 'I', 'O', 'U']
agregar_mayusculas(queue)
print(f'\nCola original de elementos: ')
queue.show()
print('\n--------------------------------------------------- Eliminación de vocales ---------------------------------------------------')
eliminar_vocales(queue)
print(f'Cola de elementos sin vocales: ')
queue.show()