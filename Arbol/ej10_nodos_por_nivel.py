# 10. Nodos por nivel
'''
Desarrollar dos algoritmos,
el primero que permita calcular en el número de nodos de un nivel del árbol –a partir de un nivel ingresado–.
La segunda que cuente los nodos que hay en dicho nivel –dado que podría no estar completo–, para responder las siguientes actividades:
a. determinar si el nivel del árbol está completo;
b. ¿cuántos nodos faltan para completar dicho nivel?
'''

from TDA_tree import BinaryTree

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

class BinaryTreeContarNodos(BinaryTree):

    def contar_nodos_nivel(self, nivel_buscado):

        def __contar_nodos_nivel(root, nivel_actual):
            if root is None:
                return 0

            if nivel_actual == nivel_buscado:
                return 1

            return (
                __contar_nodos_nivel(root.left, nivel_actual + 1)
                + __contar_nodos_nivel(root.right, nivel_actual + 1)
            )

        if self.root is None or nivel_buscado < 1:
            return 0

        return __contar_nodos_nivel(self.root, 1)

# --------- CARGA DE DATOS --------- #

arbol_numeros = BinaryTreeContarNodos()

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
print(f'\n{Color.CIAN}{f' EJERCICIO 11: CONTAR NODOS POR NIVEL '.center(140, "=")}{Color.RESET}')

print(f'{Color.AZUL}\nÁrbol original ordenado de menor a mayor:{Color.RESET}')
arbol_numeros.in_order()

# Para calcular el número máximo de nodos en un nivel de un árbol, se hace directamente con la fórmula.
print_seccion('Calcular el número de nodos de un nivel del árbol –a partir de un nivel ingresado–')
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
nivel = 3
print(f'  → Nivel: {nivel}')
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
cantidad_max_nodos = 2 ** (nivel - 1)
print(f'  → Número máximo de nodos en el nivel {nivel} de un árbol: {cantidad_max_nodos}')

# Para calcular el número de nodos en un nivel de un árbol específico, utilizamos la función.
print_seccion('Contar los nodos que hay en dicho nivel –dado que podría no estar completo–')
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
cantidad_nodos_arbol = arbol_numeros.contar_nodos_nivel(nivel)
print(f'  → Número de nodos en el nivel {nivel} del árbol dado: {cantidad_nodos_arbol}')

# a. determinar si el nivel del árbol está completo;
print_seccion('a. determinar si el nivel del árbol está completo;')
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if cantidad_max_nodos == cantidad_nodos_arbol:
    print(f'  → El nivel {nivel} del árbol está completo.')
else:
    print(f'  → El nivel {nivel} del árbol está incompleto.')

# b. ¿cuántos nodos faltan para completar dicho nivel?
print_seccion('b. ¿cuántos nodos faltan para completar dicho nivel?')
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
nodos_faltantes = cantidad_max_nodos - cantidad_nodos_arbol
if nodos_faltantes == 0:
    print(f'  → No falta ningún nodo para completar el nivel.')
else:
    print(f'  → Faltan {nodos_faltantes} nodo/s para completar dicho nivel.')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')