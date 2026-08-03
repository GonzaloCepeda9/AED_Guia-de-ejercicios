# 2. Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado

def suma_enteros(num: int):
    if num < 0:
        return 'El número debe ser un entero positivo.'
    elif num == 0:
        return 0
    else:
        return num + suma_enteros(num - 1)

# Prueba
print('----------------------------------------------- Función: Suma de números enteros -----------------------------------------------')
num_prueba = 6
resultado = suma_enteros(num_prueba)
print(f'La suma de los números enteros comprendidos entre 0 y {num_prueba} es {resultado}')