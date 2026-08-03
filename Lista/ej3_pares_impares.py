# 3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos, una que contenga los números pares y otra para los números impares.

from TDA_list import List
from modulo_agregar_elementos_aleatorios import agregar_numeros

def separar_pares_impares(lista: List):
    lista_pares = List()
    lista_impares = List()
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.insert_value(numero)
        else:
            lista_impares.insert_value(numero)

    return lista_pares, lista_impares

#################################################  Ejecución de pruebas del enunciado  #################################################
lista_enteros = List()
agregar_numeros(lista_enteros)
print(f'\nLista original: ')
lista_enteros.show()
lista_pares, lista_impares = separar_pares_impares(lista_enteros)
print(f'\nLista con números pares: ')
lista_pares.show()
print(f'\nLista con números impares: ')
lista_impares.show()