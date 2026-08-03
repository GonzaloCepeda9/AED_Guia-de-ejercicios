# 8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando solo una cola como estructura auxiliar.

from prueba_queue import Queue
from typing import Any

def ordenar_cola(queue: Queue, elemento: Any):
    queue_aux = Queue()
    agregado: bool = False

    if queue.is_empty() == True:
        queue.arrive(elemento)
        agregado = True
    else:
        while queue.size() > 0:
            elemento_frente = queue.on_front()
            if elemento < elemento_frente:
                queue_aux.arrive(elemento)
                agregado = True
                queue_aux.arrive(elemento_frente)
                queue.attention()
                
                while queue.size() > 0:
                    elemento_frente = queue.on_front()
                    queue_aux.arrive(elemento_frente)
                    queue.attention()
            else:
                while queue.size() > 0:
                    if elemento_frente < elemento:
                        queue_aux.arrive(elemento_frente)
                        queue.attention()
                    else:
                        queue_aux.arrive(elemento)
                        agregado = True
                        while queue.size() > 0:
                            elemento_frente = queue.on_front()
                            queue_aux.arrive(elemento_frente)
                            queue.attention()

                    elemento_frente = queue.on_front()
    
        if agregado == False:
            queue_aux.arrive(elemento)

        while queue_aux.size() > 0:
            value = queue_aux.attention()
            queue.arrive(value)
    
    return queue


queue = Queue()
elemento1 = (9)
elemento2 = (3)
elemento3 = (6)
elemento4 = (1)
elemento5 = (12)


ordenar_cola(queue, elemento1)
print('Cola actualizada: ')
queue.show()
ordenar_cola(queue, elemento2)
print('Cola actualizada: ')
queue.show()
ordenar_cola(queue, elemento3)
print('Cola actualizada: ')
queue.show()
ordenar_cola(queue, elemento4)
print('Cola actualizada: ')
queue.show()
ordenar_cola(queue, elemento5)
print('Cola actualizada: ')
queue.show()




# Nuevo elemento:
#12

# Oringal  /  Auxiliar
#          #1
#          #3
#          #6 
#          #9 
#          # 
#          # 
