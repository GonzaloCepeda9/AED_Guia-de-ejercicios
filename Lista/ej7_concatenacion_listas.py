# 7. Concatenación de listas
'''
7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
'''

from TDA_list import List
from modulo_agregar_elementos_aleatorios import agregar_numeros

lista1 = List()
lista2 = List()

multiplos_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
for elemento in multiplos_2:
    lista1.insert_value(elemento)

multiplos_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27]
for elemento in multiplos_3:
    lista2.insert_value(elemento)

print(f'\nLista 1 original: ')
lista1.show()
print(f'\nLista 2 original: ')
lista2.show()

#################################################  Ejecución de pruebas del enunciado  #################################################
# a. concatenar dos listas, una atrás de la otra;
print('\n------------------------------------- a. Concatenación de dos listas, una detrás de otra -------------------------------------')
print(f'Listas 1 y 2 concatenadas: ')
lista1.show()
lista2.show()

# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
print('\n----------------------------------------- b. Concatenación de dos listas en una sola -----------------------------------------')
union_listas = List()
for elemento in lista1:
    union_listas.insert_value(elemento)
for elemento in lista2:
    repetido = False
    for elemento_en_lista in union_listas:
        if elemento == elemento_en_lista:
            repetido = True
    if repetido == False:
        union_listas.insert_value(elemento)
print(f'Listas 1 y 2 concatenadas (en una sola): ')
union_listas.show()

# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
print('\n------------------------------------- c. Conteo de elementos repetidos entre dos listas --------------------------------------')
contador = 0
for elemento1 in lista1:
    value = elemento1
    for elemento2 in lista2:
        if elemento1 == elemento2:
            contador += 1
print(f'Cantidad de elementos repetidos entre las listas: {contador}')

# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
print('\n-------------------------------------------- d. Eliminación de nodos de una lista --------------------------------------------')
while not lista1.is_empty():
    elemento = lista1.pop()
    print(f'El elemento {elemento} ha sido eliminado.')

print(f'\nLista 1 actualizada: ')
lista1.show()