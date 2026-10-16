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

from TDA_tree import BinaryTree

# --------- CARGA DE DATOS --------- #
arbol_numeros = BinaryTree()

arbol_numeros.insert(19)
arbol_numeros.insert(7)
arbol_numeros.insert(31)
arbol_numeros.insert(11)
arbol_numeros.insert(22)
arbol_numeros.insert(27)
arbol_numeros.insert(45)

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
def contar_ocurrencias(arbol: BinaryTree, buscado: int):
    def __contar_ocurrencias(root, ocurrencias: int = 0):
        if root is not None:
            ocurrencias = __contar_ocurrencias(root.left, ocurrencias)
            if buscado == root.value:
                ocurrencias += 1
            ocurrencias = __contar_ocurrencias(root.right, ocurrencias)
        return ocurrencias

    if arbol.root is None:
        return 0

    return __contar_ocurrencias(arbol.root)

# f. contar cuántos números pares e impares hay en el árbol.
def contar_pares_impares(arbol: BinaryTree):
    def __contar_pares_impares(root, pares: int = 0, impares: int = 0):
        if root is not None:        
            pares, impares = __contar_pares_impares(root.left, pares, impares)

            if root.value % 2 == 0:
                pares += 1
            else:
                impares += 1

            pares, impares = __contar_pares_impares(root.right, pares, impares)

        return pares, impares

    if arbol.root is None:
        return 0, 0

    return __contar_pares_impares(arbol.root)

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

print(f'{Color.AZUL}Barrido "in order" (IZQ → RAÍZ → DER): {Color.RESET}')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.in_order()

print(f'{Color.AZUL}\nBarrido "post order" (DER → RAÍZ → IZQ): {Color.RESET}')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.post_order()

print(f'{Color.AZUL}\nBarrido "pre order" (RAÍZ → IZQ → DER): {Color.RESET}')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.pre_order()

print(f'{Color.AZUL}\nBarrido "by level" (NIVEL 1 → NIVEL 2 → ... → NIVEL n): {Color.RESET}')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.by_level()

# b. determinar si un número está cargado en el árbol o no;
print_seccion('b. determinar si un número está cargado en el árbol o no;')
# print(f'Árbol ordenado de menor a mayor: ')
# arbol_numeros.in_order()
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
numero = int(input('  → Ingrese el número que desea determinar si está cargado en el árbol: '))

print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
buscado = arbol_numeros.search(numero)
if buscado is not None:
    print(
        f'  → El nodo se encuentra en la lista.'
        f'\n    - Valor del nodo: {buscado.value}'
        f'\n    - Valor a su izquierda: {buscado.left.value if buscado.left else None}'
        f'\n    - Valor a su derecha: {buscado.right.value if buscado.right else None}'
    )
else:
    print(f'  → El número {numero} no se encuentra en el árbol.')

# c. eliminar tres valores del árbol;
print_seccion('c. eliminar tres valores del árbol;')
print(f'{Color.AZUL}Datos ingresados:{Color.RESET}')
nodo_a_eliminar = 45
print(f'  → Nodo a eliminar: {nodo_a_eliminar}')
nodo_eliminado, _ = arbol_numeros.delete(nodo_a_eliminar)
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if nodo_eliminado is not None:
    print(f'  → El nodo {nodo_eliminado} ha sido eliminado.')
else:
    print(f'  → El nodo {nodo_a_eliminar} no se encuentra en el árbol.')
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
nodo_a_eliminar = 7
print(f'  → Nodo a eliminar: {nodo_a_eliminar}')
nodo_eliminado, _ = arbol_numeros.delete(nodo_a_eliminar)
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if nodo_eliminado is not None:
    print(f'  → El nodo {nodo_eliminado} ha sido eliminado.')
else:
    print(f'  → El nodo {nodo_a_eliminar} no se encuentra en el árbol.')
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
nodo_a_eliminar = 27
print(f'  → Nodo a eliminar: {nodo_a_eliminar}')
nodo_eliminado, _ = arbol_numeros.delete(nodo_a_eliminar)
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if nodo_eliminado is not None:
    print(f'  → El nodo {nodo_eliminado} ha sido eliminado.')
else:
    print(f'  → El nodo {nodo_a_eliminar} no se encuentra en el árbol.')

# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
print_seccion('d. determinar la altura del subárbol izquierdo y del subárbol derecho;')
if arbol_numeros.root is not None and arbol_numeros.root.left is not None:
    altura_subarbol_izquierdo = arbol_numeros.height(arbol_numeros.root.left)
else:
    altura_subarbol_izquierdo = 0
if arbol_numeros.root is not None and arbol_numeros.root.right is not None:
    altura_subarbol_derecho = arbol_numeros.height(arbol_numeros.root.right)
else:
    altura_subarbol_derecho = 0
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → Altura del subárbol izquierdo: {altura_subarbol_izquierdo}')
print(f'  → Altura del subárbol derecho: {altura_subarbol_derecho}')

# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
print_seccion('e. determinar la cantidad de ocurrencias de un elemento en el árbol;')
print(f'{Color.AZUL}Datos ingresados:{Color.RESET}')
numero_buscado = int(input(f'  → Ingrese el número a determinar sus ocurrencias en el árbol: '))
ocurrencias = contar_ocurrencias(arbol_numeros, numero_buscado)
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if ocurrencias > 0:
    print(f'  → El número {numero_buscado} tiene {ocurrencias} ocurrencia/s en el árbol.')
else:
    print(f'  → El número {numero_buscado} no se encuentra en el árbol.')

# f. contar cuántos números pares e impares hay en el árbol.
print_seccion('f. contar cuántos números pares e impares hay en el árbol.')
pares, impares = contar_pares_impares(arbol_numeros)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → Numeros pares: {pares}')
print(f'  → Numeros impares: {impares}')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')