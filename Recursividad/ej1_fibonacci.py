# 1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

# Fibonacci recursivo
def fibonacci_recursiva(num: int):
    if num < 0:
        return None
    elif num == 0 or num == 1:
        return num
    else:
        return fibonacci_recursiva(num-1) + fibonacci_recursiva(num-2)

# Fibonacci iterativo
def fibonacci_iterativa(num: int):
    if num < 0 or num - (int(num)) != 0:
        return None
    
    if num == 0 or num == 1:
        return num
    else:
        result1 = 0
        result2 = 1
        result = 0

        for _ in range(2, num+1):
            result = result1 + result2
            result1 = result2
            result2 = result

        return result

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n-------------------------------------- Obtención de valores de la sucesión de Fibonacci --------------------------------------')
fib_prueba = 6
result_recursivo = fibonacci_recursiva(fib_prueba)
print(f'Fibonacci con función recursiva:')
if result_recursivo:
    print(f'F({fib_prueba}) = {result_recursivo}')
else:
    print(f'Debe ingresar un número entero positivo.')

fib_prueba = 9
result_iterativo = fibonacci_iterativa(fib_prueba)
print(f'\nFibonacci con función recursiva:')
if result_iterativo:
    print(f'F({fib_prueba}) = {result_iterativo}')
else:
    print(f'Debe ingresar un número entero positivo.')