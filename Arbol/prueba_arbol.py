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

# # Árbol con datos complejos
# arbol_superheroes = BinaryTree()
# for superheroe in lista_superheroes:
#     arbol_superheroes.insert(superheroe['nombre'], superheroe)

# ##########################################  EJECUCIÓN DE PRUEBAS DE ÁRBOL CON DATOS SIMPLES  ###########################################
# print('\n============================================= Prueba de árbol con datos simples ==============================================')
# # Barridos 
# print('\n------------------------------------------- Barridos inorder, postorder y preorden -------------------------------------------')
# print('\nBarrido inorder (hijo izquierdo → raíz → hijo derecho): ')
# arbol_numeros.in_order()
# print('\nBarrido postorder (hijo derecho → raíz → hijo izquierdo): ')
# arbol_numeros.post_order()
# print('\nBarrido preorder (nodo raíz → hijo izquierdo → hijo derecho): ')
# arbol_numeros.pre_order()

# # Búsqueda
# print('\n------------------------------------------------ Búsqueda por valor del nodo -------------------------------------------------')
# nodo = 22
# buscado = arbol_numeros.search(nodo)
# if buscado is not None:
#     print(buscado.value, buscado.left, buscado.right.value)

# #########################################  EJECUCIÓN DE PRUEBAS DE ÁRBOL CON DATOS COMPLEJOS  ##########################################
# print(f'\n============================================ Prueba de árbol con datos complejos ============================================')
# # Barridos 
# print('\n------------------------------------------- Barridos inorder, postorder y preorden -------------------------------------------')
# print('\nBarrido inorder (hijo izquierdo → raíz → hijo derecho): ')
# arbol_superheroes.in_order()
# print('\nBarrido postorder (hijo derecho → raíz → hijo izquierdo): ')
# arbol_superheroes.post_order()
# print('\nBarrido preorder (nodo raíz → hijo izquierdo → hijo derecho): ')
# arbol_superheroes.pre_order()

# # Búsquedas
# print('\n---------------------------------------------- Búsqueda por nombre de personaje ----------------------------------------------')
# posicion = arbol_superheroes.search('Spider-Man')
# if posicion is not None:
#     print(
#         f'El superhéroe se encuentra en la lista.'
#         f'\n• Valor del nodo: {posicion.value}'
#         f'\n• Valor a su izquierda: {posicion.left.value}'
#         f'\n• Valor a su derecha: {posicion.right.value}'
#     )

# posicion = arbol_superheroes.search('Wolverine')
# if posicion is not None:
#     print(
#         f'\nEl superhéroe se encuentra en la lista.'
#         f'\n• Valor del nodo: {posicion.value}'
#         f'\n• Valor a su izquierda: {posicion.left.value}'
#         f'\n• Valor a su derecha: {posicion.right}'
#     )