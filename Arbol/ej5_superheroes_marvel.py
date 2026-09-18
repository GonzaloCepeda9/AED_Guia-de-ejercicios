# 5. Superhéroes y villanos de Marvel Cinematic Universe (MCU)
'''
Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
    I. determinar cuántos nodos tiene cada árbol;
    II. realizar un barrido ordenado alfabéticamente de cada árbol.
'''

from TDA_arbol import BinaryTree
from ej5_lista_superheroes import lista_superheroes
from typing import Any, Optional

# --------- CARGA DE DATOS ---------
arbol_superheroes = BinaryTree()
arbol_ordenado_por_campo = BinaryTree()

for superheroe in lista_superheroes:
    arbol_superheroes.insert(superheroe['nombre'], superheroe)

for superheroe in lista_superheroes:
    arbol_ordenado_por_campo.insert(superheroe['nombre'], superheroe)

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

# b. listar los villanos ordenados alfabéticamente;
def listar_villanos(arbol: BinaryTree):
    def __listar_villanos(root):
        if root is not None:
            __listar_villanos(root.left)
            if root.other_values['is_villain'] == True:
                    print(f'  → {root.value}')
            __listar_villanos(root.right)

    if arbol.root is not None:
        __listar_villanos(arbol.root)

# c. mostrar todos los superhéroes que empiezan con C;
def mostrar_por_inicial(arbol: BinaryTree):
    def __mostrar_por_inicial(root):
        if root is not None:
            __mostrar_por_inicial(root.left)
            if root.value.startswith('C'):
                    print(f'  → {root.value}')
            __mostrar_por_inicial(root.right)

    if arbol.root is not None:
        __mostrar_por_inicial(arbol.root)

# d. determinar cuántos superhéroes hay el árbol;
def determinar_superheroes(arbol: BinaryTree):
    def __determinar_superheroes(root, contador: int = 0):
        if root is not None:
            contador = __determinar_superheroes(root.left, contador)
            if root.other_values['is_villain'] == False:
                contador += 1
            contador = __determinar_superheroes(root.right, contador)
        return contador

    if arbol.root is None:
        return 0

    return __determinar_superheroes(arbol.root)

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:

def insertar_por_campo(arbol, value: Any, other_values: Optional[Any] = None):
    def __insertar_por_campo(root, value, other_values):
        if root is None:
            nodo = BinaryTree.__nodeTree(value, other_values)
            return nodo
        elif other_values['is_villain'] == False:
            root.left = __insertar_por_campo(root.left, value, other_values)
        else:
            root.right = __insertar_por_campo(root.right, value, other_values)
        return root

    arbol.root = __insertar_por_campo(arbol.root, value, other_values)

#     I. determinar cuántos nodos tiene cada árbol;
def determinar_superheroe_o_villano(arbol: BinaryTree):
    def __determinar_superheroe_o_villano(root, contador_superheroes: int = 0, contador_villanos: int = 0):
        if root is not None:
            contador_superheroes, contador_villanos = __determinar_superheroe_o_villano(root.left, contador_superheroes, contador_villanos)
            if root.other_values['is_villain'] == False:
                contador_superheroes += 1
            else:
                contador_villanos += 1
            contador_superheroes, contador_villanos = __determinar_superheroe_o_villano(root.right, contador_superheroes, contador_villanos)
        return contador_superheroes, contador_villanos

    if arbol.root is None:
        return 0, 0

    return __determinar_superheroe_o_villano(arbol.root)

#     II. realizar un barrido ordenado alfabéticamente de cada árbol.


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
print(f'\n{Color.CIAN}{f' EJERCICIO 5: SUPERHÉROES Y VILLANOS DE MARVEL CINEMATIC UNIVERSE (MCU) '.center(140, "=")}{Color.RESET}')

print_seccion('Información completa de superhéroes')
print(f'{Color.AZUL}Lista original ordenada alfabéticamente:{Color.RESET}')
arbol_superheroes.in_order()

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
print_seccion('a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano')
print_seccion_extra('que indica si es un héroe o un villano, True y False respectivamente;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → En el campo "other_values" de cada nodo del árbol se almacenó la información completa de cada superhéroe.')

# b. listar los villanos ordenados alfabéticamente;
print_seccion('# b. listar los villanos ordenados alfabéticamente;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
listar_villanos(arbol_superheroes)

# c. mostrar todos los superhéroes que empiezan con C;
print_seccion('c. mostrar todos los superhéroes que empiezan con C;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
mostrar_por_inicial(arbol_superheroes)

# d. determinar cuántos superhéroes hay el árbol;
print_seccion('d. determinar cuántos superhéroes hay el árbol;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
cantidad = determinar_superheroes(arbol_superheroes)
if cantidad > 0:
    print(f'  → En el árbol hay {cantidad} superhéroes.')
else:
    print(f'  → No se encontraron superhéroes en el árbol.')

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
print_seccion('e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad')
print_seccion_extra('para encontrarlo en el árbol y modificar su nombre;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → Aún no desarrollado en clase.')

# f. listar los superhéroes ordenados de manera descendente;
print_seccion('f. listar los superhéroes ordenados de manera descendente;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_superheroes.post_order()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
print_seccion('g. generar un bosque a partir de este árbol...')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → Aún no desarrollado en clase.')

#     I. determinar cuántos nodos tiene cada árbol;
print_seccion_extra('\nI. determinar cuántos nodos tiene cada árbol;')
cantidad_superheroes, cantidad_villanos = determinar_superheroe_o_villano(arbol_ordenado_por_campo)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → El subárbol de superheroes contiene {cantidad_superheroes} nodos.')
print(f'  → El subárbol de villanos contiene {cantidad_villanos} nodos.')

#     II. realizar un barrido ordenado alfabéticamente de cada árbol.
print_seccion_extra('\nII. realizar un barrido ordenado alfabéticamente de cada árbol.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → Aún no desarrollado en clase.')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')