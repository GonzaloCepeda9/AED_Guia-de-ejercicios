from typing import Any

class List(list):

    # El parámetro (list) significa que hereda los atributos y métodos de list.
    # La lista que existe en Python ya tiene varias funciones que nos sirven, por eso las reutilizamos, y modificamos o agregamos lo necesario para que funcione como queramos.

    def show(self, lista: list):
        for i in lista:
            print(i)

    def eliminar_valor(lista, clave):
        pass

    def insertar_valor(lista, valor):
        pass

    def sort(lista, valor):
        pass

def ordenar_por_nombre(item):
    return item.nombre

def ordenar_por_apellido(item):
    return item.apellido

def ordenar_por_dni(item):
    return item.dni

"""
list_number = List()

# INSERTAR (al final o en cualquier lugar)
list_number.append(3)
list_number.append(6)
list_number.append(9)
list_number.append(12)
list_number.insert(0, 0)

print(list_number)
list_number.show()

# ORDENAR (ordena alfabéticamente, pero no sirve para tipo de dato compuesto)
list_number.sort()

# ELIMINAR
list_number.pop()               
list_number.remove(0)

print(list_number)
deleted_value1 = list_number.pop(0)       # Sí retorna el valor. Error si está fuera del rango.
deleted_value2 = list_number.remove(6)    # No retorna el valor. Eerror si el elemento no existe.
print(list_number)

print(deleted_value1)
print(deleted_value2)

"""