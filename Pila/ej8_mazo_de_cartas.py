# 8. Mazo de cartas de baraja española 
'''
Dada una pila de cartas de las cuales se conoce su número y palo (que representa un mazo de cartas de baraja española), resolver las siguientes actividades:
    a. generar las cartas del mazo de forma aleatoria;
    b. separar la pila mazo en cuatro pilas una por cada palo;
    c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
'''

from TDA_stack import Stack
import random

# b. separar la pila mazo en cuatro pilas una por cada palo;
def separar_cartas(stack: Stack, palo: str):
    stack_aux = Stack()
    stack_palo = Stack()
    for i in range(stack.size()):
        carta_cima = stack.on_top()
        if palo in carta_cima:
            stack_palo.push(carta_cima)
            stack.pop()
        else:
            stack_aux.push(carta_cima)
            stack.pop()
    while not stack_aux.is_empty():
        stack.push(stack_aux.pop())
    return stack, stack_palo

# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
def ordenar_palo(stack: Stack):
    stack_aux = Stack()
    stack_order = Stack()
    while stack.size() > 0:
        carta_cima = stack.on_top()
        numero_cima = carta_cima.split()[0]
        numero_cima = int(numero_cima)
        if stack_order.is_empty():
            stack_order.push(carta_cima)
            stack.pop()
        else:
            while stack_order.size() > 0:
                carta_ordenada = False
                carta_cima_order = stack_order.on_top()
                numero_cima_order = carta_cima_order.split()[0]
                numero_cima_order = int(numero_cima_order)

                if numero_cima > numero_cima_order:
                    stack_aux.push(carta_cima)
                    carta_ordenada = True
                    while stack_order.size() > 0:
                        stack_aux.push(stack_order.pop())               
                else:
                    stack_aux.push(carta_cima_order)
                    stack_order.pop()
            if carta_ordenada == False:
                stack_aux.push(carta_cima)
            while stack_aux.size() > 0:
                stack_order.push(stack_aux.pop()) 
            stack.pop()
    
    return stack_order

#################################################  Ejecución de pruebas del enunciado  #################################################
# a. generar las cartas del mazo de forma aleatoria;
print('\n--------------------------------------------- Generación de las cartas del mazo ----------------------------------------------')
cartas = []
palos = ['Oro', 'Copa', 'Espada', 'Basto']

for palo in palos:
    for num in range(1, 13):
        cartas.append(f'{num} {palo}')

random.shuffle(cartas)

pila_mazo = Stack()
for carta in cartas:
    pila_mazo.push(carta)

print(f'Lista mazo: ')
print(cartas)
print(f'\nCantidad de cartas en el mazo: {len(cartas)}')

print(f'\nPila mazo ({pila_mazo.size()} cartas): ')
pila_mazo.show()

# b. separar la pila mazo en cuatro pilas una por cada palo;
print('\n--------------------------------------------- Separación de cartas por cada palo ---------------------------------------------')
palo1 = 'Oro'
pila_palo1 = Stack()
pila_mazo, pila_palo1 = separar_cartas(pila_mazo, palo1)
print(f'Pila con cartas de {palo1}: ')
pila_palo1.show()
print(f'\nPila mazo actualizada ({pila_mazo.size()} cartas): ')
pila_mazo.show()

palo2 = 'Copa'
pila_palo2 = Stack()
pila_mazo, pila_palo2 = separar_cartas(pila_mazo, palo2)
print(f'\nPila con cartas de {palo2}: ')
pila_palo2.show()
print(f'\nPila mazo actualizada ({pila_mazo.size()} cartas): ')
pila_mazo.show()

palo3 = 'Espada'
pila_palo3 = Stack()
pila_mazo, pila_palo3 = separar_cartas(pila_mazo, palo3)
print(f'\nPila con cartas de {palo3}: ')
pila_palo3.show()
print(f'\nPila mazo actualizada ({pila_mazo.size()} cartas): ')
pila_mazo.show()

palo4 = 'Basto'
pila_palo4 = Stack()
pila_mazo, pila_palo4 = separar_cartas(pila_mazo, palo4)
print(f'\nPila con cartas de {palo4}: ')
pila_palo4.show()
print(f'\nPila mazo actualizada ({pila_mazo.size()} cartas): ')
pila_mazo.show()

# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
print('\n----------------------------------------- Ordenamiento por palo, de manera creciente -----------------------------------------')
print(f'Pila con cartas de {palo1}: ')
pila_palo1.show()
pila_palo1_ordenada = ordenar_palo(pila_palo1)
print(f'\nPila ordenada con cartas de {palo1}: ')
pila_palo1_ordenada.show()

print(f'\nPila con cartas de {palo2}: ')
pila_palo2.show()
pila_palo2_ordenada = ordenar_palo(pila_palo2)
print(f'\nPila ordenada con cartas de {palo2}: ')
pila_palo2_ordenada.show()

print(f'\nPila con cartas de {palo3}: ')
pila_palo3.show()
pila_palo3_ordenada = ordenar_palo(pila_palo3)
print(f'\nPila ordenada con cartas de {palo3}: ')
pila_palo3_ordenada.show()

print(f'\nPila con cartas de {palo4}: ')
pila_palo4.show()
pila_palo4_ordenada = ordenar_palo(pila_palo4)
print(f'\nPila ordenada con cartas de {palo4}: ')
pila_palo4_ordenada.show()