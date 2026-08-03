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
from superheroe import Superheroe

def order_by_name(element):
    return element.nombre

def order_by_year(element):
    return element.anio_aparicion

def order_by_house(element):
    return element.casa_comic

def order_by_biography(element):
    return element.biografia

lista_superheroes = List()
lista_superheroes.append(Superheroe("Spider-Man", 1962, "Marvel", "Joven que obtiene poderes tras ser picado por una araña radiactiva."))
lista_superheroes.append(Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor de curación."))
lista_superheroes.append(Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo que protege la Tierra de amenazas místicas."))  # Inicialmente DC para probar cambio
lista_superheroes.append(Superheroe("Iron Man", 1963, "Marvel", "Genio multimillonario que construye un traje de alta tecnología."))
lista_superheroes.append(Superheroe("Capitana Marvel", 1968, "Marvel", "Piloto que obtiene poderes cósmicos."))
lista_superheroes.append(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con fuerza sobrehumana."))
lista_superheroes.append(Superheroe("Flash", 1940, "DC", "Posee velocidad sobrehumana gracias a la Fuerza de la Velocidad."))
lista_superheroes.append(Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia, usa un traje espacial."))
lista_superheroes.append(Superheroe("Batman", 1939, "DC", "Vigilante que usa una armadura y artilugios."))
lista_superheroes.append(Superheroe("Superman", 1938, "DC", "Kryptoniano con poderes solares."))
lista_superheroes.append(Superheroe("Linterna Verde", 1940, "DC", "Miembro del cuerpo de linternas verdes, usa un anillo de poder."))

print(f'\nLista original de superhéroes: ')
lista_superheroes.show()

# Agregar criterios de búsqueda:
lista_superheroes.add_criterion('nombre', order_by_name)
lista_superheroes.add_criterion('anio_aparicion', order_by_year)
lista_superheroes.add_criterion('casa_comic', order_by_house)
lista_superheroes.add_criterion('biografia', order_by_biography)

#################################################  Ejecución de pruebas del enunciado  #################################################
# a. eliminar el nodo que contiene la información de Linterna Verde;
print('\n--------------------------------- a. Eliminación de nodo/elemento con información específica ---------------------------------')
eliminado = lista_superheroes.delete_value('nombre', 'Linterna Verde')
print(f'El superhéroe "{eliminado.nombre}" ha sido eliminado.')
print(f'\nLista de superhéroes actualizada: ')
lista_superheroes.show()

# b. mostrar el año de aparición de Wolverine;
print('\n--------------------------------------- b. Muestra del año de aparición del personaje ----------------------------------------')
superheroe = 'Wolverine'
position = lista_superheroes.search('nombre', superheroe)
if position:
    print(f'Año de aparición del superhéroe "{superheroe}": {lista_superheroes[position].anio_aparicion}')
else:
    print(f'El superhéroe {superheroe} no se encuentra en la lista.')

# c. cambiar la casa de Dr. Strange a Marvel;
print('\n------------------------------------------ c. Cambio/modificación de casa de comic -------------------------------------------')
superheroe = 'Dr. Strange'
casa_nueva = 'Marvel'
position = lista_superheroes.search('nombre', superheroe)
if position:
    lista_superheroes[position].casa_comic = casa_nueva
    print(f'La casa del superhéroe "{superheroe}" ha sido actualizada a "{casa_nueva}."')
else:
    print(f'El superhéroe {superheroe} no se encuentra en la lista.')
print(f'\nLista de superhéroes actualizada: ')
lista_superheroes.show()

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print('\n---------------------- d. Muestra del nombre superhéroe cuya biografía menciona una palabra específica -----------------------')
palabra1 = 'traje'
palabra2 = 'armadura'
print(f'Palabras mencionadas: "{palabra1}" ó "{palabra2}": ')
for superheroe in lista_superheroes:
    if palabra1 in superheroe.biografia or palabra2 in superheroe.biografia:
        print(f'{superheroe.nombre}')

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print('\n----------------------------- e. Muestra de nombre y casa de superhéroe según fecha de aparición -----------------------------')
anio = 1963
print(f'Fecha de aparición anterior a "{anio}": ')
for superheroe in lista_superheroes:
    if superheroe.anio_aparicion < anio:
        print(f'{superheroe.nombre} | {superheroe.anio_aparicion}')

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print('\n----------------------------- f. Muestra de la casa a la que pertenece el superhéroe solicitado ------------------------------')
superheroe1 = 'Capitana Marvel'
superheroe2 = 'Mujer Maravilla'
print(f'Superhéroes solicitados: {superheroe1} y {superheroe2}.')
for superheroe in lista_superheroes:
    if superheroe.nombre == superheroe1 or superheroe.nombre == superheroe2:
        print(f'{superheroe.nombre}: {superheroe.casa_comic}')

# g. mostrar toda la información de Flash y Star-Lord;
print('\n-------------------------------- g. Muestra de información completa del superhéroe solicitado --------------------------------')
superheroe1 = 'Flash'
superheroe2 = 'Star-Lord'
print(f'Superhéroes solicitados: {superheroe1} y {superheroe2}.')
for superheroe in lista_superheroes:
    if superheroe.nombre == superheroe1 or superheroe.nombre == superheroe2:
        print(superheroe)

# h. listar los superhéroes que comienzan con la letra B, M y S;
print('\n---------------------------- h. Listado de superhéroes cuyo nombre comienza con letra específica -----------------------------')
letra1 = 'B'
letra2 = 'M'
letra3 = 'S'
print(f'Letras iniciales: "{letra1}", "{letra2}" ó "{letra3}": ')
for superheroe in lista_superheroes:
    if superheroe.nombre[0] == letra1 or superheroe.nombre[0] == letra2 or superheroe.nombre[0] == letra3:
        print(superheroe)

# i. determinar cuántos superhéroes hay de cada casa de comic.
print('\n----------------------------- i. Determinación de cantidad de superhéroes por cada casa de comic -----------------------------')
casa_comic1 = 'Marvel'
casa_comic2 = 'DC'
cantidad_casa1 = 0
cantidad_casa2 = 0
print(f'Casas de comics: {casa_comic1} y {casa_comic2}.')
for superheroe in lista_superheroes:
    if superheroe.casa_comic == casa_comic1:
        cantidad_casa1 += 1
    elif superheroe.casa_comic == casa_comic2:
        cantidad_casa2 += 1
print(f'En la casa de comic "{casa_comic1}" hay {cantidad_casa1} superhéroes.')
print(f'En la casa de comic "{casa_comic2}" hay {cantidad_casa2} superhéroes.')