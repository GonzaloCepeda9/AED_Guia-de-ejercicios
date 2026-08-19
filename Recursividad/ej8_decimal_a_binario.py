# 8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario

'''
◘ Algoritmo para resolver el problema:
    A un número dado, aplicarle división entera entre 2:
    • Si el resto es 0, retornar 0 en tipo de dato str.
    • Si el resto es 1, retornar 1 en tipo de dato str.
    • Si el número es 1 o es 0, retornar el mismo número (caso base).
'''

def decimal_a_binario(num: int):
    if num == 1 or num == 0:
        return f'{num}'
    elif num % 2 == 0:
        return decimal_a_binario(num // 2) + '0'
    else:
        return decimal_a_binario(num // 2) + '1'
    
#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n----------------------------------------- Conversión de un número decimal a binario ------------------------------------------')
number = 9
if number < 0:
    print('El número debe ser positivo.')
else:
    resultado = decimal_a_binario(number)
    print(f'Número decimal: {number} | Número binario: {resultado}.')
    # print(f'El número decimal {number} corresponde al número {resultado} en formato binario.')