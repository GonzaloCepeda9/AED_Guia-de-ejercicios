# 1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

from TDA_list import List
from modulo_agregar_elementos_aleatorios import agregar_numeros

#################################################  Ejecución de pruebas del enunciado  #################################################
new_list = List()
agregar_numeros(new_list)

print(f'\nLista original: ')
new_list.show()
cantidad_nodos = new_list.size()
print(f'\nLa lista contiene {cantidad_nodos} nodos.')