# 9. Resolver el problema del factorial de un número utilizando una pila.

from TDA_stack import Stack

def calcular_factorial(stack: Stack, numero: int):
    for _ in range(numero):
        stack.push(numero)
        numero = numero - 1

    acumulador = 1

    while stack.size() > 0:
        acumulador = acumulador * stack.pop()

    return acumulador

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n------------------------------------------- Resolución del problema del factorial --------------------------------------------')
stack = Stack()
numero = int(input('Ingrese un número para calcular su factorial: '))
factorial = calcular_factorial(stack, numero)
print(f'El factorial de {numero} es {factorial}.')