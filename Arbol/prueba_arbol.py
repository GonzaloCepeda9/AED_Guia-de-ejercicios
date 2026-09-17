from TDA_arbol import BinaryTree
from superheroes import lista_superheroes

# --------- CARGA DE DATOS --------- #

# Árbol con datos simples
arbol_numeros = BinaryTree()
arbol_numeros.insert(19)
arbol_numeros.insert(7)
arbol_numeros.insert(31)
arbol_numeros.insert(11)
arbol_numeros.insert(22)
arbol_numeros.insert(45)
arbol_numeros.insert(27)

# Árbol con datos complejos
arbol_superheroes = BinaryTree()
for superheroe in lista_superheroes:
    arbol_superheroes.insert(superheroe['nombre'], superheroe)

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

##########################################  EJECUCIÓN DE PRUEBAS DE ÁRBOL CON DATOS SIMPLES  ###########################################
print(f'\n{Color.CIAN}{f' PRUEBA DE ÁRBOL CON DATOS SIMPLES '.center(140, "=")}{Color.RESET}')
# Barridos 
print_seccion('Barridos')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')

print(f'\n  Barrido inorder (hijo izquierdo → raíz → hijo derecho):')
arbol_numeros.in_order()

print(f'\n  Barrido postorder (hijo derecho → raíz → hijo izquierdo):')
arbol_numeros.post_order()

print(f'\n  Barrido preorder (nodo raíz → hijo izquierdo → hijo derecho):')
arbol_numeros.pre_order()

# Búsqueda
print_seccion('Búsqueda por valor del nodo: ')
print(f'Árbol ordenado de menor a mayor: ')
arbol_numeros.in_order()
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
numero = 22
print(f'  → {numero}')

print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
buscado = arbol_numeros.search(numero)
if buscado is not None:
    print(
        f'  → El nodo se encuentra en la lista.'
        f'\n    - Valor del nodo: {buscado.value}'
        f'\n    - Valor a su izquierda: {buscado.left}'
        f'\n    - Valor a su derecha: {buscado.right.value}'
    )
else:
    print(f'  → No se encontró el número {numero}.')


#########################################  EJECUCIÓN DE PRUEBAS DE ÁRBOL CON DATOS COMPLEJOS  ##########################################
print(f'\n{Color.CIAN}{f' PRUEBA DE ÁRBOL CON DATOS COMPLEJOS '.center(140, "=")}{Color.RESET}')
# Barridos 
print_seccion('Barridos')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')

print(f'\nBarrido inorder (hijo izquierdo → raíz → hijo derecho):')
arbol_superheroes.in_order()

print(f'\nBarrido postorder (hijo derecho → raíz → hijo izquierdo):')
arbol_superheroes.post_order()

print(f'\nBarrido preorder (nodo raíz → hijo izquierdo → hijo derecho):')
arbol_superheroes.pre_order()

# Búsquedas
print_seccion('Búsqueda por nombre del personaje')
print(f'Árbol ordenado alfabéticamente: ')
arbol_superheroes.in_order()
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
superheroe = 'Spider-Man'
print(f'  → {superheroe}')

print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
buscado = arbol_superheroes.search(superheroe)
if buscado is not None:
    print(
        f'  → El superhéroe {superheroe} se encuentra en la lista.'
        f'\n    - Valor del nodo: {buscado.value}'
        f'\n    - Valor a su izquierda: {buscado.left.value}'
        f'\n    - Valor a su derecha: {buscado.right.value}'
        f'\n\n  → Información completa del superhéroe buscado: \n{buscado.other_values}'
        f'\n    - {buscado.other_values}'
    )
else:
    print(f'  → El superhéroe {superheroe} no se encuentra en el árbol.')

print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
superheroe = 'Wolverine'
buscado = arbol_superheroes.search(superheroe)
print(f'  → {superheroe}')
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if buscado is not None:
    print(
        f'  → El superhéroe {superheroe} se encuentra en la lista.'
        f'\n    - Valor del nodo: {buscado.value}'
        f'\n    - Valor a su izquierda: {buscado.left.value}'
        f'\n    - Valor a su derecha: {buscado.right}'
        f'\n\n  → Información completa del superhéroe buscado:'
        f'\n    - {buscado.other_values}'
    )
else:
    print(f'  → El superhéroe {superheroe} no se encuentra en el árbol.')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')