from TDA_list import List
from typing import Any, Optional

class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.other_values = other_values # Aún no está en uso

        def __str__(self):
            return self.value


    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # Aún no está en uso

        def __str__(self):
            return f'  → Destination: {self.value} | Weight: {self.weight}'

    CRITERION_FUNCTIONS = {}

    def __init__(self, is_directed = True):

        def order_by_value(item):
            return item.value

        self.add_criterion('value', order_by_value)

        self.is_directed = is_directed

    def add_criterion(self, key_criterion: str, function):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self) -> None:
        for vertex in self:
            print(f'Vertex: {vertex}')
            vertex.edges.show()

    def insert_vertex(self, value: Any) -> None:
        node_vertex = Graph.__nodeVertex(value)
        self.insert_value(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search(origin_vertex)
        destination = self.search(destination_vertex)
        print(f'Resultado de buscar origen... {origin}')
        print(f'Resultado de buscar destino... {destination}')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.insert_value(node_edge)                  # En el código original está con .append()
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.insert_value(node_edge)         # En el código original está con .append()
        else:
            print('No se puede insertar. Falta al menos un vértice.')   # Este mensaje no debe ir acá. Modificar luego.

    # def delete_value(self, value, key_value: str = None) -> Optional[Any]:
    #     index = self.search(value, key_value)
    #     if index is not None:
    #         return self.pop(index)
    #     else:
    #         return index

    def sort_by_criterion(self, criterion_key: str = None):
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('Criterio de orden no encontrado.')

    def search(self, search_value, search_key: str = 'value') -> int:

        # Búsqueda binaria
        self.sort_by_criterion(search_key)
        criterion = self.CRITERION_FUNCTIONS.get(search_key)
        if criterion is None and self and not isinstance(self[0], (int, str, bool)):
            return None
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            value = criterion(self[middle]) if criterion else self[middle] # Si hay criterio se ejecuta la función; si no, se pasa el dato directamente.
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            elif value > search_value:
                end = middle - 1   
            middle = (start + end) // 2

        return None

graph_letras = Graph()

graph_letras.insert_vertex('A')
graph_letras.insert_vertex('B')
graph_letras.insert_vertex('C')
graph_letras.insert_vertex('D')
graph_letras.insert_vertex('E')
graph_letras.insert_vertex('F')

graph_letras.insert_edge('A', 'B', 7)
graph_letras.insert_edge('A', 'D', 5)
graph_letras.insert_edge('A', 'C', 5)
graph_letras.insert_edge('B', 'D', 4)
graph_letras.insert_edge('B', 'E', 11)
graph_letras.insert_edge('C', 'F', 9)
graph_letras.insert_edge('C', 'E', 18)
graph_letras.insert_edge('D', 'C', 2)
graph_letras.insert_edge('E', 'F', 6)
graph_letras.insert_edge('F', 'D', 1)

graph_letras.show()            