# 3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.

from TDA_queue import Queue
from TDA_stack import Stack

def determinar_palindromo(secuencia: str):
    queue = Queue()
    stack = Stack()
    palindroma = True
    secuencia_normalizada = secuencia.lower().replace(" ", "")
    for elemento in secuencia_normalizada:
        queue.arrive(elemento)
        stack.push(elemento)

    while stack.size() > 0:
        elemento_cima = stack.pop()
        elemento_frente = queue.attention()
        if elemento_cima != elemento_frente:
            palindroma = False

    return palindroma

#################################################  Ejecución de pruebas del enunciado  #################################################
secuencia = input(f'\nIngrese una secuencia de caracteres: ')
print(f'\n------------------------------------------- Determinación de secuencia palíndroma --------------------------------------------')
palindromo = determinar_palindromo(secuencia)
if palindromo == True:
    print(f'La secuencia de caracteres "{secuencia}" es palíndroma.')
else:
    print(f'La secuencia de caracteres "{secuencia}" no es palíndroma.')