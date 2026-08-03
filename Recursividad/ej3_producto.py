# 3. Implementar una función para calcular el producto de dos números enteros dados.

def producto_enteros(num1: int, num2: int):
    if num1 < 0 or num2 < 0:
        return 'Los números deben ser positivos.'
    elif num1 or num2 == 0:
        return 0
    elif num1 == 1:
        return num2
    elif num2 == 1:
        return num1
    else:
        return num1 + producto_enteros(num1, num2 - 1)

# Prueba
print('-------------------------------------- Función: Producto de dos números enteros positivos --------------------------------------')
factor_1 = 9
factor_2 = 9
resultado = producto_enteros(factor_1, factor_2)
print(f'El producto entre {factor_1} y {factor_2} es {resultado}')
# print(f'{factor_1} * {factor_2} = {resultado}')