# 10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

'''
◘ Algoritmo para resolver el problema:
    A un número dado, aplicarle división entera entre 10.
    • En cada llamada, sumar 1.
    • Si el número es menor que 10, devolver 1 (caso base).
'''

def cantidad_digitos(num: int):
    num = abs(num)
    if num < 10:
        return 1
    else:
        return 1 + cantidad_digitos(num//10)
    
# Prueba
print('--------------------------------------------- Función: Contar cantidad de dígitos ----------------------------------------------')
number = -999
resultado = cantidad_digitos(number)
print(f'El número {number} tiene {resultado} dígitos.')