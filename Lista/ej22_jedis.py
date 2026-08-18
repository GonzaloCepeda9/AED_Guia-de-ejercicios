"""
22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las actividades enumeradas a continuación:
a. listado ordenado por nombre y por especie;
b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
d. mostrar los Jedi de especie humana y twi'lek;
e. listar todos los Jedi que comienzan con A;
f. mostrar los Jedi que usaron sable de luz de más de un color;
g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
"""

from jedi import Jedi
from TDA_list import List

lista_jedis = List()

# --------- Carga de datos ---------

# Ahsoka Tano
maestros = List()
maestros.append("Anakin Skywalker")
sables = List()
sables.append("Verde")
sables.append("Azul")
sables.append("Blanco")
ahsoka = Jedi("Ahsoka Tano", "Togruta")
ahsoka.maestros = maestros
ahsoka.sables_usados = sables
lista_jedis.append(ahsoka)

# Kit Fisto
maestros = List()
sables = List()
sables.append("Verde")
kit = Jedi("Kit Fisto", "Nautolano")
kit.maestros = maestros
kit.sables_usados = sables
lista_jedis.append(kit)

# Yoda
maestros = List()
maestros.append("N'Kata Del Gormo")
sables = List()
sables.append("Verde")
yoda = Jedi("Yoda", "Desconocida")
yoda.maestros = maestros
yoda.sables_usados = sables
lista_jedis.append(yoda)

# Luke Skywalker
maestros = List()
maestros.append("Obi-Wan Kenobi")
maestros.append("Yoda")
sables = List()
sables.append("Azul")
sables.append("Verde")
luke = Jedi("Luke Skywalker", "Humana")
luke.maestros = maestros
luke.sables_usados = sables
lista_jedis.append(luke)

# Qui-Gon Jinn
maestros = List()
maestros.append("Conde Dooku")
sables = List()
sables.append("Verde")
qui_gon = Jedi("Qui-Gon Jinn", "Humana")
qui_gon.maestros = maestros
qui_gon.sables_usados = sables
lista_jedis.append(qui_gon)

# Mace Windu
maestros = List()
sables = List()
sables.append("Violeta")
mace = Jedi("Mace Windu", "Humana")
mace.maestros = maestros
mace.sables_usados = sables
lista_jedis.append(mace)

# Aayla Secura
maestros = List()
maestros.append("Quinlan Vos")
sables = List()
sables.append("Azul")
aayla = Jedi("Aayla Secura", "Twi'lek")
aayla.maestros = maestros
aayla.sables_usados = sables
lista_jedis.append(aayla)

# Quinlan Vos
maestros = List()
maestros.append("Tholme")
sables = List()
sables.append("Verde")
sables.append("Azul")
quinlan = Jedi("Quinlan Vos", "Kiffar")
quinlan.maestros = maestros
quinlan.sables_usados = sables
lista_jedis.append(quinlan)

# Cal Kestis
maestros = List()
maestros.append("Jaro Tapal")
sables = List()
sables.append("Azul")
sables.append("Naranja")
sables.append("Verde")
cal = Jedi("Cal Kestis", "Humana")
cal.maestros = maestros
cal.sables_usados = sables
lista_jedis.append(cal)

# Satele Shan
maestros = List()
maestros.append("Bran")
maestros.append("Kao Cen Darach")
sables = List()
sables.append("Azul")
sables.append("Verde")
sables.append("Amarillo")
satele = Jedi("Satele Shan", "Humana")
satele.maestros = maestros
satele.sables_usados = sables
lista_jedis.append(satele)

# Ben Solo
maestros = List()
maestros.append("Luke Skywalker")
sables = List()
sables.append("Azul")
ben = Jedi("Ben Solo", "Humana")
ben.maestros = maestros
ben.sables_usados = sables
lista_jedis.append(ben)

# Grogu
maestros = List()
maestros.append("Luke Skywalker")
sables = List()
grogu = Jedi("Grogu", "Desconocida")
grogu.maestros = maestros
grogu.sables_usados = sables
lista_jedis.append(grogu)

# Leia Organa
maestros = List()
maestros.append("Luke Skywalker")
sables = List()
sables.append("Azul")
leia = Jedi("Leia Organa", "Humana")
leia.maestros = maestros
leia.sables_usados = sables
lista_jedis.append(leia)

# Agen Kolar
maestros = List()
sables = List()
sables.append("Azul")
agen = Jedi("Agen Kolar", "Zabrak")
agen.maestros = maestros
agen.sables_usados = sables
lista_jedis.append(agen)

# Adi Gallia
maestros = List()
sables = List()
sables.append("Azul")
adi = Jedi("Adi Gallia", "Tholothiana")
adi.maestros = maestros
adi.sables_usados = sables
lista_jedis.append(adi)

# Creación de funciones para ordenar por criterio
def order_by_name(jedi):
    return jedi.nombre

def order_by_species(jedi):
    return jedi.especie

# Agregación de criterios de búsqueda
lista_jedis.add_criterion('nombre', order_by_name)
lista_jedis.add_criterion('especie', order_by_species)

#################################################  Ejecución de pruebas del enunciado  #################################################
print(f'\nLista original de Jedis: ')
lista_jedis.show()

# a. listado ordenado por nombre y por especie;
print('\n---------------------------------------------- a. Listado ordenado por criterio ----------------------------------------------')
criterio = 'nombre'
print(f'Listado ordenado por "{criterio}": ')
lista_jedis.sort_by_criterion(criterio)
lista_jedis.show()

criterio = 'especie'
print(f'\nListado ordenado por "{criterio}": ')
lista_jedis.sort_by_criterion(criterio)
lista_jedis.show()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
print('\n--------------------------------------- b. Muestreo de información de Jedi específico ----------------------------------------')
buscado = 'Ahsoka Tano'
encontrado = False
for jedi in lista_jedis:
    if jedi.nombre == buscado:
        encontrado = True
        jedi_buscado = jedi
        break

if encontrado:
    print(f'Información de "{buscado}": ')
    print(jedi_buscado)
else:
    print(f'El Jedi "{buscado}" no se encuentra en la lista.')

buscado = 'Kit Fisto'
encontrado = False
for jedi in lista_jedis:
    if jedi.nombre == buscado:
        encontrado = True
        jedi_buscado = jedi
        break

if encontrado:
    print(f'\nInformación de "{buscado}": ')
    print(jedi_buscado)
else:
    print(f'El Jedi "{buscado}" no se encuentra en la lista.')

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print('\n---------------------------------- c. Muestreo de padawans (aprendices) de Jedi específico -----------------------------------')
maestro = 'Yoda'
lista_aprendices = List()
for jedi in lista_jedis:
    if maestro in jedi.maestros:
        lista_aprendices.append(jedi.nombre)

if lista_aprendices:
    print(f'Aprendices de "{maestro}": ')
    lista_aprendices.show()
else:
    print(f'No se encontraron aprendices de {maestro}.')

maestro = 'Luke Skywalker'
lista_aprendices = List()
for jedi in lista_jedis:
    if maestro in jedi.maestros:
        lista_aprendices.append(jedi.nombre)

if lista_aprendices:
    print(f'\nAprendices de "{maestro}": ')
    lista_aprendices.show()
else:
    print(f'\nNo se encontraron aprendices de {maestro}.')

# d. mostrar los Jedi de especie Humana y Twi'lek;
print('\n------------------------------------------- d. Muestreo de Jedis según su especie --------------------------------------------')
especie = "Humana"
lista_por_especie = List()
for jedi in lista_jedis:
    if jedi.especie.upper() == especie.upper():
        lista_por_especie.append(jedi)

if lista_por_especie:
    print(f'Jedis de especie {especie}: ')
    lista_por_especie.show()
else:
    print(f'No se encontraron Jedis de especie {especie}')

especie = "Twi'Lek"
lista_por_especie = List()
for jedi in lista_jedis:
    if jedi.especie.upper() == especie.upper():
        lista_por_especie.append(jedi)

if lista_por_especie:
    print(f'\nJedis de especie {especie}: ')
    lista_por_especie.show()
else:
    print(f'No se encontraron Jedis de especie {especie}')

# e. listar todos los Jedi que comienzan con A;
print('\n---------------------------------------------- e. Listado de Jedis por inicial -----------------------------------------------')
inicial = 'A'
lista_por_inicial = List()
for jedi in lista_jedis:
    if jedi.nombre.startswith(inicial):
        lista_por_inicial.append(jedi)

if lista_por_inicial:
    print(f'Listado de Jedis que comienzan con {inicial}: ')
    lista_por_inicial.show()
else:
    print(f'No se encontró ningún Jedi cuyo nombre comience con "{inicial}".')

# f. mostrar los Jedi que usaron sable de luz de más de un color;
print('\n------------------------------------ f. Muestreo de Jedis según cantidad de sables usados ------------------------------------')
cantidad = 1
lista_por_sables = List()
for jedi in lista_jedis:
    if jedi.sables_usados.size() > cantidad:
        lista_por_sables.append(jedi)

if lista_por_sables:
    print(f'Listado de Jedis que usaron más de {cantidad} sable/s: ')
    lista_por_sables.show()
else:
    print(f'No se encontraron Jedis que hayan usado más de {cantidad} sable/s.')

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print('\n------------------------------------- g. Indicación de Jedis según color de sable usado --------------------------------------')
color1 = 'Amarillo'
color2 = 'Violeta'
for jedi in lista_jedis:
    if color1 in jedi.sables_usados or color2 in jedi.sables_usados:
        print(f'{jedi.nombre} utilizó sable de luz {color1} o {color2}.')

# h. indicar los nombre de los padawans de Qui-Gon Jinn y Mace Windu, si los tuvieron.
print('\n---------------------------------------- h. Indicación de padawans de Jedi específico ----------------------------------------')
maestro = 'Qui-Gon Jinn'
lista_padawans = List()
for jedi in lista_jedis:
    if maestro in jedi.maestros:
        lista_padawans.append(jedi.nombre)

if lista_padawans:
    print(f'Padawans del maestro {maestro}: ')
    lista_padawans.show()
else:
    print(f'El maestro {maestro} no tuvo padawans.')

maestro = 'Mace Windu'
lista_padawans = List()
for jedi in lista_jedis:
    if maestro in jedi.maestros:
        lista_padawans.append(jedi.nombre)

if lista_padawans:
    print(f'\nPadawans del maestro {maestro}: ')
    lista_padawans.show()
else:
    print(f'\nEl maestro {maestro} no tuvo padawans.')