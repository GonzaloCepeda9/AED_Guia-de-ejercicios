# Extra: Implementar una función que permita calcular el factorial de un número entero dado.

# Factorial recursiva
def factorial_recursivo(num: int) -> int:
    if num < 0 or num - (int(num)) != 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial_recursivo(num-1)

# Factorial iterativa
def factorial_iterativa(num):
    if num < 0 or num - (int(num)) != 0:
        return None
    else:
        acumulador = 1
        while num > 0:
            acumulador = acumulador * num
            num -= 1
        return acumulador

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n--------------------------------------------- Factorial de un número entero dado ---------------------------------------------')
numero = 4
resultado = factorial_recursivo(numero)
print(f'\nFactorial con función recursiva:')
if resultado:
    print(f'{numero}! = {resultado}')
else:
    print(f'Debe ingresar un número entero positivo.')

numero = 5
resultado = factorial_iterativa(numero)
print(f'\nFactorial con función iterativa:')
if resultado:
    print(f'{numero}! = {resultado}')
else:
    print(f'Debe ingresar un número entero positivo.')