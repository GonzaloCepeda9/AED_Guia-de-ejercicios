# 8. Desarrollar un algoritmo que implemente dos funciones, una para obtener el mínimo nodo del árbol y la segunda para obtener el máximo.

from TDA_tree import BinaryTree

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

class BinaryTreeMinMax(BinaryTree):

    def obtener_minimo(self):

        if self.root is None:
            return None

        def __obtener_minimo(root, minimo):

            if root is None:
                return minimo

            minimo = __obtener_minimo(root.left, minimo)
            if root.value < minimo:
                minimo = root.value

            minimo = __obtener_minimo(root.right, minimo)

            return minimo

        minimo = self.root.value
        return __obtener_minimo(self.root, minimo)
    
    def obtener_maximo(self):

        if self.root is None:
            return None

        def __obtener_maximo(root, maximo):

            if root is None:
                return maximo

            maximo = __obtener_maximo(root.left, maximo)
            if root.value > maximo:
                maximo = root.value

            maximo = __obtener_maximo(root.right, maximo)

            return maximo

        maximo = self.root.value
        return __obtener_maximo(self.root, maximo)

# --------- CARGA DE DATOS --------- #

arbol_numeros = BinaryTreeMinMax()

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
print(f'\n{Color.CIAN}{f' EJERCICIO 8: OBTENER MÍNIMO Y MÁXIMO '.center(140, "=")}{Color.RESET}')

print(f'{Color.AZUL}Árbol original:{Color.RESET}')
arbol_numeros.in_order()

print_seccion('Mínimo nodo del árbol')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
minimo = arbol_numeros.obtener_minimo()
print(f'  → {minimo}')

print_seccion('Máximo nodo del árbol')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
maximo = arbol_numeros.obtener_maximo()
print(f'  → {maximo}')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')