'''
10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista, duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que permita realizar las siguientes actividades:
a. obtener la información de la canción más larga;
b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
c. obtener todas las canciones de la banda Arctic Monkeys;
d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
'''

from cancion import Cancion
from TDA_list import List

# --- CARGA DE DATOS ---

lista_canciones = List()
# Patricio Rey y sus Redonditos de Ricota
lista_canciones.append(Cancion("La Bestia Pop", "Patricio Rey y sus Redonditos de Ricota", 243, 24500))
lista_canciones.append(Cancion("El infierno está encantador esta noche", "Patricio Rey y sus Redonditos de Ricota", 289, 11000))
lista_canciones.append(Cancion("Motor-pisco", "Patricio Rey y sus Redonditos de Ricota", 296, 21500))
lista_canciones.append(Cancion("Preso en mi ciudad", "Patricio Rey y sus Redonditos de Ricota", 243, 19900))
lista_canciones.append(Cancion("Juguetes Perdidos", "Patricio Rey y sus Redonditos de Ricota", 430, 18700))
lista_canciones.append(Cancion("Blues de la libertad", "Patricio Rey y sus Redonditos de Ricota", 301, 23600))
lista_canciones.append(Cancion("Murga de la virgencita", "Patricio Rey y sus Redonditos de Ricota", 295, 6900))
lista_canciones.append(Cancion("Pool, averna y papusa", "Patricio Rey y sus Redonditos de Ricota", 295, 10600))
lista_canciones.append(Cancion("Tarea fina", "Patricio Rey y sus Redonditos de Ricota", 280, 18700))
lista_canciones.append(Cancion("Un poco de amor francés", "Patricio Rey y sus Redonditos de Ricota", 210, 7600))
lista_canciones.append(Cancion("Luzbelito y las sirenas", "Patricio Rey y sus Redonditos de Ricota", 320, 8200))

# Los Fundamentalistas del Aire Acondicionado
lista_canciones.append(Cancion("El tesoro de los inocentes", "Los Fundamentalistas del Aire Acondicionado", 258, 7500))
lista_canciones.append(Cancion("Y mientras tanto el sol se muere", "Los Fundamentalistas del Aire Acondicionado", 242, 6800))
lista_canciones.append(Cancion("Submarino soluble", "Los Fundamentalistas del Aire Acondicionado", 238, 6200))
lista_canciones.append(Cancion("Chante Noire", "Los Fundamentalistas del Aire Acondicionado", 310, 7100))  # cover?
lista_canciones.append(Cancion("Torito es muerto", "Los Fundamentalistas del Aire Acondicionado", 295, 5900))
lista_canciones.append(Cancion("Porco Rex", "Los Fundamentalistas del Aire Acondicionado", 270, 6400))

# La Renga
lista_canciones.append(Cancion("La balada del diablo y la muerte", "La Renga", 336, 15000))
lista_canciones.append(Cancion("El viento que todo empuja", "La Renga", 321, 11000))
lista_canciones.append(Cancion("Bien alto", "La Renga", 206, 9800))
lista_canciones.append(Cancion("En el baldío", "La Renga", 230, 27200))
lista_canciones.append(Cancion("Triste canción de amor", "La Renga", 270, 9200))
lista_canciones.append(Cancion("Cuando estés acá", "La Renga", 280, 8800))

# Callejeros
lista_canciones.append(Cancion("Señales", "Callejeros", 357, 13000))
lista_canciones.append(Cancion("Rocanroles sin destino", "Callejeros", 241, 10500))
lista_canciones.append(Cancion("Prohibido", "Callejeros", 190, 11500))
lista_canciones.append(Cancion("Cristal", "Callejeros", 215, 9900))
lista_canciones.append(Cancion("Fantasía o realidad", "Callejeros", 300, 20900))

# La Bersuit
lista_canciones.append(Cancion("Desconexión sideral", "La Bersuit", 291, 14000))
lista_canciones.append(Cancion("Vuelos", "La Bersuit", 264, 11200))
lista_canciones.append(Cancion("La argentinidad al palo", "La Bersuit", 310, 13500))
lista_canciones.append(Cancion("La danza de los muertos pobres", "La Bersuit", 285, 10800))
lista_canciones.append(Cancion("Un pacto", "La Bersuit", 240, 9500))

# The Rolling Stones
lista_canciones.append(Cancion("Start me up", "The Rolling Stones", 280, 6300))
lista_canciones.append(Cancion("Satisfaction", "The Rolling Stones", 235, 8100))
lista_canciones.append(Cancion("Paint it black", "The Rolling Stones", 210, 7000))
lista_canciones.append(Cancion("Angie", "The Rolling Stones", 280, 5900))
lista_canciones.append(Cancion("Sympathy for the Devil", "The Rolling Stones", 360, 1500))

# Arctic Monkeys
lista_canciones.append(Cancion("Do I Wanna Know?", "Arctic Monkeys", 273, 8000))
lista_canciones.append(Cancion("R U Mine?", "Arctic Monkeys", 183, 16500))
lista_canciones.append(Cancion("Why'd You Only Call Me When You're High?", "Arctic Monkeys", 200, 15500))
lista_canciones.append(Cancion("Fluorescent Adolescent", "Arctic Monkeys", 210, 14000))
lista_canciones.append(Cancion("505", "Arctic Monkeys", 270, 17500))

# Los Piojos
lista_canciones.append(Cancion("Civilización", "Los Piojos", 280, 12500))
lista_canciones.append(Cancion("Verano del '92", "Los Piojos", 290, 11800))
lista_canciones.append(Cancion("El farolito", "Los Piojos", 260, 13000))
lista_canciones.append(Cancion("Ruleta", "Los Piojos", 260, 13000))

#La Vela Puerca
lista_canciones.append(Cancion("Zafar", "La Vela Puerca", 240, 11000))
lista_canciones.append(Cancion("El viejo", "La Vela Puerca", 255, 10500))

# Rata Blanca
lista_canciones.append(Cancion("Mujer amante", "Rata Blanca", 240, 11000))
lista_canciones.append(Cancion("Aún estás en mis sueños", "Rata Blanca", 255, 10500))

# Divididos
lista_canciones.append(Cancion("Spaghetti del rock", "Divididos", 270, 9800))
lista_canciones.append(Cancion("¿Qué ves?", "Divididos", 220, 9200))
lista_canciones.append(Cancion("El arriero", "Divididos", 220, 9900))

# --- AGREGACIÓN DE FUNCIONES DE ORDENAMIENTO ---

def sort_by_duration(cancion):
    return cancion.duracion

def sort_by_reproductions(cancion):
    return cancion.reproducciones

lista_canciones.add_criterion('duracion', sort_by_duration)
lista_canciones.add_criterion('reproducciones', sort_by_reproductions)

#################################################  Ejecución de pruebas del enunciado  #################################################
print(f'\nLista original de canciones: ')
lista_canciones.show()

# a. obtener la información de la canción más larga;
print('\n-------------------------------------- a. Obtención de información de canción más larga --------------------------------------')
mayor_duracion = 0
cancion_mayor_duracion = None
for cancion in lista_canciones:
    duracion_parcial = cancion.duracion
    if duracion_parcial > mayor_duracion:
        mayor_duracion = duracion_parcial
        cancion_mayor_duracion = cancion

print(f'\nCanción más larga: \n{cancion_mayor_duracion}')

# lista_canciones.sort_by_criterion('duracion') # Menos líneas de códigos, pero más costosa porque ordena toda la lista antes.
# print(f'\nCanción más larga: \n{lista_canciones[-1]}')

# b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
print('\n------------------------------------------ b. Obtención de canciones más escuchadas ------------------------------------------')
lista_canciones.sort_by_criterion('reproducciones')

top = 5
print(f'Top {top} de canciones más escuchadas: ')
if (top) > lista_canciones.size():
    print(f'El "TOP" excede el tamaño de la lista.')
else:
    for i in range(top):
        index = i+1
        print(f'#{index} {lista_canciones[-index]}')

top = 10
print(f'\nTop {top} de canciones más escuchadas: ')
if (top) > lista_canciones.size():
    print(f'El "TOP" excede el tamaño de la lista.')
else:
    for i in range(top):
        index = i+1
        print(f'#{index} {lista_canciones[-index]}')

top = 40
print(f'\nTop {top} de canciones más escuchadas: ')
if (top) > lista_canciones.size():
    print(f'El "TOP" excede el tamaño de la lista.')
else:
    for i in range(top):
        index = i+1
        print(f'#{index} {lista_canciones[-index]}')

# c. obtener todas las canciones de la banda Arctic Monkeys;
print('\n--------------------------------------- c. Obtención de canciones de banda específica ----------------------------------------')
banda = 'Arctic Monkeys'
lista_auxiliar = List()
for cancion in lista_canciones:
    if cancion.banda == banda:
        lista_auxiliar.append(cancion)

print(f'Lista de canciones de la banda "{banda}": ')
lista_auxiliar.show()

# d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
print('\n--------------------------------- d. Muestreo de banda o artistas según cantidad de palabras ---------------------------------')
cantidad = 1
bandas_una_palabra = List()
for cancion in lista_canciones:
    banda = cancion.banda
    palabras = banda.split()
    if len(palabras) == cantidad and banda not in bandas_una_palabra:
        bandas_una_palabra.append(banda)

print(f'Nombres de bandas o artistas que son de {cantidad} palabra/s: ')
bandas_una_palabra.show()