from TDA_tree import BinaryTree

class BinaryTreeMinMax(BinaryTree):

    def obtener_minimo(self):

        if self.root is None:  # Comprueba si el árbol completo está vacío.
            return None        # Si está vacío, termina y retorna None.

        def __obtener_minimo(root, minimo):
            # Función recursiva interna. Recibe el nodo que se va a evaluar
            # y el mínimo acumulado hasta ese momento.

            if root is None:
                # Comprueba si el nodo que se intenta visitar existe.
                # Si es None, devuelve el mínimo acumulado a la llamada anterior.
                return minimo

            minimo = __obtener_minimo(root.left, minimo)
            # Primero recorre el subárbol izquierdo. Cuando esa llamada termina,
            # guarda el mínimo que devuelve en el minimo local de esta llamada.

            if root.value < minimo:
                # Compara el valor del nodo actual con el mínimo acumulado.
                minimo = root.value
                # Si el valor actual es menor, actualiza el mínimo.

            minimo = __obtener_minimo(root.right, minimo)
            # Después recorre el subárbol derecho usando el mínimo actualizado
            # y guarda el valor que devuelve esa llamada.

            return minimo
            # Devuelve el mínimo resultante a la llamada anterior.

        minimo = self.root.value
        # Inicializa el mínimo con el valor de la raíz.

        return __obtener_minimo(self.root, minimo)
        # Inicia el recorrido desde la raíz y devuelve el resultado final.