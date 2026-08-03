# 8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando solo una cola como estructura auxiliar.

from TDA_queue import Queue
from typing import Any

def agregar_ordenado(queue: Queue, elemento: Any):
    queue_aux = Queue()
    
    while not queue.is_empty() and queue.on_front() <= elemento:
        queue_aux.arrive(queue.attention())
    
    queue_aux.arrive(elemento)

    while not queue.is_empty():
        queue_aux.arrive(queue.attention())

    while not queue_aux.is_empty():
        queue.arrive(queue_aux.attention())

    return queue

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
print('\n---------------------------------------------- Agregación ordenada de elementos ----------------------------------------------')
elemento = input('Ingrese un elemento para agregar en la Cola o presione "Enter" para finalizar: ')
while elemento != '':
    if elemento.isdigit():
        elemento = int(elemento)
    agregar_ordenado(queue, elemento)
    queue.show()
    elemento = input('Ingrese el elemento del mismo tipo para agregar a la Cola, o presione "Enter" para finalizar: ')
print(f'\nEjecución finalizada.')