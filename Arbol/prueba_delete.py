from TDA_arbol import BinaryTree

arbol = BinaryTree()
arbol.insert(50)
arbol.insert(70)
arbol.insert(60)
arbol.insert(30)
arbol.insert(20)
arbol.insert(40)
arbol.insert(10)

print(f'\nÁrbol original')
arbol.in_order()

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