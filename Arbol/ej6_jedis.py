# 6. Jedis
'''
Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las siguientes consignas:
a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
b. realizar un barrido inorden del árbol por nombre y ranking;
c. realizar un barrido por nivel de los árboles por ranking y especie;
d. mostrar toda la información de Yoda y Luke Skywalker;
e. mostrar todos los Jedi con ranking “Jedi Master”;
f. listar todos los Jedi que utilizaron sabe de luz color verde;
g. listar todos los Jedi cuyos maestros están en el archivo;
h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
'''

from TDA_tree import BinaryTree
from TDA_queue import Queue
from TDA_list import List
from ej6_lista_jedis import lista_jedis

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

class BinaryTreeJedis(BinaryTree):

    def in_order_completo(self):
        def __in_order_completo(root):
            if root is not None:
                __in_order_completo(root.left)
                print(f'  → {root.value} | {root.other_values}')
                __in_order_completo(root.right)

        if self.root is not None:
            __in_order_completo(self.root)

    def by_level_completo(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(f'  → {node.value} | {node.other_values}') 
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    # e. mostrar todos los Jedi con ranking “Jedi Master”;

    def mostrar_jedi_master(self):
        def __mostrar_jedi_master(root):
            if root is not None:
                __mostrar_jedi_master(root.left)
                if root.value == 'Jedi Master':
                    print(f'  → {root.value} | {root.other_values}')
                __mostrar_jedi_master(root.right)

        if self.root is not None:
            __mostrar_jedi_master(self.root)

    # f. listar todos los Jedi que utilizaron sabe de luz color verde;

    def listar_por_sable(self):
        def __listar_por_sable(root):
            if root is not None:
                __listar_por_sable(root.left)
                if 'verde' in root.other_values['color_sable']:
                    print(f'  → {root.value} | Sables utilizados: {root.other_values['color_sable']}')
                __listar_por_sable(root.right)

        if self.root is not None:
            __listar_por_sable(self.root)

    # g. listar todos los Jedi cuyos maestros están en el archivo;

    def listar_por_maestro(self, lista_maestros):

        def __listar_por_maestro(root, lista_maestros):
            if root is not None:
                __listar_por_maestro(root.left, lista_maestros)
                for maestro in root.other_values['maestros']:
                    if maestro in lista_maestros:
                        print(f'  → Jedi: {root.value} | Maestro: {maestro}')
                __listar_por_maestro(root.right, lista_maestros)

        if self.root is not None:
            __listar_por_maestro(self.root, lista_maestros)
    
    # h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;

    def mostrar_por_especie(self):
        def __mostrar_por_especie(root):
            if root is not None:
                __mostrar_por_especie(root.left)
                if root.value == 'Togruta' or root.value == 'Cerean':
                    print(f'  → {root.other_values['nombre']} | Especie: {root.value}')
                __mostrar_por_especie(root.right)

        if self.root is not None:
            __mostrar_por_especie(self.root)

    # i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.

    def listar_por_coincidencia(self):
        def __listar_por_coincidencia(root):
            if root is not None:
                __listar_por_coincidencia(root.left)
                if root.value.startswith('A') or '-' in root.value:
                    print(f'  → {root.value}')
                __listar_por_coincidencia(root.right)

        if self.root is not None:
            __listar_por_coincidencia(self.root)

class ListaJedis(List):

    def show(self):
        for element in self:
            print(f'  → {element}')

# --------- CARGA DE DATOS --------- #

# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;

arbol_jedis_nombre = BinaryTreeJedis()
arbol_jedis_especie = BinaryTreeJedis()
arbol_jedis_ranking = BinaryTreeJedis()

for jedi in lista_jedis:
    datos = {
        "nombre": jedi['nombre'],
        "especie": jedi['especie'],
        "anio_nacimiento": jedi['anio_nacimiento'],
        "color_sable": jedi["color_sable"],
        "ranking": jedi['ranking'],
        "maestros": jedi['maestros']  
    }

    datos_copy_1 = datos.copy()
    datos_copy_1.pop('nombre')
    arbol_jedis_nombre.insert(jedi['nombre'], datos_copy_1)

    datos_copy_2 = datos.copy()
    datos_copy_2.pop('especie')
    arbol_jedis_especie.insert(jedi['especie'], datos_copy_2)

    datos_copy_3 = datos.copy()
    datos_copy_3.pop('ranking')
    for ranking in jedi['ranking']:
        arbol_jedis_ranking.insert(ranking, datos_copy_3)

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
print(f'\n{Color.CIAN}{f' EJERCICIO 6: JEDIS '.center(140, "=")}{Color.RESET}')

# b. realizar un barrido inorden del árbol por nombre y ranking;
print_seccion('b. realizar un barrido inorden del árbol por nombre y ranking;')
print(f'{Color.AZUL}Barrido in_order por nombre:{Color.RESET}')
arbol_jedis_nombre.in_order()
# arbol_jedis_nombre.in_order_completo()

print(f'{Color.AZUL}\nBarrido in_order por ranking:{Color.RESET}')
arbol_jedis_ranking.in_order()
# arbol_jedis_ranking.in_order_completo()

# print(f'{Color.AZUL}\nÁrbol ordenado por especie:{Color.RESET}')
# arbol_jedis_especie.in_order()
# arbol_jedis_especie.in_order_completo()

# c. realizar un barrido por nivel de los árboles por ranking y especie;
print_seccion('c. realizar un barrido por nivel de los árboles por ranking y especie;')
print(f'{Color.AZUL}Barrido by_level_completo por ranking:{Color.RESET}')
arbol_jedis_ranking.by_level()
# arbol_jedis_ranking.by_level_completo()

print(f'{Color.AZUL}\nBarrido by_level por especie:{Color.RESET}')
arbol_jedis_especie.by_level()
# arbol_jedis_especie.by_level_completo()

# d. mostrar toda la información de Yoda y Luke Skywalker;
print_seccion('d. mostrar toda la información de Yoda y Luke Skywalker;')

# Yoda
print(f'{Color.AZUL}Datos ingresados:{Color.RESET}')
jedi_buscado = 'Yoda'
print(f'  → {jedi_buscado}')
buscado = arbol_jedis_nombre.search(jedi_buscado)
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if buscado is not None:
    print(f'  → {buscado.value} | {buscado.other_values}')
else:
    print(f'  → El Jedi {jedi_buscado} no se encuentra en el árbol.')

# Luke Skywalker
print(f'{Color.AZUL}\nDatos ingresados:{Color.RESET}')
jedi_buscado = 'Luke Skywalker'
print(f'  → {jedi_buscado}')
buscado = arbol_jedis_nombre.search(jedi_buscado)
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
if buscado is not None:
    print(f'  → {buscado.value} | {buscado.other_values}')
else:
    print(f'  → El Jedi {jedi_buscado} no se encuentra en el árbol.')

# e. mostrar todos los Jedi con ranking “Jedi Master”;
print_seccion('e. mostrar todos los Jedi con ranking “Jedi Master”;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_jedis_ranking.mostrar_jedi_master()

# f. listar todos los Jedi que utilizaron sabe de luz color verde;
print_seccion('f. listar todos los Jedi que utilizaron sabe de luz color verde;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_jedis_nombre.listar_por_sable()

# g. listar todos los Jedi cuyos maestros están en el archivo;
print_seccion('g. listar todos los Jedi cuyos maestros están en el archivo;')

lista_nombres_jedis = ListaJedis()
for jedi in lista_jedis:
    lista_nombres_jedis.insert_value(jedi['nombre'])

print(f'{Color.AZUL}\nLista de Jedis en el archivo: {Color.RESET}')
lista_nombres_jedis.sort_by_criterion()
lista_nombres_jedis.show()

print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
arbol_jedis_nombre.listar_por_maestro(lista_nombres_jedis)

# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
print_seccion('h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_jedis_especie.mostrar_por_especie()

# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
print_seccion('i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_jedis_nombre.listar_por_coincidencia()

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')