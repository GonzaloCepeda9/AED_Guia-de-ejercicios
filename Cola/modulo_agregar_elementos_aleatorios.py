from TDA_queue import Queue
from TDA_stack import Stack
from random import randint

def agregar_mayusculas(estructura: Stack | Queue):
    cantidad = int(input('Ingrese la cantidad de letras mayúsculas aleatorias que desea agregar a la estructura: '))
    if cantidad < 1:
        return None
    else:
        for _ in range(cantidad):
            letter = chr(randint(65, 90))
            if isinstance(estructura, Queue):
                estructura.arrive(letter)
            elif isinstance(estructura, Stack):
                estructura.push(letter)
    return estructura

def agregar_minusculas(estructura: Stack | Queue):
    cantidad = int(input('Ingrese la cantidad de letras minúsculas aleatorias que desea agregar a la estructura: '))
    if cantidad < 1:
        return None
    else:
        for _ in range(cantidad):
            letter = chr(randint(97, 122))
            if isinstance(estructura, Queue):
                estructura.arrive(letter)
            elif isinstance(estructura, Stack):
                estructura.push(letter)
    return estructura

def agregar_numeros(estructura: Stack | Queue):
    cantidad = int(input('Ingrese la cantidad de números aleatorios que desea agregar a la estructura: '))
    menor = int(input('Ingrese el menor número permitido (inclusive): '))
    mayor = int(input('Ingrese el mayor número permitido (inclusive): '))
    if cantidad < 1:
        return None
    else:
        for _ in range(cantidad):
            numero = randint(menor, mayor)
            if isinstance(estructura, Queue):
                estructura.arrive(numero)
            elif isinstance(estructura, Stack):
                estructura.push(numero)
    return estructura