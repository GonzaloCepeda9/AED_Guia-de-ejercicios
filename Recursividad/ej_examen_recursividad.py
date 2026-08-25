# Ejercicio de recursividad tipo parcial:
'''
Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
    a. funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
    b. funcion recursiva para listar los superheroes de la lista.
'''

# • funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
def busqueda_binaria_recursiva(array: list, valor_busc: str, primero = 0, ultimo = None) -> int: 
    if ultimo is None:
        ultimo = len(array) - 1
    medio = (primero + ultimo) // 2
    if primero > ultimo:
        return None
    elif array[medio] == valor_busc:
        return medio
    else:
        if array[medio] > valor_busc:
            return busqueda_binaria_recursiva(array, valor_busc, primero, medio-1)
        else:
            return busqueda_binaria_recursiva(array, valor_busc, medio+1, ultimo)

# • funcion recursiva para listar los superheroes de la lista.
def listar_superheroes(lista: list, indice: int = 0) -> None:
    if indice == len(lista):
        return
    else:
        print(f'#{indice+1} {lista[indice]}')
        return listar_superheroes(lista, indice + 1)

# --------- Carga de datos ---------
lista_superheroes = [
    "Iron Man",
    "Capitan America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Scarlet Witch",
    "Vision",
    "Ant-Man",
    "Wasp",
    "Star-Lord",
    "Captain Marvel"
]

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n--------------------------------------------- Listado de superhéroes de la lista ---------------------------------------------')
# • funcion recursiva para listar los superheroes de la lista.
print(f'Lista original de superhéroes: ')
listar_superheroes(lista_superheroes)

# • funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
print('\n--------------------------------------- Búsqueda de un superhéroe dentro de una lista ----------------------------------------')
lista_superheroes.sort()
for i in range (len(lista_superheroes)):
    print(f'Superhéroe en posición {i}: {lista_superheroes[i]}')
buscado = 'Capitan America'
posicion = busqueda_binaria_recursiva(lista_superheroes, buscado)
if posicion is not None:
    print(f'\nEl superhéroe "{buscado}" se encuentra en la posición {posicion}.')
else:
    print(f'\nEl superhéroe "{buscado}" no se encuentra en la lista.')