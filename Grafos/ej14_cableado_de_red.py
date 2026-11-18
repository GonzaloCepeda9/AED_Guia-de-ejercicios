# 14. Cableado de red en el hogar
'''
Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
'''

from ej14_listas import ambientes, conexiones
from ED_graph import Graph
from ED_list import List

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #


# --------- CARGA DE DATOS --------- #

graph_home_network_cabling = Graph(is_directed=False)

# VÉRICES

for ambiente in ambientes:
    graph_home_network_cabling.insert_vertex(ambiente['value'])

# ARISTAS

for conexion in conexiones:
    graph_home_network_cabling.insert_edge(conexion['origin'], conexion['destination'], conexion['weight'])

# graph_home_network_cabling.show()

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
print(f'\n{Color.CIAN}{f' EJERCICIO 14: CABLEADO DE RED EN EL HOGAR '.center(140, "=")}{Color.RESET}')

# # a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# print_seccion('a. cada vértice representar un ambiente de una casa: ')
# print_seccion_extra('cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;')


# # b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# print_seccion('b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, ')
# print_seccion_extra('el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;')


# # c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# print_seccion('c. obtener el árbol de expansión mínima y determine cuantos metros de cables ')
# print_seccion_extra('se necesitan para conectar todos los ambientes;')
# expansion_tree = graph_home_network_cabling.kruskal('Sala de estar')
# print(f'\n{expansion_tree}')

# list_elements_mst = expansion_tree.split(';')
# print(f'\n{list_elements_mst}')

# number_of_edges = 0
# total_weight = 0

# print(f'{Color.VIOLETA}Resultado:{Color.RESET}')

# print(f'\n{Color.AZUL}  Árbol de expansión mínima: {Color.RESET}')
# for element in list_elements_mst:
#     origin, destination, weight = element.split('-')
#     print(f'  → Arista: {origin} — {destination} | Peso: {weight}')
#     number_of_edges += 1 
#     total_weight += int(weight)

# print(f'\n  Cantidad de aristas del grafo: {number_of_edges}.')
# print(f'\n  Peso total del grafo: {total_weight}.')

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
print_seccion('d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para ')
print_seccion_extra('determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.')

path = graph_home_network_cabling.dijkstra('Habitación 1')

path.show()

destination = 'Sala de estar'

complete_path = List()

while not path.is_empty():
    pass




print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')

