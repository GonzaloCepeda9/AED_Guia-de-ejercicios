# 3. Implementar una función para calcular el producto de dos números enteros dados.

def producto_enteros(num1: int, num2: int):
    if num1 < 0 or num2 < 0 or (num1 - (int(num1))) != 0 or (num2 - (int(num2))) != 0:
        return None
    if num1 == 0 or num2 == 0:
        return 0
    elif num1 == 1:
        return num2
    elif num2 == 1:
        return num1
    else:
        return num1 + producto_enteros(num1, num2 - 1)

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n----------------------------------------- Producto de dos números enteros positivos ------------------------------------------')
factor_1 = 9
factor_2 = 9
resultado = producto_enteros(factor_1, factor_2)
if resultado:
    print(f'{factor_1} * {factor_2} = {resultado}')
else:
    print(f'Debe ingresar números enteros positivos.')