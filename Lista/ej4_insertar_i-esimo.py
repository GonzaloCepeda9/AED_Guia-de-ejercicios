# 4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

from TDA_list import List
from modulo_agregar_elementos_aleatorios import agregar_numeros
from typing import Any

def insertar_iesimo(lista: List, elemento: Any, posicion: int):
    lista.insert(posicion, elemento)
    
#################################################  Ejecución de pruebas del enunciado  #################################################
lista_elementos = List()
agregar_numeros(lista_elementos)
print(f'\nLista original: ')
lista_elementos.show()
elemento = input(f'\nIngrese el elemento a insertar: ')
posicion = int(input(f'\nIngrese la posición en la cual quiere insertarlo: '))
insertar_iesimo(lista_elementos, elemento, posicion)
print(f'\nLista actualizada: ')
lista_elementos.show()