# 24. Peronajes de Marvel Cinematic Universe (MCU)
"""
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
    a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
    b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
    c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    d. mostrar todos los personajes cuyos nombre empiezan con C, D y G
"""

from TDA_stack import Stack
from personaje import Personaje

pila_personajes = Stack()

pila_personajes.push(Personaje("Iron Man", 10))
pila_personajes.push(Personaje("Captain America (Capitán América)", 11))
pila_personajes.push(Personaje("Thor", 8))
pila_personajes.push(Personaje("Black Widow (Viuda Negra)", 9))
pila_personajes.push(Personaje("Hawkeye (Ojo de Halcón)", 6))
pila_personajes.push(Personaje("Hulk", 8))
pila_personajes.push(Personaje("Nick Fury (Nick Furia)", 11))
pila_personajes.push(Personaje("Loki", 6))
pila_personajes.push(Personaje("Spider-Man", 7))
pila_personajes.push(Personaje("Doctor Strange", 5))
pila_personajes.push(Personaje("Black Panther (Pantera Negra)", 5))
pila_personajes.push(Personaje("Ant-Man (Hombre Hormiga)", 5))
pila_personajes.push(Personaje("Scarlet Witch (Bruja Escarlata)", 7))
pila_personajes.push(Personaje("Falcon (Halcón)", 7))
pila_personajes.push(Personaje("Groot", 5))
pila_personajes.push(Personaje("Winter Soldier (Soldado del Invierno)", 7))
pila_personajes.push(Personaje("War Machine (Máquina de Guerra)", 7))
pila_personajes.push(Personaje("Captain Marvel (Capitana Marvel)", 4))
pila_personajes.push(Personaje("Gamora", 5))
pila_personajes.push(Personaje("Rocket Raccoon", 5))
pila_personajes.push(Personaje("Thanos", 8))

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

def determinar_posicion(stack: Stack, personaje: str):

    stack_aux = Stack()
    posicion = None

    for i in range(stack.size()):
        personaje_cima = stack.pop()
        stack_aux.push(personaje_cima)

        if personaje_cima.nombre == personaje:
            posicion = i+1

    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return posicion

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;

def determinar_participacion(stack: Stack, cantidad_peliculas: int):

    stack_aux = Stack()
    personajes_participacion = Stack()

    while stack.size() > 0:
        personaje_cima = stack.pop()
        stack_aux.push(personaje_cima)
        if personaje_cima.cantidad_peliculas > cantidad_peliculas:
            personajes_participacion.push(personaje_cima)

    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return personajes_participacion

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

def determinar_cantidad_peliculas(stack: Stack, personaje: str):

    stack_aux = Stack()
    cantidad_peliculas = None
    
    while stack.size() > 0:    
        personaje_cima = stack.pop()
        stack_aux.push(personaje_cima)

        if personaje_cima.nombre == personaje:
            cantidad_peliculas = personaje_cima.cantidad_peliculas
    
    while stack_aux.size():
        stack.push(stack_aux.pop())

    return cantidad_peliculas

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G

def mostrar_por_inicial(stack: Stack, inicial: chr):
    
    stack_aux = Stack()
    personajes_buscados = Stack()

    while stack.size() > 0:
        personaje_cima = stack.pop()
        stack_aux.push(personaje_cima)
        
        if personaje_cima.nombre[0] == inicial:
            personajes_buscados.push(personaje_cima)
    
    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return personajes_buscados

################################################ // Ejecución de pruebas del enunciado // ################################################

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
print('\n--------------------------------------- a. Determinación de la posición del personaje ----------------------------------------')

personaje1 = 'Rocket Raccoon'
posicion1 = determinar_posicion(pila_personajes, personaje1)
if posicion1 is not None:
    print(f'El personaje "{personaje1}" se encuentra en la posición {posicion1}.')
else:
    print(f'El personaje "{personaje1}" no se encuentra en la pila.')

personaje2 = 'Groot'
posicion2 = determinar_posicion(pila_personajes, personaje2)
if posicion2 is not None:
    print(f'El personaje "{personaje2}" se encuentra en la posición {posicion2}.')
else:
    print(f'El personaje "{personaje2}" no se encuentra en la pila.')

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
print('\n----------------------------------- b. Determinación de la participación de los personajes -----------------------------------')
participacion = 5
personajes_participacion = determinar_participacion(pila_personajes, participacion)

if participacion < 0:
    print('\nDebe ingresar una cantidad válida de películas.')
else:
    if not personajes_participacion.is_empty():
        print(f'Los personajes que participaron en más de {participacion} películas son: ')
        personajes_participacion.show()
    else:
        print(f'Ningún personaje a participado en más de {participacion} películas.')

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
print('\n-------------------------- c. Determinación cantidad de películas en las que participó el personaje --------------------------')

personaje = 'Black Widow (Viuda Negra)'
cantidad_peliculas = determinar_cantidad_peliculas(pila_personajes, personaje)

if cantidad_peliculas is not None:
    print(f'El personaje {personaje} participó en {cantidad_peliculas} película/s.')
else:
    print(f'El personaje {personaje} no participó en ninguna película.')

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G
print('\n------------------------------------ d. Muestra de los personajes por inicial específica -------------------------------------')
inicial1 = 'C'
personajes_buscados1 = mostrar_por_inicial(pila_personajes, inicial1)
if not personajes_buscados1.is_empty():
    print(f'Los personajes cuyo nombre empiezan con la letra "{inicial1}" son: ')
    personajes_buscados1.show()
else:
    print(f'No se encontró ningún personaje cuyo nombre comience con la letra "{inicial1}"')

inicial2 = 'D'
personajes_buscados2 = mostrar_por_inicial(pila_personajes, inicial2)
if not personajes_buscados2.is_empty():
    print(f'Los personajes cuyo nombre empiezan con la letra "{inicial2}" son: ')
    personajes_buscados2.show()
else:
    print(f'No se encontró ningún personaje cuyo nombre comience con la letra "{inicial2}"')

inicial3 = 'G'
personajes_buscados3 = mostrar_por_inicial(pila_personajes, inicial3)
if not personajes_buscados3.is_empty():
    print(f'Los personajes cuyo nombre empiezan con la letra "{inicial3}" son: ')
    personajes_buscados3.show()
else:
    print(f'No se encontró ningún personaje cuyo nombre comience con la letra "{inicial3}"')