# 9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay
'''
◘ Algoritmo para resolver el problema:
Calcular su rango
    Obtener el valor mínimo y máximo de la Cola, creando un ciclo y comparando cada elemento.
    Aplicar fórmula para el rango (Rango = Valor máximo - Valor mínimo).

Contar elementos negativos
    Crear un contador para los negativos.
    Realizar un ciclo que vaya aumentando en 1 cada vez que la condición de negatividad se cumpla. 
'''

from TDA_queue import Queue
from modulo_agregar_elementos_aleatorios import agregar_numeros

def calcular_rango(queue: Queue):
    
    rango: int
    valor_minimo = queue.on_front()
    valor_maximo = queue.on_front()
    
    for _ in range(queue.size()):
        
        valor_frente = queue.on_front()

        if valor_frente < valor_minimo:
            valor_minimo = valor_frente
        
        if valor_frente > valor_maximo:
            valor_maximo = valor_frente

        queue.move_to_end()

    rango = valor_maximo - valor_minimo

    return valor_maximo, valor_minimo, rango

def contar_negativos(queue: Queue):
    
    negativos: int = 0

    for _ in range(queue.size()):
        elemento_frente = queue.move_to_end()
        if elemento_frente < 0:
            negativos += 1

    return negativos

#################################################  Ejecución de pruebas del enunciado  #################################################
queue = Queue()
agregar_numeros(queue)
print(f'\nCola de elementos: ')
queue.show()
print('\n------------------------------------------ Cálculo del rango de la cola de valores -------------------------------------------')
min, max, rango = calcular_rango(queue)
print(f'Valor mínimo de la Cola: {min}. \nValor máximo de la Cola: {max}. \nEl rango de la Cola de valores es {rango}.')

print('\n----------------------------------------------- Conteo de elementos negativos ------------------------------------------------')
cantidad_negativos = contar_negativos(queue)
print(f'En la cola hay {cantidad_negativos} elementos negativos.')