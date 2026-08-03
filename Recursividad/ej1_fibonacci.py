# 1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

# Fibonacci recursivo
def fibonacci(num: int):
    if num < 0:
        return "El número debe ser positivo."
    elif num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# Prueba
print('------------------------------------------------- Función: Fibonacci recursivo -------------------------------------------------')
fib_prueba = 6
result_recursivo = fibonacci(fib_prueba)
print(f'Fibonacci de {fib_prueba} = {result_recursivo}.')

# Fibonacci iterativo
def fibonacci_iterativa(num: int):
    if num == 0 or num == 1:
        return num
    else:
        result1 = 0
        result2 = 1
        result = 0

        for i in range(2, num+1):
            result = result1 + result2
            result1 = result2
            result2 = result

        return result

# Prueba
print('------------------------------------------------- Función: Fibonacci iterativo -------------------------------------------------')
fib_prueba = 7
result_iterativo = fibonacci_iterativa(fib_prueba)
print(f'Fibonacci de {fib_prueba} = {result_iterativo}.')