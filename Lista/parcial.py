class Parcial:
    def __init__(self, materia: str, nota: int, fecha: str):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return f'{self.materia}: {self.nota} | {self.fecha}'