from TDA_list import List

class Alumno:
    def __init__(self, nombre: str, apellido: str, legajo: int):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.parciales = List()

    def __str__(self):
        return f'{self.apellido}, {self.nombre} | {self.legajo}'