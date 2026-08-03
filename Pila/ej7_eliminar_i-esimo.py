# 7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

from TDA_stack import Stack

def eliminar_iesimo(stack: Stack, elemento: int):
    for i in range (stack.size()):
        if i == elemento:
            eliminado = stack.on_top()
            stack.pop()
        else:
            stack_aux.push(stack.pop())

    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return stack, eliminado

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n------------------------------------- Eliminación del i-ésimo elemento debajo de la cima -------------------------------------')
stack = Stack()
stack_aux = Stack()

stack.push('Python')
stack.push('Mundo')
stack.push('Hola')
stack.push('Datos')
stack.push('Estructuras')
stack.push('Algoritmos')

print('\nPila original: ')
stack.show()

elemento = int(input('\nIngrese el número de elemento debajo de la cima que desea eliminar: '))

if elemento == 0:
    print(f'\nEl número {elemento} corresponde al elemento en la que está en la cima. No se puede eliminar.')
elif elemento < 0:
    print('\nDebe ingresar un número positivo.')
elif elemento > stack.size() -1:
    print('\nEl número ingresado excede la cantidad de elementos debajo de la cima.')
else:
    stack, eliminado = eliminar_iesimo(stack, elemento)
    print(f'\nEl elemento a eliminar es: "{eliminado}".')
    print('\nPila actualizada: ')
    stack.show()