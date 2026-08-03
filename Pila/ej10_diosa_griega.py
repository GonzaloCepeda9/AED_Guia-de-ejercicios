# 10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una pila con nombres de dioses griegos.

from TDA_stack import Stack

def insertar_nombre(stack: Stack, diosa: str, posicion: int):

    stack_aux = Stack()

    for i in range(stack.size()):
        nombre_cima = stack.pop()
        if i == posicion:
            stack_aux.push(diosa)
            stack_aux.push(nombre_cima)
        else:
            stack_aux.push(nombre_cima)
    
    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())
    
    return stack

#################################################  Ejecución de pruebas del enunciado  #################################################
pila_dioses = Stack()

pila_dioses.push("Zeus")
pila_dioses.push("Hera")
pila_dioses.push("Poseidón")
pila_dioses.push("Deméter")
pila_dioses.push("Apolo")
pila_dioses.push("Artemisa")
pila_dioses.push("Ares")
pila_dioses.push("Afrodita")
pila_dioses.push("Hermes")
print('\nPila original: ')
pila_dioses.show()
deidad = input(f'\nIngrese el nombre de la deidad que desea agregar: ') # Utilizar en caso de querer solicitárselo al usuario.
posicion = int(input(f'Ingrese la posición en la que desea agregarlo/a: ')) # Utilizar en caso de querer solicitárselo al usuario.
deidad = 'Atenea'
posicion = 1
print('\n------------------------------- Inserción de un nombre en la i-ésima posición debajo de la cima ------------------------------')
print(f'Nombre a agregar: {deidad} | Posición debajo de la cima: {posicion}.')
insertar_nombre(pila_dioses, deidad, posicion)
print(f'\nPila actualizada: ')
pila_dioses.show()