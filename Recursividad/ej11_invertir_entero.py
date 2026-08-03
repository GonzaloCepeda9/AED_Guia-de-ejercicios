# 11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

'''
◘ Algoritmo para resolver el problema:
    A un número dado, aplicarle división entera entre 10.
    Al resto, sumarlo a un acumulador e ir multiplicándolo por 10 en cada llamada. 
    Si el número es menor que 10, retornar el acumulador luego de multiplicarlo por 10 y sumarle el resto (caso base).
'''
def invertir_entero(num: int, acum: int = 0):
    if num < 10:
        acum = acum * 10 + num
        return acum
    else:
        resto = num % 10
        acum = acum * 10 + resto
        return invertir_entero(num // 10, acum)

# Prueba
number = 1994
if number and isinstance(number, int) and number > 0:
    resultado = (invertir_entero(number))
    print(f'Número ingresado: {number} | Número invertido: {resultado}.')
else:
    print('Debe ingresar un número entero positivo.')