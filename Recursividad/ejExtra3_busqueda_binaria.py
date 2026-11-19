from typing import Any

# Extra: Implementar una función de búsqueda que devuelva la posición de un número en una lista.

# Búsqueda binaria recursiva
def busqueda_binaria_recursiva(array, valor_busc, primero = 0, ultimo = None) -> int: 
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

# Búsqueda binaria iterativa
def busqueda_binaria_iterativa(array: list, valor_buscado: Any) -> int:
    primero = 0
    ultimo = len(array) -1
    posicion = -1
    while primero <= ultimo and posicion == -1:
        medio = (primero + ultimo) // 2 
        if array[medio] == valor_buscado:
            posicion = medio
        elif array[medio] > valor_buscado:
            ultimo = medio - 1
        else:
            primero = medio + 1
    if posicion == -1:
        return None
    else:
        return medio

# --------- Carga de datos ---------
numbers = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n----------------------------- Búsqueda binaria recursiva de un número entero dentro de una lista -----------------------------')
buscado = 0
posicion = busqueda_binaria_recursiva(numbers, buscado)
print(f'Búsqueda binaria recursiva:')
if posicion is not None:
    print(f'El número {buscado} se encuentra en la posición {posicion}.')
else:
    print(f'El número {buscado} no se encuentra en la lista.')

print('\n----------------------------- Búsqueda binaria iterativa de un número entero dentro de una lista -----------------------------')
buscado = 18
posicion = busqueda_binaria_iterativa(numbers, buscado)
print(f'\nBúsqueda binaria iterativa:')
if posicion:
    print(f'El número {buscado} se encuentra en la posición {posicion}.')
else:
    print(f'El número {buscado} no se encuentra en la lista.')