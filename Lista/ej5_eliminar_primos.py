# 5. Dada una lista de números enteros eliminar de estas los números primos.
'''
Un número entero positivo p es un número primo si y solo si p > 1 y tiene exactamente dos divisores positivos distintos.
Esos dos divisores son, necesariamente, el 1 y el propio p.
'''

from TDA_list import List
from modulo_agregar_elementos_aleatorios import agregar_numeros

def eliminar_primos(lista: List):
    lista_aux = List()
    for numero in lista:
        es_primo = False
        if numero > 1:
            es_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    es_primo = False
                    break
        if es_primo == False:
            lista_aux.insert_value(numero)

    lista.clear()

    for numero in lista_aux:
        lista.insert_value(numero)

#################################################  Ejecución de pruebas del enunciado  #################################################
lista_enteros = List()
agregar_numeros(lista_enteros)
print(f'\nLista original: ')
lista_enteros.show()
eliminar_primos(lista_enteros)
print(f'\nLista sin números primos: ')
lista_enteros.show()