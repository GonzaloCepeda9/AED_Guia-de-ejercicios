# 2. Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado

def suma_enteros(num: int):
    if num < 0 or num - (int(num)) != 0:
        return None
    elif num == 0:
        return 0
    else:
        return num + suma_enteros(num - 1)

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n-------------------------------------------------- Suma de números enteros ---------------------------------------------------')
num_prueba = 6
resultado = suma_enteros(num_prueba)
if resultado:
    print(f'La suma de los números enteros comprendidos entre 0 y {num_prueba} es igual a {resultado}.')
else:
    print(f'Debe ingresar un número entero positivo.')