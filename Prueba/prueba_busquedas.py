# BÚSQUEDA SECUENCIAL
def busqueda_secuencial(self, search_value):
    for index, element in enumerate(self): # Enumerate enumera cada elemento de la la lista. Index toma el valor numérico, y element toma el elemento que esté en la lista.
        if element.dni == search_value:
            return f'El elemento se encuentra en la posición {index}. \nApellido y nombre: {element.nombre}, {element.apellido} | DNI: {element.dni}'

# BÚSQUEDA BINARIA
def busqueda_binaria(self, search_value):
    start = 0
    end = len(self) -1
    middle = (start + end) // 2

    while start <= end:
        if middle == search_value:
            return middle
        elif middle < search_value:
            start = middle + 1
        elif middle > search_value:
            end = middle - 1   
        middle = (start + end) // 2

    return None