from TDA_tree import BinaryTree
from ej5_lista_personajes_comic import lista_personajes_comic

# --------- CARGA DE DATOS --------- #

# Árbol con datos simples
arbol_numeros = BinaryTree()
arbol_numeros.insert(50)
arbol_numeros.insert(70)
arbol_numeros.insert(60)
arbol_numeros.insert(30)
arbol_numeros.insert(20)
arbol_numeros.insert(40)
arbol_numeros.insert(10)

# Árbol con datos complejos
arbol_superheroes = BinaryTree()
for superheroe in lista_personajes_comic:
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

# # Caso 1 → El nodo no tiene hijos
# nodo_a_eliminar = 40
# print(f'\nÁrbol resultante luego de borrar {nodo_a_eliminar}')
# arbol.delete(nodo_a_eliminar)
# arbol.in_order()


# # Caso 2 → El nodo tiene un solo hijo
# nodo_a_eliminar = 20
# print(f'\nÁrbol resultante luego de borrar {nodo_a_eliminar}')
# arbol.delete(nodo_a_eliminar)
# arbol.in_order()


# Caso 3 → El nodo tiene hijo izquierdo e hijo derecho (llama a la función/herlper __replace)

# # 3A → El mayor del subárbol izquierdo es la raíz del subárbol izquierdo
# nodo_a_eliminar = 30
# print(f'\nÁrbol resultante luego de borrar {nodo_a_eliminar}')
# arbol.delete(nodo_a_eliminar)
# arbol.in_order()


# # 3B → El mayor del subárbol izquierdo NO es la raíz del subárbol izquierdo (debe buscar el último nodo de la derecha)
# nodo_a_eliminar = 50
# print(f'\nÁrbol resultante luego de borrar {nodo_a_eliminar}')
# arbol.delete(nodo_a_eliminar)
# arbol.in_order()

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

# División
print_seccion('División del árbol en superhéroes y villanos')
print(f'Árbol completo ordenado alfabéticamente: ')
arbol_superheroes.in_order()

print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
arbol_supervillanos = BinaryTree()
arbol_heroes = BinaryTree()
condition = 'is_villain'
print(f'  → Condición para división: {condition}')

print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
print(f'\nÁrbol con villanos: ')
arbol_supervillanos.in_order()
print(f'\nÁrbol con héroes: ')
arbol_superheroes.in_order()

arbol_superheroes.divide_tree(arbol_supervillanos, arbol_heroes, condition)
