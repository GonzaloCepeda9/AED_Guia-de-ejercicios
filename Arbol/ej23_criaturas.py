# 23. Criaturas y Dioses
'''
Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.
'''

from TDA_tree import BinaryTree
from ej23_lista_criaturas import lista_criaturas

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

class BinaryTreeCriaturas(BinaryTree):

    # def in_order_completo(self):
    #     def __in_order_completo(root):
    #         if root is not None:
    #             __in_order_completo(root.left)
    #             print(f'  → {root.value} | {root.other_values}')
    #             __in_order_completo(root.right)

    #     if self.root is not None:
    #         __in_order_completo(self.root)


    # a. listado inorden de las criaturas y quienes la derrotaron;

    def listar_inorder(self):
        def __listar_inorder(root):
            if root is not None:
                __listar_inorder(root.left)
                print(f'  → Criatura: {root.value} | Derrotada por: {root.other_values['derrotado_por']}')
                __listar_inorder(root.right)

        if self.root is not None:
            __listar_inorder(self.root)

    # b. se debe permitir cargar una breve descripción sobre cada criatura;

        # Corregir. Dice permitir cargar. No cargar todas al inicio. 

    # c. mostrar toda la información de la criatura Talos;
    # d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
    # e. listar las criaturas derrotadas por Heracles;
    # f. listar las criaturas que no han sido derrotadas;
    # g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
    # h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
    # i. se debe permitir búsquedas por coincidencia;
    # j. eliminar al Basilisco y a las Sirenas;
    # k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
    # l. modifique el nombre de la criatura Ladón por Dragón Ladón;
    # m. realizar un listado por nivel del árbol;
    # n. muestre las criaturas capturadas por Heracles.

# --------- CARGA DE DATOS --------- #

arbol_criaturas = BinaryTreeCriaturas()

for criatura in lista_criaturas:
    datos = {
        "nombre": criatura['nombre'],
        "derrotado_por": criatura['derrotado_por'],
        "descripcion": criatura['descripcion'],
        "capturada_por": criatura['capturada_por']
    }

    datos_copy = datos.copy()
    datos_copy.pop('nombre')
    arbol_criaturas.insert(criatura['nombre'], datos_copy)

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
print(f'\n{Color.CIAN}{f' EJERCICIO 23: CRIATURAS Y DIOSES '.center(140, "=")}{Color.RESET}')

# a. listado inorden de las criaturas y quienes la derrotaron;
print_seccion('a. listado inorden de las criaturas y quienes la derrotaron;')
print(f'{Color.AZUL}Listado in_order:{Color.RESET}')
arbol_criaturas.listar_inorder()

# b. se debe permitir cargar una breve descripción sobre cada criatura;

# c. mostrar toda la información de la criatura Talos;
print_seccion('c. mostrar toda la información de la criatura Talos;')
criatura_buscada = 'Talos'
posicion = arbol_criaturas.search(criatura_buscada)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if posicion is not None:
    print(f'  → {posicion.value} | {posicion.other_values}')
else:
    print(f'  → {criatura_buscada} no se encuentra en el árbol.')

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print_seccion('d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;')


# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.


print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')