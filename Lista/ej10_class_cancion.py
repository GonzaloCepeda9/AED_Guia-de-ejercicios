class Cancion:
    def __init__(
        self,
        nombre: str,
        banda: str,
        duracion: int,
        reproducciones: int
    ):
        self.nombre = nombre
        self.banda = banda
        self.duracion = duracion
        self.reproducciones = reproducciones

    def __str__(self):
        return f'{self.nombre} - {self.banda} | Duración: {self.duracion} s | Reproducciones último mes: {self.reproducciones}'