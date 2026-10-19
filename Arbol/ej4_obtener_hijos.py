# 4. Implementar un algoritmo que contemple dos funciones, la primera que devuelva el hijo derecho de un nodo y la segunda que devuelva el hijo izquierdo.

from TDA_tree import BinaryTree

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

class BinaryTreeHijos(BinaryTree):

    def obtener_hijo_derecho(self, value):
        def __obtener_hijo_derecho(root, value):
            if root is not None:
                if value == root.value:
                    return root
                elif value < root.value:
                    return __obtener_hijo_derecho(root.left, value)
                else:
                    return __obtener_hijo_derecho(root.right, value)
        aux = None
        if self.root is not None:                   # Antes de llamar a la función, verifica que la raíz no sea None.
            aux = __obtener_hijo_derecho(self.root, value)
        return aux

    def obtener_hijo_izquierdo(self, value):
        def __obtener_hijo_izquierdo(root, value):
            if root is not None:
                if value == root.value:
                    return root
                elif value < root.value:
                    return __obtener_hijo_izquierdo(root.left, value)
                else:
                    return __obtener_hijo_izquierdo(root.right, value)
        aux = None
        if self.root is not None:                   # Antes de llamar a la función, verifica que la raíz no sea None.
            aux = __obtener_hijo_izquierdo(self.root, value)
        return aux

# --------- CARGA DE DATOS --------- #
arbol_numeros = BinaryTreeHijos()

arbol_numeros.insert(19)
arbol_numeros.insert(7)
arbol_numeros.insert(31)
arbol_numeros.insert(11)
arbol_numeros.insert(22)
arbol_numeros.insert(27)
arbol_numeros.insert(45)

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
print(f'\n{Color.CIAN}{f' EJERCICIO 4: OBTENCIÓN DE HIJOS IZQUIERDO Y DERECHO '.center(140, "=")}{Color.RESET}')
print_seccion('Implementar un algoritmo que contemple dos funciones: ')

# Obtener hijo derecho
print_seccion_extra(f'\n...la primera que devuelva el hijo derecho de un nodo')
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
nodo_buscado = 19
print(f'  → {nodo_buscado}')

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
resultado = arbol_numeros.obtener_hijo_derecho(nodo_buscado)
if resultado is not None:
    if resultado.right is not None:
        print(f'  → El hijo derecho del nodo {nodo_buscado} es {resultado.right.value}.')
    else:
        print(f'  → El nodo {nodo_buscado} no tiene hijo derecho.')
else:
    print(f'  → El nodo {nodo_buscado} no se encuentra en el árbol.')

# Obtener hijo izquierdo
print_seccion_extra(f'\n...y la segunda que devuelva el hijo izquierdo.')
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
nodo_buscado = 19
print(f'  → {nodo_buscado}')

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
resultado = arbol_numeros.obtener_hijo_izquierdo(nodo_buscado)
if resultado is not None:
    if resultado.left is not None:
        print(f'  → El hijo izquierdo del nodo {nodo_buscado} es {resultado.left.value}.')
    else:
        print(f'  → El nodo {nodo_buscado} no tiene hijo izquierdo.')
else:
    print(f'  → El nodo {nodo_buscado} no se encuentra en el árbol')                                                            
print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')