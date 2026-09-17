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

# # f. contar cuántos números pares e impares hay en el árbol.
# def contar_pares_impares(arbol: BinaryTree, pares: int = 0, impares: int = 0):
#     def __contar_pares_impares(root):
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

# --------- CREACIÓN DE FUNCIONES PARA FORMATO --------- #
class Color:
    RESET   = '\033[0m'
    NEGRITA = '\033[1m'
    CIAN    = '\033[96m'
    ROJO    = '\033[38;2;171;29;29m'     #AB1D1D
    AMARILLO= '\033[38;2;227;187;45m'    #E3BB2D
    AZUL    = '\033[38;2;0;48;176m'      #0030B0
    VERDE   = '\033[38;2;12;120;0m'      #0C7800
    VIOLETA = '\033[38;2;88;31;122m'     #581F7A

def print_seccion(titulo, ancho=140, relleno="-", color=Color.VERDE):
    print(f'\n{color}{f" {titulo} ".center(ancho, relleno)}{Color.RESET}')

#################################################  EJECUCIÓN DE PRUEBAS DEL ENUNCIADO  #################################################
print(f'\n{Color.CIAN}{f' EJERCICIO 1: NÚMEROS ENTEROS '.center(140, "=")}{Color.RESET}')

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
print_seccion('a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;')

print(f'{Color.AZUL}\nBarrido inorder (hijo izquierdo → raíz → hijo derecho): {Color.RESET}')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.in_order()

print(f'{Color.AZUL}\nBarrido postorder (hijo derecho → raíz → hijo izquierdo): {Color.RESET}')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.post_order()

print(f'{Color.AZUL}\nBarrido preorder (nodo raíz → hijo izquierdo → hijo derecho): {Color.RESET}')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.pre_order()

# b. determinar si un número está cargado en el árbol o no;
print_seccion('Búsqueda por valor del nodo: ')
# print(f'{Color.AZUL}\nÁrbol ordenado de menor a mayor: {Color.RESET}')
print(f'Árbol ordenado de menor a mayor: ')
arbol_numeros.in_order()
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
numero = int(input('  → Ingrese el número que desea buscar: '))

print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
buscado = arbol_numeros.search(numero)
if buscado is not None:
    print(
        f'  → El nodo se encuentra en la lista.'
        f'\n    - Valor del nodo: {buscado.value}'
        f'\n    - Valor a su izquierda: {buscado.left}'
        f'\n    - Valor a su derecha: {buscado.right}'
    )
else:
    print(f'  → El número {numero} no se encuentra en el árbol.')

# c. eliminar tres valores del árbol; → Aún no desarrollada la función eliminar

# # f. contar cuántos números pares e impares hay en el árbol.
# pares, impares = contar_pares_impares(arbol_numeros)
# print(f'Numeros pares: {pares}')
# print(f'Numeros impares: {impares}')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')