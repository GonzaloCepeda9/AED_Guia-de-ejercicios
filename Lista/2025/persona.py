from list_ import List

class Persona:

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return (f'{self.apellido}, {self.nombre} - {self.dni}')

def order_by_name(item):
    return item.nombre

def order_by_surname(item):
    return item.apellido

def order_by_dni(item):
    return item.dni

personas = [
    Persona(nombre='Juana', apellido='Gonzalez', dni=45),
    Persona(nombre='Mariano', apellido='Perez', dni=32),
    Persona(nombre='Mariano', apellido='Perez', dni=51),
    Persona(nombre='Carlos', apellido='Romero', dni=14),
    Persona(nombre='Ana', apellido='Cordoba', dni=29),
]

lista_personas = List()

lista_personas.add_criterion('nombre', order_by_name)
lista_personas.add_criterion('apellido', order_by_surname)
lista_personas.add_criterion('dni', order_by_dni)

for persona in personas:
    lista_personas.append(persona)

# Pruebas de Listas

print()
print(lista_personas.search(45, 'dni'))
print()
lista_personas.show()
print()
print(f'Elemento eliminado: {lista_personas.delete_value(51, 'dni')}.')
print()
lista_personas.show()
print()
print(f'Elemento eliminado: {lista_personas.delete_value('Romero', 'apellido')}.')
print()
lista_personas.show()
print()
print(f'Elemento eliminado: {lista_personas.delete_value('Roberto', 'nombre')}.')
print()
lista_personas.sort_by_criterion()
print()
lista_personas.show()
print()