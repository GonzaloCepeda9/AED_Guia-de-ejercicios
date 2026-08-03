from TDA_list import List

class Person:

    def __init__(self, nombre: str, apellido: str, dni: int):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'{self.nombre}, {self.apellido} | {self.dni}. '