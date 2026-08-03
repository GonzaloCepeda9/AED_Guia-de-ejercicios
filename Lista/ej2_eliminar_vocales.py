# 2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

from TDA_list import List
from modulo_agregar_elementos_aleatorios import agregar_mayusculas

def eliminar_vocales(lista: List):
    lista_aux = List()
    for letter in lista:
        if letter not in vowels:
            lista_aux.insert_value(letter)

    lista.clear() # Si no podemos usar .clear(), hacer un ciclo While con .pop()

    for element in lista_aux:
        lista.insert_value(element)

#################################################  Ejecución de pruebas del enunciado  #################################################
vowels = ['A', 'E', 'I', 'O', 'U']
lista_letras = List()
agregar_mayusculas(lista_letras)
print(f'\nLista original de elementos: ')
lista_letras.show()
eliminar_vocales(lista_letras)
print(f'\nLista de elementos sin vocales: ')
lista_letras.show()