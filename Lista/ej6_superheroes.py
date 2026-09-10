# Superhéroes de comics
'''
6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.
'''

from TDA_list import List
from ej6_class_superheroe import Superheroe

# --------- CREACIÓN DE FUNCIÓN PARA SEPARAR SECCIONES --------- #
def print_seccion(titulo, ancho=120):
    print(f'\n{f' {titulo} '.center(ancho, "-")}')

# --------- CREACIÓN DE LISTA --------- #
lista_superheroes = List()

# --------- CREACIÓN DE FUNCIONES PARA ORDENAR POR CRITERIO --------- #

def order_by_name(element):
    return element.nombre

def order_by_year(element):
    return element.anio_aparicion

def order_by_house(element):
    return element.casa_comic

def order_by_biography(element):
    return element.biografia

# --------- AGREGACIÓN DE CRITERIOS DE BÚSQUEDA --------- #
lista_superheroes.add_criterion('nombre', order_by_name)
lista_superheroes.add_criterion('anio_aparicion', order_by_year)
lista_superheroes.add_criterion('casa_comic', order_by_house)
lista_superheroes.add_criterion('biografia', order_by_biography)

# --------- CARGA DE DATOS EN LA LISTA --------- #
lista_superheroes.insert_value(Superheroe("Spider-Man", 1962, "Marvel", "Joven que obtiene poderes tras ser picado por una araña radiactiva."))
lista_superheroes.insert_value(Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor de curación."))
lista_superheroes.insert_value(Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo que protege la Tierra de amenazas místicas."))  # Inicialmente DC para probar cambio
lista_superheroes.insert_value(Superheroe("Iron Man", 1963, "Marvel", "Genio multimillonario que construye un traje de alta tecnología."))
lista_superheroes.insert_value(Superheroe("Capitana Marvel", 1968, "Marvel", "Piloto que obtiene poderes cósmicos."))
lista_superheroes.insert_value(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con fuerza sobrehumana."))
lista_superheroes.insert_value(Superheroe("Flash", 1940, "DC", "Posee velocidad sobrehumana gracias a la Fuerza de la Velocidad."))
lista_superheroes.insert_value(Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia, usa un traje espacial."))
lista_superheroes.insert_value(Superheroe("Batman", 1939, "DC", "Vigilante que usa una armadura y artilugios."))
lista_superheroes.insert_value(Superheroe("Superman", 1938, "DC", "Kryptoniano con poderes solares."))
lista_superheroes.insert_value(Superheroe("Linterna Verde", 1940, "DC", "Miembro del cuerpo de linternas verdes, usa un anillo de poder."))

#################################################  EJECUCIÓN DE PRUEBAS DEL ENUNCIADO  #################################################
print('\n==================================== Ejercicio 6 - Superhéroes de comics ====================================')
print('\n----------------------------------------------- Lista original de superhéroes ------------------------------------------------')
lista_superheroes.show()

# a. eliminar el nodo que contiene la información de Linterna Verde;
print_seccion('a. Eliminación de elemento con información específica')
print('Enunciado: \n  → a. eliminar el nodo que contiene la información de Linterna Verde;')
print('\nDatos ingresados:')
nombre_elemento = 'Linterna Verde'
print(f'  → Nombre del elemento: {nombre_elemento}')
print('\nResultado:')
eliminado = lista_superheroes.delete_value('nombre', nombre_elemento)
if eliminado is not None:
    print('  → Elemento eliminado:')
    print(f'  → {eliminado}')
    print('Lista actualizada:')
    for superheroe in lista_superheroes:
        print(f'  → {superheroe.nombre}')
else:
    print(f'  → El superhéroe "{nombre_elemento}" no se encuentra en la lista.')

# b. mostrar el año de aparición de Wolverine;
print_seccion('b. Muestra del año de aparición de un superhéroe específico')
print('Enunciado:\n  → b. mostrar el año de aparición de Wolverine;')
print('\nDatos ingresados:')
nombre_superheroe = 'Wolverine'
print(f'  → Nombre del superhéroe: {nombre_superheroe}')
position = lista_superheroes.search('nombre', nombre_superheroe)
print('\nResultado:')
if position is not None:
    print(f'  → Año de aparición: {lista_superheroes[position].anio_aparicion}')
else:
    print(f'  → El superhéroe "{nombre_superheroe}" no se encuentra en la lista.')


# c. cambiar la casa de Dr. Strange a Marvel;
print_seccion('c. Modificación de casa de comic')
print('Enunciado: \n  → c. cambiar la casa de Dr. Strange a Marvel;')
print('\nDatos ingresados:')
superheroe = 'Dr. Strange'
casa_nueva = 'Marvel'
print(f'  → Nombre del superhéroe: {superheroe}')
print(f'  → Casa nueva: {casa_nueva}')
print('\nResultado:')
position = lista_superheroes.search('nombre', superheroe)
if position is not None:
    lista_superheroes[position].casa_comic = casa_nueva
    print(f'  → Casa actualizada correctamente.')
    print('\nLista actualizada:')
    for superheroe in lista_superheroes:
        print(f'  → {superheroe.nombre} | Casa: {superheroe.casa_comic}')
else:
    print(f'  → El superhéroe "{superheroe}" no se encuentra en la lista.')

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra "traje" o "armadura";
print_seccion('d. Muestra de nombre del superhéroe cuya biografía menciona una palabra específica')
print('Enunciado: \n  → d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra "traje" o "armadura";')
print('\nDatos ingresados:')
palabra1 = 'traje'
palabra2 = 'armadura'
print(f'  → Palabra 1: {palabra1}')
print(f'  → Palabra 2: {palabra2}')
print('\nResultado:')
lista_superheroes_aux = List()
for superheroe in lista_superheroes:
    if palabra1 in superheroe.biografia or palabra2 in superheroe.biografia:
        lista_superheroes_aux.insert_value(superheroe)
if not lista_superheroes_aux.is_empty():
    for superheroe in lista_superheroes_aux:
        print(f'  → {superheroe.nombre}')
else:
    print(f'  → No se encontraron superhéroes cuya biografía incluya la palabra "{palabra1}" o "{palabra2}".')

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print_seccion('e. Muestra de nombre y casa de superhéroe según fecha de aparición')
print('Enunciado: \n  → e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;')
print('\nDatos ingresados:')
anio = 1963
print(f'  → Año de aparición anterior a: {anio}')
print('\nResultado:')
lista_superheroes_aux = List()
for superheroe in lista_superheroes:
    if superheroe.anio_aparicion < anio:
        lista_superheroes_aux.insert_value(superheroe)
if not lista_superheroes_aux.is_empty():
    print(f'  → Nombre: {superheroe.nombre} | Casa: {superheroe.casa_comic}')
else:
    print(f'  → No se encontraron superhéroes cuya fecha de aparición sea anterior al año {anio}".')

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print_seccion('f. Muestra de la casa a la que pertenece el superhéroe solicitado')
print('Enunciado: \n  → f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;')
print(f'\nDatos ingresados')
superheroe1 = 'Capitana Marvel'
superheroe2 = 'Mujer Maravilla'
print(f'  → Nombre de superhéroe 1: {superheroe1}')
print(f'  → Nombre de superhéroe 2: {superheroe2}')
print('\nResultado:')
lista_superheroes_aux = List()
encontrado1 = False
encontrado2 = False
for superheroe in lista_superheroes:
    if superheroe.nombre == superheroe1:
        encontrado1 = True
        lista_superheroes_aux.insert_value(superheroe)
    elif superheroe.nombre == superheroe2:
        encontrado2 = True
        lista_superheroes_aux.insert_value(superheroe)

if not lista_superheroes_aux.is_empty():
    for superheroe in lista_superheroes_aux:
        print(f'  → {superheroe.nombre} | Casa: {superheroe.casa_comic}')
    if not encontrado1:
        print(f'  → El superhéroe {superheroe1} no se encuentra en la lista.')
    if not encontrado2:
        print(f'  → El superhéroe {superheroe2} no se encuentra en la lista.')
else:
    print(f'  → Los superheroes {superheroe1} y {superheroe2} no se encuentran en la lista.')

# g. mostrar toda la información de Flash y Star-Lord;
print_seccion('g. Muestra de información completa del superhéroe solicitado')
print('Enunciado: \n  → g. mostrar toda la información de Flash y Star-Lord;')
print('\nDatos ingresados:')
superheroe1 = 'Flash'
superheroe2 = 'Star-Lord'
print(f'  → Nombre de superhéroe 1: {superheroe1}')
print(f'  → Nombre de superhéroe 2: {superheroe2}')
print('\nResultado:')
lista_superheroes_aux = List()
encontrado1 = False
encontrado2 = False
for superheroe in lista_superheroes:
    if superheroe.nombre == superheroe1:
        encontrado1 = True
        lista_superheroes_aux.insert_value(superheroe)
    elif superheroe.nombre == superheroe2:
        encontrado2 = True
        lista_superheroes_aux.insert_value(superheroe)

if not lista_superheroes_aux.is_empty():
    for superheroe in lista_superheroes_aux:
        print(f'  → {superheroe}')
    if not encontrado1:
        print(f'  → El superhéroe {superheroe1} no se encuentra en la lista.')
    if not encontrado2:
        print(f'  → El superhéroe {superheroe2} no se encuentra en la lista.')
else:
    print(f'  → Los superheroes {superheroe1} y {superheroe2} no se encuentran en la lista.')

# h. listar los superhéroes que comienzan con la letra B, M y S;
print_seccion('h. Listado de superhéroes cuyo nombre comienza con letra específica')
print('Enunciado: \n  → h. listar los superhéroes que comienzan con la letra B, M y S;')
print('\nDatos ingresados:')
inicial1 = 'Z'
inicial2 = 'V'
inicial3 = 'K'
iniciales = (inicial1, inicial2, inicial3)
print(f'  → Iniciales: {iniciales}')
print('\nResultado:')
lista_superheroes_aux = List()
for superheroe in lista_superheroes:
    if superheroe.nombre.startswith(iniciales):
        lista_superheroes_aux.insert_value(superheroe)
if not lista_superheroes_aux.is_empty():
    for superheroe in lista_superheroes_aux:
        print(f'  → {superheroe}')
else:
    print(f'  → No se encontraron superhéroes cuyos nombres comienzan con las iniciales {inicial1}, {inicial2} o {inicial3}.')

# i. determinar cuántos superhéroes hay de cada casa de comic.
print_seccion('i. Determinación de cantidad de superhéroes por cada casa de comic')
print('Enunciado: \n  → i. determinar cuántos superhéroes hay de cada casa de comic.')
print('\nDatos ingresados:')
casa_comic1 = 'Marvel'
casa_comic2 = 'DC'
cantidad_casa1 = 0
cantidad_casa2 = 0
print(f'  → Casa de comic 1: {casa_comic1}')
print(f'  → Casa de comic 2: {casa_comic2}')
print('\nResultado:')
for superheroe in lista_superheroes:
    if superheroe.casa_comic == casa_comic1:
        cantidad_casa1 += 1
    elif superheroe.casa_comic == casa_comic2:
        cantidad_casa2 += 1

if cantidad_casa1 > 0:
    print(f'  → En la casa de comic "{casa_comic1}" hay {cantidad_casa1} superhéroes.')
else:
    print(f'  → No se encontraron superhéroes en la casa de comic {casa_comic1}')

if cantidad_casa2 > 0:
    print(f'  → En la casa de comic "{casa_comic2}" hay {cantidad_casa2} superhéroes.')
else:
    print(f'  → No se encontraron superhéroes en la casa de comic {casa_comic2}')