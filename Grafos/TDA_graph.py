from TDA_list import List
from typing import Any, Optional

class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values # Aún no está en uso
            self.visited = False

        def __str__(self):
            return self.value

    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # Aún no está en uso

        def __str__(self):
            return f'  → Destination: {self.value} | Weight: {self.weight}'

    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight

    def __init__(self, is_directed: bool = False):

        self.add_criterion('value', self._order_by_value)

        self.is_directed = is_directed

    def show(self) -> None:
        for vertex in self:
            print(f'Vertex: {vertex}')
            vertex.edges.show()

    def insert_vertex(self, value: Any) -> None:
        node_vertex = Graph.__nodeVertex(value)
        self.insert_value(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search('value', origin_vertex)
        destination = self.search('value', destination_vertex)
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.insert_value(node_edge)                  # En el código original está con .append()
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.insert_value(node_edge)         # En el código original está con .append()
        else:
            print('No se puede insertar. Falta al menos un vértice.')   # Este mensaje no debe ir acá. Modificar luego.

    def delete_edge(self, key_value: str, origin: Any, destination: Any) -> Optional[Any]:
        pos_origin = self.search(key_value, origin)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(key_value, destination)
            if pos_origin is not None and not self.is_directed:
                pos_destination = self.search(key_value, destination)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(key_value, origin)
            return edge

    def delete_vertex(self, value, key_value_vertex: str = None, key_value_edges: str = 'value'):
        delete_value = self.delete_value(key_value_vertex, value)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(key_value_edges, vertex.value, value)
        return delete_value

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def deep_sweep(self, value) -> None:
        def __deep_sweep(graph, value):
            pos_vertex = graph.search('value', value) # Si la busqueda de arista no se encuentra, falla y no ejecuta lo que está dentro del condicional.
            if pos_vertex is not None:
                if graph[pos_vertex].visited is False:
                    graph[pos_vertex].visited = True
                    print(graph[pos_vertex])
                    for edge in graph[pos_vertex].edges:
                        pos_edge = graph.search('value', edge.value)
                        if graph[pos_edge].visited is False:
                            __deep_sweep(graph, graph[pos_edge].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)


graph_letters = Graph(is_directed = True)

graph_letters.insert_vertex('A')
graph_letters.insert_vertex('B')
graph_letters.insert_vertex('C')
graph_letters.insert_vertex('D')
graph_letters.insert_vertex('E')
graph_letters.insert_vertex('F')

graph_letters.insert_edge('A', 'B', 7)
graph_letters.insert_edge('A', 'D', 5)
graph_letters.insert_edge('A', 'C', 5)
graph_letters.insert_edge('B', 'D', 4)
graph_letters.insert_edge('B', 'E', 11)
graph_letters.insert_edge('C', 'F', 9)
graph_letters.insert_edge('C', 'E', 18)
graph_letters.insert_edge('D', 'C', 2)
graph_letters.insert_edge('E', 'F', 6)
graph_letters.insert_edge('F', 'D', 1) 
    
print('\n--------------------------- Borrar una arista ---------------------------')
print(f'Grafo original: ')
graph_letters.show()

edge_origin = 'A'
edge_destination = 'B'
edge_deleted = graph_letters.delete_edge('value', edge_origin, edge_destination)

if edge_deleted is not None:
    print(f'\nLa arista {edge_origin} → {edge_destination} ha sido eliminada.')
    if graph_letters.is_directed is False:
        print(f'\nLa arista {edge_destination} → {edge_origin} ha sido eliminada.')
else:
    print(f'La arista {edge_origin} → {edge_destination} no se encuentra en el Grafo.')
print(f'\nGrafo actualizado: ')
graph_letters.show()

print(f'\n--------------------------- Borrar un vértice ---------------------------')
vertex_deleted = 'C'
criterion_deleted = 'value'
delete_value = graph_letters.delete_vertex(vertex_deleted, criterion_deleted)

# print(f'\nTipo de dato de la variable "delete_value": {type(delete_value)}')
# print(f'\nValor del vértice: {delete_value}')

if delete_value is not None:
    print(f'\nBorrando vértice {vertex_deleted} y sus aristas...')
    print(f'\nGrafo actualizado: ')
    graph_letters.show()
else:
    print(f'\nEl vértice {vertex_deleted} no se encuentra en el grafo.')

print(f'\n--------------------------- Barrido en profundidad ---------------------------')
graph_letters.mark_as_unvisited()
graph_letters.deep_sweep('A')