# 11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

'''
◘ Algoritmo para resolver el problema:
    A un número dado, aplicarle división entera entre 10.
    Al resto, sumarlo a un acumulador e ir multiplicándolo por 10 en cada llamada. 
    Si el número es menor que 10, retornar el acumulador luego de multiplicarlo por 10 y sumarle el resto (caso base).
'''
def invertir_entero(num: int, acum: int = 0):
    print(f'Valor ingresado: {num}')
    if num < 10:
        print(f'Valor del resto: Ninguno. Acá no se calcula, porque es menor que 10 y ya no debe dividirse.')
        print(f'Valor del número que llegó al caso base: {num}.')
        acum = acum * 10 + num
        print(f'Valor del acumulador luego de calcularse en el caso base: {acum}.')
        print(f'-------------------------------------------------------------------------------------------------------------------')
        return acum
    else:
        resto = num % 10
        acum = acum * 10 + resto
        print(f'Valor del número luego de dividirlo entre 10: {num//10} (es el valor que ingresa a la siguiente llamada recursiva).')
        print(f'Valor del resto: {resto}.')
        print(f'Valor del acumulador que ingresa a la siguiente llamada recursiva: {acum}.')
        print(f'-------------------------------------------------------------------------------------------------------------------')
        return invertir_entero(num // 10, acum)

# Prueba
number = 1994
resultado = (invertir_entero(number))
print(f'Número invertido: {resultado}')