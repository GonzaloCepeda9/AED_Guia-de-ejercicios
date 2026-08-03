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

from list_ import List
from jedi import Jedi, lista_de_jedis

lista_jedis = lista_de_jedis

# a. listado ordenado por nombre y por especie;
print('\n------------------------------------------------- Listado ordenado por nombre ------------------------------------------------')
lista_jedis.sort_by_criterion('nombre')
lista_jedis.show()

print('\n------------------------------------------------ Listado ordenado por especie ------------------------------------------------')
lista_jedis.sort_by_criterion('especie')
lista_jedis.show()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
print('\n--------------------------------------- Información completa de los Jedis solicitados ----------------------------------------')
buscado1 = 'Ashoka Tano'
buscado2 = 'Kit Fisto'
posicion1 = lista_jedis.search(buscado1, 'nombre')
posicion2 = lista_jedis.search(buscado2, 'nombre')
if posicion1:
    print(lista_jedis[posicion1])
else:
    print(f'El personaje {posicion1} no se encuentra en la lista.')

if posicion2:
    print(lista_jedis[posicion2])
else:
    print(f'El personaje {posicion2} no se encuentra en la lista.')

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print('\n--------------------------------------------- Padawans de Yoda y Luke Skywalker ----------------------------------------------')
list_aux = List()
for jedi in lista_jedis:
    for maestro in jedi.maestros:
        if maestro == 'Yoda' or maestro == 'Luke Skywalker':
            print(f'{jedi.nombre} es padawan de {maestro}')

# d. mostrar los Jedi de especie humana y twi'lek;
print('\n--------------------------------------------- Jedis de especie humana y Twi\'lek ---------------------------------------------')
for jedi in lista_jedis:
    if jedi.especie == 'Humana' or jedi.especie == 'Twi\'lek':
        print(f'{jedi.nombre} | {jedi.especie}')

# e. listar todos los Jedi que comienzan con A;
print('\n--------------------------------------------- Jedis cuyos nombres comienzan con A --------------------------------------------')
for jedi in lista_jedis:
    if jedi.nombre.startswith(('A')):
        print(jedi.nombre)

# f. mostrar los Jedi que usaron sable de luz de más de un color;
print('\n-------------------------------------- Jedis que usaron sable de luz de más de un color --------------------------------------')
for jedi in lista_jedis:
    if len(jedi.sables) > 1:
        print(f'{jedi.nombre} usó {len(jedi.sables)} sables de luz de distinto color.')

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print('\n-------------------------------------- Jedis que usaron sable de luz amarillo o violeta --------------------------------------')
for jedi in lista_jedis:
    color1 = 'Amarillo'
    color2 = 'Violeta'
    bool_color1 = False
    bool_color2 = False
    for sable in jedi.sables:
        if sable == color1:
            bool_color1 = True
        if sable == color2:
            bool_color2 = True
    if bool_color1 and bool_color2:
        print(f'{jedi.nombre} usó sables de luz {color1} y {color2}.')
    elif bool_color1:
        print(f'{jedi.nombre} usó sable de luz {color1}.')
    elif bool_color2:
        print(f'{jedi.nombre} usó sable de luz {color2}.')

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print('\n---------------------------------------------- Padawans de Qui-Gon y Mace Windu ----------------------------------------------')
padawans_maestro1 = List()
padawans_maestro2 = List()
maestro1 = 'Qui-Gon'
maestro2 = 'Mace Windu'
for jedi in lista_jedis:
    for maestro in jedi.maestros:
        if maestro == maestro1:
            padawans_maestro1.append(jedi.nombre)
        if maestro == maestro2:
            padawans_maestro2.append(jedi.nombre)

if padawans_maestro1:
    print(f'El maestro {maestro1} tuvo como padawan/s a: ')
    padawans_maestro1.show()
else:
    print(f'El maestro {maestro1} no tuvo ningún padawan.')

if padawans_maestro2:
    print(f'El maestro {maestro2} tuvo como padawan/s a: ')
    padawans_maestro2.show()
else:
    print(f'El maestro {maestro2} no tuvo ningún padawan.')
print()