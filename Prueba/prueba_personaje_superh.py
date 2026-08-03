class Personaje:
    def __init__(self, nombre_personaje: int, nombre_superheroe: int, genero: str):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __str__(self):
        return f'Personaje: {self.nombre_personaje} | Superhéroe: {self.nombre_superheroe} | Género: {self.genero}'