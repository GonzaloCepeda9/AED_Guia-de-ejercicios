# Listado de alumnos
'''
9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
algoritmo que permita realizar la siguientes actividades:
a. mostrar los alumnos ordenados alfabéticamente por apellido;
b. indicar los alumnos que no desaprobaron ningún parcial;
c. determinar los alumnos que tienen promedio mayor a 8,89;
d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
e. mostrar el promedio de cada uno de los alumnos;
f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
i. mostrar todos los alumnos que rindieron en el año 2020;
j. debe modificar el TDA para implementar lista de lista.
'''

from alumno import Alumno
from parcial import Parcial
from TDA_list import List

lista_alumnos = List()

# --- CARGA DE DATOS ---

# Alumno 1: Apellido con L, promedio > 8.89, rindió Algoritmos en 2020, sin desaprobados.
al1 = Alumno("Lucas", "Lopez", 101)
al1.parciales.insert_value(Parcial("Algoritmos y estructuras de datos", 10, "2020-05-12"))
al1.parciales.insert_value(Parcial("Base de datos", 9, "2020-11-05"))
lista_alumnos.insert_value(al1)

# Alumno 2: Apellido con L, tiene un desaprobado en Base de Datos, rindió en 2020.
al2 = Alumno("Lara", "Ledesma", 102)
al2.parciales.insert_value(Parcial("Algoritmos y estructuras de datos", 7, "2020-06-10"))
al2.parciales.insert_value(Parcial("Base de datos", 2, "2020-10-15")) # Desaprobado
lista_alumnos.insert_value(al2)

# Alumno 3: Promedio alto (> 8.89), rindió Algoritmos pero no en 2020.
al3 = Alumno("Marcos", "Martinez", 103)
al3.parciales.insert_value(Parcial("Algoritmos y estructuras de datos", 9, "2021-05-20"))
al3.parciales.insert_value(Parcial("Cálculo Diferencial e Integral", 9, "2021-07-02"))
lista_alumnos.insert_value(al3)

# Alumno 4: No rindió Algoritmos, rindió Base de Datos (aprobado).
al4 = Alumno("Ana", "Alvarez", 104)
al4.parciales.insert_value(Parcial("Base de datos", 8, "2019-11-10"))
al4.parciales.insert_value(Parcial("Fundamentos de Programación", 7, "2019-06-15"))
lista_alumnos.insert_value(al4)

# Alumno 5: Apellido con L, rindió Algoritmos en 2020, tiene desaprobados.
al5 = Alumno("Luis", "Lucero", 105)
al5.parciales.insert_value(Parcial("Algoritmos y estructuras de datos", 4, "2020-05-12"))
al5.parciales.insert_value(Parcial("Ingeniería de Software", 2, "2020-09-20")) # Desaprobado
lista_alumnos.insert_value(al5)

# Alumno 6: Rindió Base de Datos (desaprobado), rindió en 2020.
al6 = Alumno("Gaston", "Gomez", 106)
al6.parciales.insert_value(Parcial("Base de datos", 3, "2020-11-05")) # Desaprobado
al6.parciales.insert_value(Parcial("Matemática Discreta", 6, "2020-06-22"))
lista_alumnos.insert_value(al6)

# Creación de funciones para ordenar por criterio
def order_by_name(alumno):
    return alumno.nombre
def order_by_surname(alumno):
    return alumno.apellido
def order_by_file(alumno):
    return alumno.legajo

# Agregación de criterios de búsqueda
lista_alumnos.add_criterion('nombre', order_by_name)
lista_alumnos.add_criterion('apellido', order_by_surname)
lista_alumnos.add_criterion('legajo', order_by_file)

#################################################  Ejecución de pruebas del enunciado  #################################################
print(f'\nLista original de alumnos: ')
lista_alumnos.show()

# a. mostrar los alumnos ordenados alfabéticamente por apellido;
print('\n---------------------------------------------- a. Muestreo de alumnos ordenados ----------------------------------------------')
print(f'Lista de alumnos ordenados alfabéticamente por apellido:')
lista_alumnos.sort_by_criterion('apellido')
lista_alumnos.show()

# b. indicar los alumnos que no desaprobaron ningún parcial;
print('\n-------------------------------------------- b. Indicación de alumnos sin aplazos --------------------------------------------')
for alumno in lista_alumnos:
    aplazado = False
    for parcial in alumno.parciales:
        if parcial.nota < 4:
            aplazado = True
    if aplazado == False:
        print(f'El alumno {alumno.apellido}, {alumno.nombre} no desaprobó ningún parcial.')

# c. determinar los alumnos que tienen promedio mayor a 8,89;
print('\n------------------------------------------------ c. Determinación de promedio ------------------------------------------------')
promedio_requerido = 8.89
print(f'Alumnos con promedio mayor a {promedio_requerido}: ')
for alumno in lista_alumnos:
    acumulador = 0
    for parcial in alumno.parciales:
        acumulador += parcial.nota
    cantidad_parciales = alumno.parciales.size()
    promedio = acumulador / cantidad_parciales

    if promedio > promedio_requerido:
        print(f'{alumno.nombre} {alumno.apellido} tiene un promedio de {promedio}')

# d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
print('\n--------------------------------------------- d. Mostar información por inicial ----------------------------------------------')
inicial = 'L'
print('Información de alumnos cuyos apellidos comienzan con L: ')
for alumno in lista_alumnos:
    if alumno.apellido.startswith(inicial):
        print(alumno)

# e. mostrar el promedio de cada uno de los alumnos;
print('\n------------------------------------------ e. Muestreo del promedio de los alumnos -------------------------------------------')
for alumno in lista_alumnos:
    acumulador = 0
    for parcial in alumno.parciales:
        acumulador += parcial.nota
    cantidad_parciales = alumno.parciales.size()
    promedio = acumulador / cantidad_parciales

    print(f'Alumno: {alumno} >> Promedio: {promedio}')

# f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
print('\n---------------------------------------------- f. Muestreo por cátedra rendida -----------------------------------------------')
catedra = 'Algoritmos y estructuras de datos'
print(f'Alumnos que rindieron {catedra}:')
for alumno in lista_alumnos:
    for parcial in alumno.parciales:
        if parcial.materia == catedra:
            print(alumno)

# g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
print('\n------------------------------------- g. Indicación de porcentaje de parciales aprobados -------------------------------------')
for alumno in lista_alumnos:
    sumatoria_aprobados = 0
    cantidad_aprobados = 0
    for parcial in alumno.parciales:
        sumatoria_aprobados += parcial.nota
        if parcial.nota >= 6:
            cantidad_aprobados += 1
    if cantidad_aprobados == 0:
        print(f'Alumno: {alumno} >> Porcentaje de parciales aprobados: {0}')
    else:
        cantidad_parciales = alumno.parciales.size()
        porcentaje_aprobados = cantidad_aprobados * 100 / cantidad_parciales
        print(f'Alumno: {alumno} >> Porcentaje de parciales aprobados: {porcentaje_aprobados}%')

# h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
print('\n------------------------------------ h. Indicación aprobados y desaprobados según materia ------------------------------------')
catedra = 'Base de datos'
aprobados = 0
desaprobados = 0
for alumno in lista_alumnos:
    for parcial in alumno.parciales:
        if parcial.materia == catedra:
            if parcial.nota >= 6:
                aprobados += 1
            else:
                desaprobados += 1
print(f'Cantidad de alumnos que aprobaron la cátedra {catedra}: {aprobados}.')
print(f'Cantidad de alumnos que desaprobaron la cátedra {catedra}: {aprobados}.')

# i. mostrar todos los alumnos que rindieron en el año 2020;
print('\n----------------------------------- i. Muestreo de alumnos que rindieron en año específico -----------------------------------')
anio = 2020
condicion = False
print(f'Alumnos que rindieron en el año {anio}:')
for alumno in lista_alumnos:
    condicion_cumplida = False
    for parcial in alumno.parciales:
        anio_parcial = int(parcial.fecha[:4])
        if anio_parcial == anio:
            condicion = True
            condicion_cumplida = True
            break
    if condicion_cumplida == True:
        print(alumno)
if condicion == False:
    print(f'Ningún alumno rindió en el año 2020.')