# 4. Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.

def potencia_enteros(base: int, exp: int):
    if exp < 0:
        return 'El exponente debe ser un número positivo.'
    elif exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * potencia_enteros(base, exp - 1)

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n---------------------------------------------- Potencia de dos números enteros -----------------------------------------------')
base_prueba = 2
exp_prueba = 9
resultado = potencia_enteros(base_prueba, exp_prueba)
if exp_prueba < 0:
    print(resultado)
else:
    print(f'El número {base_prueba} elevado a la {exp_prueba}ª potencia da como resultado {resultado}.')
    # print(f'{base_prueba} ^ {exp_prueba} = {resultado}')