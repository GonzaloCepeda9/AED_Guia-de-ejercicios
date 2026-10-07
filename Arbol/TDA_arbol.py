from typing import Any, Optional

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.height = 0                     # Convención: Un nodo hoja tiene altura 0, y un nodo inexistente (None) tiene altura -1

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                nodo = BinaryTree.__nodeTree(value, other_values)
                # print(f'Nuevo nodo: {nodo.value}')
                return nodo
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
                # print(f'Nodo izquierdo: {root.left.value}')
            else:
                root.right = __insert(root.right, value, other_values)
                # print(f'Nodo derecho: {root.right.value}')

            # print(f'Nodo root: {root.value}')
            root = self.auto_balance(root)
            self.update_height(root)
            return root
        # print('----------------------------------------------------')

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
            def __pre_order(root):
                if root is not None:
                    print(f'  → {root.value}') 
                    __pre_order(root.left)
                    __pre_order(root.right)
    
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(f'  → {root.value}')            # Este print sería "procesar el nodo".
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(f'  → {root.value}')               # Este print sería "procesar el nodo".
                __post_order(root.left)

        if self.root is not None:    
            __post_order(self.root)

    def by_level(self):
        pass

    def search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if value == root.value:
                    # print(f'Valor encontrado')  # Este print sería "procesar el nodo".
                    return root
                elif value < root.value:
                    # print(f'Me voy a buscar a la izquierda')
                    return __search(root.left, value)
                else:
                    # print(f'Me voy a buscar a la derecha')
                    return __search(root.right, value)
        aux = None
        if self.root is not None:                   # Antes de llamar a la función, verifica que la raíz no sea None.
            aux = __search(self.root, value)
        return aux

    def proximity_search():
        pass

    def delete(self, value):
        
        def __replace(root):

            # Caso 3A → El mayor del subárbol izquierdo es la raíz del subárbol izquierdo
            if root.right is None:
                return root.left, root

            # Caso 3B → El mayor del subárbol izquierdo NO es la raíz del subárbol izquierdo (debe buscar el último nodo de la derecha)
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            if root is None:
                return None
            if value < root.value:
                root.left = __delete(root.left, value)
            elif value > root.value:
                root.right = __delete(root.right, value)
            else:
                # Caso 1 → El nodo no tiene hijos
                if root.left is None and root.right is None:
                    return None # Al devolver None, el nodo padre deja de apuntar al valor encontrado y apunta a None. Entonces, queda desconectado del árbol (al buscado ya nadie lo referencia).

                # Caso 2 → El nodo tiene un solo hijo
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                # Caso 3 → El nodo tiene hijo izquierdo e hijo derecho (llama a la función/herlper __replace)
                else:
                    root.left, replace_node = __replace(root.left)
                    root.value = replace_node.value
                    root.other_values = replace_node.other_values
                
            return root

        self.root = __delete(self.root, value)

    def by_level(self):
        pass

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            alt_left = self.height(root.left)
            alt_right = self.height(root.right)
            root.height = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control:
        # Si control es True, quiere decir que está cargado a la izquierda, por lo tanto se realiza una rotación simple a la derecha.
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
        # Si control es False, quiere decir que está cargado a la derecha, por lo tanto se realiza una rotación simple a la izquierda.
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        return aux

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                control = True
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, control)
                else:
                    root = self.double_rotation(root, control)
            elif self.height(root.right) - self.height(root.left) == 2:
                control = False
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, control)
                else:
                    root = self.double_rotation(root, control)
        return root

        # Si control es True, quiere decir que está cargado a la izquierda, por lo tanto se realiza una rotación simple a la derecha.

        # Si control es False, quiere decir que está cargado a la derecha, por lo tanto se realiza una rotación simple a la izquierda.