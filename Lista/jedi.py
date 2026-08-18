from TDA_list import List

class Jedi:
    def __init__(self, nombre: str, especie: str):
        self.nombre = nombre
        self.especie = especie
        self.maestros = List()
        self.sables_usados = List()

    def __str__(self):
        return f'\nNombre: {self.nombre} \nEspecie: {self.especie} \nMaestros: {self.maestros} \nSables usados: {self.sables_usados}'