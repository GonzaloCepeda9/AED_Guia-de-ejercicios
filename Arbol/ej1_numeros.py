# 1. Números
'''
Desarrollar un algoritmo que permita cargar 1000 número enteros (generados de manera aleatoria) que resuelva las siguientes actividades:
a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
b. determinar si un número está cargado en el árbol o no;
c. eliminar tres valores del árbol;
d. determinar la altura del subárbol izquierdo y del subárbol derecho;
e. determinar la cantidad de ocurrencias de un elemento en el árbol;
f. contar cuántos números pares e impares hay en el árbol.
'''

from TDA_arbol import BinaryTree
from random import randint

# --------- CARGA DE DATOS --------- #

arbol_numeros = BinaryTree()
for _ in range(10):
    arbol_numeros.insert(randint(1, 20))

# def contar_pares_impares(arbol):
#     def __contar_pares_impares(root, pares: int = 0, impares: int = 0):
#         if root is not None:
#             __contar_pares_impares(root.left)
#             print(root.value)
#             if root.value % 2 == 0:
#                 pares += 1
#             else:
#                 impares += 1
#             __contar_pares_impares(root.right)

#     if arbol.root is not None:
#         __contar_pares_impares(arbol.root)

#     return pares, impares

##########################################  EJECUCIÓN DE PRUEBAS DE ÁRBOL CON DATOS SIMPLES  ###########################################

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
print('\n------------------------------------------- Barridos inorder, postorder y preorden -------------------------------------------')
print('\nBarrido inorder (hijo izquierdo → raíz → hijo derecho): ')
arbol_numeros.in_order()
print('\nBarrido postorder (hijo derecho → raíz → hijo izquierdo): ')
arbol_numeros.post_order()
print('\nBarrido preorder (nodo raíz → hijo izquierdo → hijo derecho): ')
arbol_numeros.pre_order()

# b. determinar si un número está cargado en el árbol o no;
# numero = int(input('Ingrese el número a determinar si está cargado en el árbol o no: '))
# buscado = arbol_numeros.search(numero)
# if buscado is not None:
#     print(f'El número {numero} está cargado en el árbol.')
#     # print(
#     #     f'\nValor del nodo raíz: {buscado.value}'
#     #     f'\nValor del nodo izquierdo: {buscado.left.value}'
#     #     f'\nValor del nodo derecho: {buscado.right.value}'
#     # )
# else:
#     print(f'El número {numero} no está cargado en el árbol.')

# c. eliminar tres valores del árbol; → Aún no desarrollada la función eliminar

# f. contar cuántos números pares e impares hay en el árbol.
# pares, impares = contar_pares_impares(arbol_numeros)
# print(f'Numeros pares: {pares}')
# print(f'Numeros impares: {impares}')