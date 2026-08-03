# Extra: Función de búsqueda binaria

numbers = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

print("--------- Función de búsqueda binaria recursiva ---------")

def busqueda_binaria_recursiva(array, valor_busc, primero = 0, ultimo = len(numbers)): 
    medio = (primero + ultimo) // 2
    if primero >= ultimo:
        return "El número no se encuentra en la lista."
    elif array[medio] == valor_busc:
        return f"El número se encuentra en la posición {medio}."
    else:
        if array[medio] > valor_busc:
            return busqueda_binaria_recursiva(array, valor_busc, primero, ultimo-1)
        else:
            return busqueda_binaria_recursiva(array, valor_busc, primero+1, ultimo)

print(busqueda_binaria_recursiva(numbers, 3))
print(busqueda_binaria_recursiva(numbers, 9))
print(busqueda_binaria_recursiva(numbers, 27))
print(busqueda_binaria_recursiva(numbers, 45))
print(busqueda_binaria_recursiva(numbers, 63))
print(busqueda_binaria_recursiva(numbers, 81))
print(busqueda_binaria_recursiva(numbers, 99))

print("--------- Función de búsqueda binaria iterativa ---------")

def busqueda_binaria_iterativa(array, valor_buscado):
    primero = 0
    ultimo = len(array) -1
    posicion = -1

    while (primero <= ultimo) and (posicion == -1):
        medio = (primero + ultimo) // 2 
        if array[medio] == valor_buscado:
            posicion = medio
        elif array[medio] > valor_buscado:
            ultimo = medio - 1
        else:
            primero = medio + 1
    if posicion == -1:
        return "El número no se encuentra en la lista."
    else:
        return f"El número {valor_buscado} se encuentra en la posición {posicion}."

print(busqueda_binaria_iterativa(numbers, 3))
print(busqueda_binaria_iterativa(numbers, 9))
print(busqueda_binaria_iterativa(numbers, 27))
print(busqueda_binaria_iterativa(numbers, 45))
print(busqueda_binaria_iterativa(numbers, 63))
print(busqueda_binaria_iterativa(numbers, 81))
print(busqueda_binaria_iterativa(numbers, 99))