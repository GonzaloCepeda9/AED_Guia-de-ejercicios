# 20. Movimientos de un robot
"""
Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son cantidad de pasos y dirección (suponga que el robot solo puede moverse en ocho direcciones: norte, sur, este, oeste, noreste, noroeste, sureste y suroeste).
Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de partida, retornando por el mismo camino que fue.
"""

from TDA_stack import Stack

movimientos_robot = Stack()

movimiento_contrario = {
    'norte': 'sur',
    'sur': 'norte',
    'este': 'oeste',
    'oeste': 'este',
    'noreste': 'suroeste',
    'suroeste': 'noreste',
    'noroeste': 'sureste',
    'sureste': 'noroeste'
}

# Registrar movimientos de un robot (paso y dirección):
print('\n--------------------------------------------- Registro de movimientos del robot ----------------------------------------------')
movimiento = input('Ingrese los pasos y dirección del movimiento, separados por un espacio (ejemplo: 9 sur ); o "fin" para finalizar: ')

while movimiento != 'fin':

    datos = movimiento.split() # Divide la cadena ingresada por espacios, y devuelve una lista con los elementos.

    if len(datos) > 0:
        pasos = int(datos[0]) # Si no ingresa un número, el programa lanza error. Esto no se puede corregir sin try-except, todavía no lo hemos dado.
        direccion = datos[1]

        print(f'El robot se movió {pasos} paso/s hacia el {direccion}.')

        movimientos_robot.push(datos)

    movimiento = input('Ingrese los pasos y dirección del movimiento, separados por un espacio (ejemplo: 9 sur ); o "fin" para finalizar: ')

print('Secuencia de movimientos finalizada.')

# Generar la secuencia de movimientos necesarios para hacer volver al robot a su lugar de partida:
print('\n----------------------- Secuencia de movimientos necesaria para volver al robot a su lugar de partida ------------------------')
while movimientos_robot.size() > 0:
    pasos, direccion = movimientos_robot.pop()
    direccion_contraria = movimiento_contrario[direccion]
    print(f'El robot debe moverse {pasos} pasos hacia la dirección {direccion_contraria}.')