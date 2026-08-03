# 4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

from TDA_queue import Queue
from modulo_agregar_elementos_aleatorios import agregar_numeros

def eliminar_primos(queue: Queue):
    for i in range(queue.size()):
        numero_frente = queue.on_front()
        if numero_frente <= 0:
            queue.attention()
        elif numero_frente == 1 or numero_frente == 2:
            queue.move_to_end()
        else:
            primo: bool = True
            for j in range(2, numero_frente):
                if numero_frente % j == 0:
                    primo = False
                    break   # Si no usamos break, sigue comparando y haciendo operaciones sin sentido.
            if primo == True:
                queue.move_to_end()
            else:
                queue.attention()
    return queue

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
agregar_numeros(queue)
print(f'\nCola original: ')
queue.show()
print(f'\n---------------------------------------------- Eliminación de números no primos ----------------------------------------------')
eliminar_primos(queue)
print(f'Cola de números primos: ')
queue.show()