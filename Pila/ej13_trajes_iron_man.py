# 13. Trajes de Iron Man
"""
Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver las siguientes actividades:
    a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas;
    b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
    c. eliminar los modelos de los trajes destruidos mostrando su nombre;
    d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, estos deben cargarse por separado; // No requiere respuesta.
    e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
    f. mostrar los nombres de los trajes utilizados en las películas “Spider-Man: Homecoming (2017)” y “Captain America: Civil War (2016)”.
"""

from TDA_stack import Stack
from traje import Traje

pila_trajes = Stack()

pila_trajes.push(Traje("Mark I", "Iron Man (2008)", "Dañado"))
pila_trajes.push(Traje("Mark III", "Iron Man (2008)", "Dañado"))
pila_trajes.push(Traje("Mark V", "Iron Man 2 (2010)", "Dañado"))
pila_trajes.push(Traje("Mark VI", "Iron Man 2 (2010)", "Dañado"))
pila_trajes.push(Traje("Mark VII", "The Avengers (2012)", "Dañado"))
pila_trajes.push(Traje("Mark XLII", "Iron Man 3 (2013)", "Destruido"))
pila_trajes.push(Traje("Mark XLIV (Hulkbuster)", "Avengers: Age of Ultron (2015)", "Dañado"))
pila_trajes.push(Traje("Mark XLV", "Avengers: Age of Ultron (2015)", "Impecable"))
pila_trajes.push(Traje("Mark XLVI", "Captain America: Civil War (2016)", "Dañado"))
pila_trajes.push(Traje("Mark L", "Avengers: Infinity War (2018)", "Dañado"))
pila_trajes.push(Traje("Mark LXXXV", "Avengers: Endgame (2019)", "Destruido"))

# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas.
def determinar_utilizados(stack: Stack, traje_utilizado: str):

    stack_aux = Stack()
    stack_peliculas = Stack()

    while stack.size() > 0:
        traje_cima = stack.pop()
        stack_aux.push(traje_cima)

        if traje_cima.modelo == traje_utilizado:
            stack_peliculas.push(traje_cima)

    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return stack_peliculas

# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
def mostrar_daniados(stack: Stack, estado: str):

    stack_aux = Stack()
    trajes_daniados = Stack()

    while stack.size() > 0:
        
        traje_cima = stack.pop()
        stack_aux.push(traje_cima)

        if traje_cima.estado == estado:
            trajes_daniados.push(traje_cima.modelo)
        
    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return trajes_daniados

# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
def eliminar_por_estado(stack: Stack, estado: str):
    
    stack_aux = Stack()
    trajes_destruidos = Stack()

    while stack.size() > 0:

        traje_cima = stack.on_top()

        if traje_cima.estado == estado:    
            trajes_destruidos.push(traje_cima.modelo)
            stack.pop()
        else:
            stack_aux.push(stack.pop())

    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return trajes_destruidos

# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
def agregar_modelo(stack: Stack, traje: Traje):

    stack_aux = Stack()
    traje_repetido = False
    
    while stack.size() > 0:
        traje_cima = stack.pop()

        if traje_cima.modelo == traje.modelo and traje_cima.pelicula == traje.pelicula:
            traje_repetido = True

        stack_aux.push(traje_cima)

    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    if traje_repetido == False:
        stack.push(traje)

    return traje_repetido

# f. mostrar los nombres de los trajes utilizados en las películas “Spider-Man: Homecoming (2017)” y “Captain America: Civil War (2016)”.
def mostrar_utilizados(stack: Stack, pelicula: str):
    stack_aux = Stack()
    utilizados_pelicula = Stack()

    while stack.size() > 0:
        utilizado = stack.pop()

        if utilizado.pelicula == pelicula:
            utilizados_pelicula.push(utilizado.modelo)

        stack_aux.push(utilizado)

    while stack_aux.size() > 0:
        stack.push(stack_aux.pop())

    return utilizados_pelicula

#################################################  Ejecución de pruebas del enunciado  #################################################

print(f'\n------------------------------------------------------- Pila original --------------------------------------------------------')
print(f'Pila original de trajes antes de ejecutar pruebas: ')
pila_trajes.show()

# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas.
print(f'\n----------------------------------------- a. Determinación de utilización de trajes ------------------------------------------')
peliculas = Stack()
traje_utilizado = 'Mark XLIV (Hulkbuster)'
peliculas = determinar_utilizados(pila_trajes, traje_utilizado)

if not peliculas.is_empty():
    print(f'El modelo de traje {traje_utilizado} fue utilizado en las siguientes películas: ')
    peliculas.show()
else:
    print(f'El traje {traje_utilizado} no se utilizó en ninguna película.')

# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
print(f'\n---------------------------------------- b. Muestra de modelos de trajes según estado ----------------------------------------')
estado = 'Dañado'
trajes_daniados = Stack()
trajes_daniados = mostrar_daniados(pila_trajes, estado)

if not trajes_daniados.is_empty():
    print(f'Los modelos de trajes que quedaron en estado "{estado}" son: ')
    trajes_daniados.show()
else:
    print('Ningún traje fue dañado en estas películas.')

# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
print(f'\n------------------------------------------- c. Eliminación de trajes según estado --------------------------------------------')
estado = 'Destruido'
trajes_eliminados = eliminar_por_estado(pila_trajes, estado)

if not trajes_eliminados.is_empty():
    # print(f'Los trajes con estado "{estado}" son: ')
    while trajes_eliminados.size() > 0:
        traje_eliminado = trajes_eliminados.pop()
        print(f'El traje "{traje_eliminado}" con estado "{estado}" ha sido eliminado.')
else:
    print('No se encontraron trajes con ese estado.')

# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
print(f'\n---------------------------------------------- e. Agregación de traje a la pila ----------------------------------------------')
print(f'Pila de trajes antes de intentar agregar uno nuevo: ')
pila_trajes.show()

nuevo_traje = Traje("Mark LXXXV", "Avengers: Endgame (2019)", "Destruido")
agregado = agregar_modelo(pila_trajes, nuevo_traje)

if agregado != True:
    print('\nEl traje fue agregado exitosamente.')
else:
    print('No se pueden cargar modelos repetidos en una misma película.')

print('\nPila de trajes luego de intentar agregar uno nuevo: ')
pila_trajes.show()

# f. mostrar los nombres de los trajes utilizados en las películas “Spider-Man: Homecoming (2017)” y “Captain America: Civil War (2016)”.
print(f'\n----------------------------------------- f. Muestra de nombres de trajes utilizados -----------------------------------------')
pelicula1 = 'Spider-Man: Homecoming (2017)'
utilizados_pelicula1 = Stack()
utilizados_pelicula1 = mostrar_utilizados(pila_trajes, pelicula1)

if not utilizados_pelicula1.is_empty():
    print(f'Los trajes utilizados en la película {pelicula1} fueron: ')
    utilizados_pelicula1.show()
else:
    print(f'La película "{pelicula1}" no se encuentra en la lista.')

pelicula2 = 'Captain America: Civil War (2016)'
utilizados_pelicula2 = Stack()
utilizados_pelicula2 = mostrar_utilizados(pila_trajes, pelicula2)

if not utilizados_pelicula2.is_empty():
    print(f'En la película "{pelicula2}" se utilizaron los siguientes trajes: ')
    utilizados_pelicula2.show()
else:
    print(f'El traje no fue utilizado en ninguna película')

print(f'\n------------------------------------------------------- Pila original --------------------------------------------------------')
print(f'Pila original de trajes después de ejecutar pruebas: ')
pila_trajes.show()