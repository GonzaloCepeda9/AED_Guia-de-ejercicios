##################################################  Ejecución de pruebas de listas   ###################################################

from TDA_list import List
from person import Person

def order_by_name(elemento):
    return elemento.nombre

def order_by_surname(elemento):
    return elemento.apellido

def order_by_dni(elemento):
    return elemento.dni

list_people = List()

people = [
    Person(nombre='Jennifer', apellido='Lawrence', dni=5678),
    Person(nombre='Martín', apellido='Palermo', dni=2345),
    Person(nombre='Sergio', apellido='Martínez', dni=3456),
    Person(nombre='Carlos', apellido='Solari', dni=1234),
    Person(nombre='Scarlett', apellido='Johansson', dni=6789),
    Person(nombre='Gustavo', apellido='Nápoli', dni=4567)
]

for person in people:
    list_people.insert_value(person)

list_people.add_criterion('nombre', order_by_name)
list_people.add_criterion('apellido', order_by_surname)
list_people.add_criterion('dni', order_by_dni)

print(f'\nLista original: ')
list_people.show()
list_people.insert_value(Person(nombre='Emiliano', apellido='Martínez', dni=7890))

print(f'\nLista actualizada: ')
list_people.show()
print()

position = list_people.search('dni', 4567)
print(f'\nLista ordenada por criterio: ')
list_people.show()
if position:
    print(f'\nEl elemento se encuentra en la posición {position}.')
else:
    print(f'\nEl elemento no se encuentra en la lista.')

list_people.sort_by_criterion('nombre')
print(f'\nLista ordenada por nombre: ')
list_people.show()

list_people.sort_by_criterion('apellido')
print(f'\nLista ordenada por apellido: ')
list_people.show()

list_people.sort_by_criterion('dni')
print(f'\nLista ordenada por DNI: ')
list_people.show()

print(f'\nLista original: ')
list_people.show()

list_people.sort_by_criterion('apellido')
print(f'\nLista ordenada por apellido: ')
list_people.show()

print(f'\nPersona a eliminar:')
print(list_people.delete_value('apellido', 'Nápoli'))
print(f'\nLista actualizada:')
list_people.show()