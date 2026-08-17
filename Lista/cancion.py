'''
10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista, duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que permita realizar las siguientes actividades:
a. obtener la información de la canción más larga;
b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
c. obtener todas las canciones de la banda Arctic Monkeys;
d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
'''

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