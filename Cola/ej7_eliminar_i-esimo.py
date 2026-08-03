# 7. Eliminar el i-ésimo elemento después del frente de la cola.

from TDA_queue import Queue
from modulo_agregar_elementos_aleatorios import agregar_numeros

def eliminar_elemento(queue: Queue, posicion: int):

    for i in range(queue.size()):

        if i == posicion:
            queue.attention()
        else:
            queue.move_to_end()

    return queue

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
agregar_numeros(queue)
print(f'\nCola de elementos: ')
queue.show()
posicion = int(input('\nIngrese la posición del elemento después del frente que desea eliminar: '))
print('\n------------------------------- Eliminación del i-ésimo elemento después del frente de la cola -------------------------------')
if posicion < 0 or posicion > queue.size():
    print(f'La posición ingresada no corresponde a ningún elemento en la Cola.')
elif posicion == 0:
    print(f'Debe ingresar una posición diferente a la del elemento en el frente de la Cola.')
else:
    queue = eliminar_elemento(queue, posicion)
    print(f'Cola de elementos actualizada: ')
    queue.show()