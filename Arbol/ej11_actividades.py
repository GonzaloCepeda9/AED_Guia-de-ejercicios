# 11. Variado
'''
Escribir un algoritmo que permita resolver las siguientes actividades:
a. contar el número de nodos del árbol;
b. determinar el número de hojas del árbol;
c. mostrar la información de los nodos hojas;
d. determinar el padre de un nodo;
e. determinar la altura de un árbol.
'''

from TDA_tree import BinaryTree
from typing import Any

class BinaryTreeAct (BinaryTree):

    # a. contar el número de nodos del árbol;

    def contar_nodos(self):

        if self.root is None:
            return None

        def __contar_nodos(root, nodos):

            if root is None:
                return nodos

            nodos = __contar_nodos(root.left, nodos)

            if root.value is not None:
                nodos = nodos + 1

            nodos = __contar_nodos(root.right, nodos)

            return nodos

        nodos = 0
        return __contar_nodos(self.root, nodos)

    # b. determinar el número de hojas del árbol;

    def determinar_hojas(self):

        if self.root is None:
            return None

        def __determinar_hojas(root, hojas):

            if root is None:
                return hojas

            hojas = __determinar_hojas(root.left, hojas)

            if root.left is None and root.right is None:
                hojas = hojas + 1

            hojas = __determinar_hojas(root.right, hojas)

            return hojas

        hojas = 0
        return __determinar_hojas(self.root, hojas)

    # c. mostrar la información de los nodos hojas;

    def mostrar_info_hojas(self):

        if self.root is None:
            print(f'  → El árbol está vacío.')  # Como no se retorna nada porque es un barrido, hacemos un print() para mostrar un mensaje al usuario.

        def __mostrar_info_hojas(root):

            if root is not None:

                __mostrar_info_hojas(root.left)

                if root.left is None and root.right is None:
                    print(f'  → El nodo {root.value} es hoja. | Información: {root.other_values}')

                __mostrar_info_hojas(root.right)

        if self.root is not None:
            __mostrar_info_hojas(self.root)

    # d. determinar el padre de un nodo;

    def determinar_padre(self, value: Any):
        
        def __determinar_padre(root, value, padre):

            if root is not None:
                
                if value == root.value:
                    return padre

                elif value < root.value:
                    padre = root.value
                    return __determinar_padre(root.left, value, padre)
                
                else:
                    padre = root.value
                    return __determinar_padre(root.right, value, padre)

            padre = 0
            return padre
                
        padre = None

        if self.root is not None:
            padre = False
            padre = __determinar_padre(self.root, value, padre)

        return padre

    # e. determinar la altura de un árbol.

    def determinar_altura(self):
        def __determinar_altura(root, altura):
            if root is not None:
                __determinar_altura(root.left, altura)
                if root == self.root:
                    altura = root.height
                    return altura
                __determinar_altura(root.right, altura)

        altura = None

        if self.root is not None:
            altura = __determinar_altura(self.root, altura)

        return altura

# --------- CARGA DE DATOS --------- #

arbol_numeros = BinaryTreeAct()

arbol_numeros.insert(19)
arbol_numeros.insert(7)
arbol_numeros.insert(31)
arbol_numeros.insert(11)
arbol_numeros.insert(22)
arbol_numeros.insert(45)
arbol_numeros.insert(27)

# arbol_numeros.insert(191)
# arbol_numeros.insert(71)
# arbol_numeros.insert(311)
# arbol_numeros.insert(112)
# arbol_numeros.insert(224)
# arbol_numeros.insert(274)
# arbol_numeros.insert(455)

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

def print_seccion_extra(titulo, ancho=140, relleno=" ", color=Color.VERDE):
    print(f'{color}{f" {titulo} ".center(ancho, relleno)}{Color.RESET}')

#################################################  EJECUCIÓN DE PRUEBAS DEL ENUNCIADO  #################################################
print(f'\n{Color.CIAN}{f' EJERCICIO 11: RESOLVER ACTIVIDADES '.center(140, "=")}{Color.RESET}')

print(f'{Color.AZUL}Árbol original:{Color.RESET}')
arbol_numeros.in_order()

print_seccion('a. contar el número de nodos del árbol;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
nodos = arbol_numeros.contar_nodos()
print(f'  → {nodos}')

print_seccion('b. determinar el número de hojas del árbol;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
hojas = arbol_numeros.determinar_hojas()
print(f'  → {hojas}')

print_seccion('c. mostrar la información de los nodos hojas;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_numeros.mostrar_info_hojas()

print_seccion('d. determinar el padre de un nodo;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
buscado = 45
padre = arbol_numeros.determinar_padre(buscado)
if padre is not None:
    if padre is False:
        print(f'  → El nodo {buscado} no tiene padre, es el nodo raíz.')
    elif padre == 0:
        print(f'  → El nodo {buscado} no se encuentra en el árbol.')
    else:
        print(f'  → El nodo {buscado} tiene como padre al nodo {padre}')
else:
    print(f'  → El árbol está vacío.')

print_seccion('e. determinar la altura de un árbol.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
altura_arbol = arbol_numeros.determinar_altura()
if altura_arbol is not None:
    print(f'  → La altura del árbol es {altura_arbol}')
else:
    print('  → El árbol está vacío.')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')