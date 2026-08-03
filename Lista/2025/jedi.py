from list_ import List

def ordenar_por_nombre(item):
    return item.nombre

def ordenar_por_especie(item):
    return item.especie

class Jedi:
    
    def __init__(self, nombre: str, maestros: List, sables: List, especie: str):
        self.nombre = nombre
        self.maestros = maestros
        self.sables = sables
        self.especie = especie
        self.maestros.add_criterion('nombre', ordenar_por_nombre)
        self.maestros.add_criterion('especie', ordenar_por_especie)

    def __str__(self):
        return f'Nombre: {self.nombre} | Maestros: {self.maestros} | Sables de luz usados: {self.sables} | Especie: {self.especie}'

# En caso de que maestro o sable no sea un dato simple:
# class Maestro:
#     def __init__(self, nombre_maestro: str):
#         self.nombre_maestro = nombre_maestro
#     def __str__(self):
#         return f'{self.nombre_maestro}'
   
# class Sable:
#     def __init__(self, color_sable: str):
#         self.color_sable = color_sable
#     def __str__(self):
#         return f'{self.color_sable}'

lista_de_jedis = List()

# Ahsoka Tano
maestros = List()
maestros.append("Anakin Skywalker")
sables = List()
sables.append("Verde")
sables.append("Azul")
sables.append("Blanco")
lista_de_jedis.append(Jedi("Ashoka Tano", maestros, sables, "Togruta"))

# Kit Fisto
maestros = List()
sables = List()
sables.append("Verde")
lista_de_jedis.append(Jedi("Kit Fisto", maestros, sables, "Nautolano"))

# Yoda
maestros = List()
maestros.append("N'Kata Del Gormo")
sables = List()
sables.append("Verde")
lista_de_jedis.append(Jedi("Yoda", maestros, sables, "Desconocida"))

# Luke Skywalker
maestros = List()
maestros.append("Obi-Wan Kenobi")
maestros.append("Yoda")
sables = List()
sables.append("Azul")
sables.append("Verde")
lista_de_jedis.append(Jedi("Luke Skywalker", maestros, sables, "Humana"))

# Qui-Gon Jinn
maestros = List()
maestros.append("Conde Dooku")
sables = List()
sables.append("Verde")
lista_de_jedis.append(Jedi("Qui-Gon", maestros, sables, "Humana"))

# Mace Windu
maestros = List()
sables = List()
sables.append("Violeta")
lista_de_jedis.append(Jedi("Mace Windu", maestros, sables, "Humana"))

# Aayla Secura
maestros = List()
maestros.append("Quinlan Vos")
sables = List()
sables.append("Azul")
lista_de_jedis.append(Jedi("Aayla Secura", maestros, sables, "Twi'lek"))

# Quinlan Vos
maestros = List()
maestros.append("Tholme")
sables = List()
sables.append("Verde")
sables.append("Azul")
lista_de_jedis.append(Jedi("Quinlan Vos", maestros, sables, "Kiffar"))

# Cal Kestis
maestros = List()
maestros.append("Jaro Tapal")
sables = List()
sables.append("Azul")
sables.append("Naranja")
sables.append("Verde")
lista_de_jedis.append(Jedi("Cal Kestis", maestros, sables, "Humana"))

# Satele Shan
maestros = List()
maestros.append("Bran")
maestros.append("Kao Cen Darach")
sables = List()
sables.append("Azul")
sables.append("Verde")
sables.append("Amarillo")
lista_de_jedis.append(Jedi("Satele Shan", maestros, sables, "Humana"))

# Ben Solo
maestros = List()
maestros.append("Luke Skywalker")
sables = List()
sables.append("Azul")
lista_de_jedis.append(Jedi("Ben Solo", maestros, sables, "Humana"))

# Grogu
maestros = List()
maestros.append("Luke Skywalker")
sables = List()
lista_de_jedis.append(Jedi("Grogu", maestros, sables, "Desconocida"))

# Leia Organa
maestros = List()
maestros.append("Luke Skywalker")
sables = List()
sables.append("Azul")
lista_de_jedis.append(Jedi("Leia Organa", maestros, sables, "Humana"))

# Agen Kolar
maestros = List()
sables = List()
sables.append("Azul")
lista_de_jedis.append(Jedi("Agen Kolar", maestros, sables, "Zabraka"))

# Adi Gallia
maestros = List()
sables = List()
sables.append("Azul")
lista_de_jedis.append(Jedi("Adi Gallia", maestros, sables, "Tholothiana"))