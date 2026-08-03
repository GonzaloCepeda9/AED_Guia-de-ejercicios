# Ordenar una pila de menor a mayor.
'''
◘ Algoritmo para resolver el problema
    Cada número que va ingresando, se va comparando con el que está en la Pila original.
    Si el número que va a ingresar es menor que el que está en la pila original, pusheo el número de la pila original a una pila auxiliar, y vuelvo a comparar con el nuevo número que quedó en la cima.
    Si el número que va a ingresar es mayor que el que está en la pila original, pusheo el número a la misma.
'''

# 8. Mazo de cartas.
'''
Dada una pila de cartas de las cuales se conoce su número y palo, (que representa un mazo de
cartas de baraja española), resolver las siguientes actividades:
    a. generar las cartas del mazo de forma aleatoria;
    b. separar la pila mazo en cuatro pilas una por cada palo;
    c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
'''

from TDA_stack import Stack
from random import randint

pila_mazo = Stack()
pila_aux = Stack()

while pila_mazo.size() < 4:
    carta_nueva = randint(1, 4)
    print(f'Nueva carta: {carta_nueva}')
    # while pila_mazo.size() > 0:
    
    if not pila_mazo.is_empty():
        pila_mazo.push(carta_nueva)
    else:
        carta_cima = pila_mazo.pop()
        if carta_nueva != carta_cima:
            pila_mazo.push(carta_nueva)
        else:
            pila_aux.push(carta_cima)

    while pila_aux.size() > 0:
        pila_mazo.push(pila_aux.pop())

pila_mazo.show()