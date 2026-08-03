# 6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.

from TDA_queue import Queue
from modulo_agregar_elementos_aleatorios import agregar_numeros

def contar_ocurrencias(queue: Queue, buscado):
    contador: int = 0
    for _ in range(queue.size()):
        numero_frente = queue.move_to_end()
        if numero_frente == buscado:
            contador += 1
    return contador

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
agregar_numeros(queue)
print(f'\nCola de elementos: ')
queue.show()
buscado = int(input(f'\nIngrese el número que desea contar sus ocurrencias en la cola: '))
print('\n---------------------------------------------- Conteo de cantidad de ocurencias ----------------------------------------------')
ocurrencias = contar_ocurrencias(queue, buscado)
if ocurrencias > 0:
    print(f'El elemento "{buscado}" tiene {ocurrencias} ocurrencia/s en la cola.')
else:
    print(f'El elemento "{buscado}" no se encuentra en la cola.')