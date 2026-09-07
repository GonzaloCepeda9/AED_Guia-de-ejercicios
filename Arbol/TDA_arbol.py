from typing import Any, Optional

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                nodo = BinaryTree.__nodeTree(value, other_values)
                print(f'Nuevo nodo: {nodo.value}')
                return nodo
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
                print(f'Nodo izquierdo: {root.left.value}')
            else:
                root.right = __insert(root.right, value, other_values)
                print(f'Nodo derecho: {root.right.value}')

            print(f'Nodo root: {root.value}')
            return root
        print('----------------------------------------------------')

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
            def __pre_order(root):
                if root is not None:
                    print(root.value)           # Este print sería "procesar el nodo".
                    __pre_order(root.left)
                    __pre_order(root.right)
    
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value)              # Este print sería "procesar el nodo".
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)               # Este print sería "procesar el nodo".
                __post_order(root.left)

        if self.root is not None:    
            __post_order(self.root)

    def search(self, value: Any):
        def __search(root, value):
            if root is not None:
                if value == root.value:
                    # print(f'Valor encontrado')
                    return root
                elif value < root.value:
                    # print(f'Me voy a buscar a la izquierda')
                    return __search(root.left, value)
                else:
                    # print(f'Me voy a buscar a la derecha')
                    return __search(root.right, value)
        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux