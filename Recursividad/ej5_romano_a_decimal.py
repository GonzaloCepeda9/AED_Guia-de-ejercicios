# 5. Desarrollar una función que permita convertir un número romano en un número decimal.

'''
◘ Algoritmo para resolver el problema:
    CASO IDEAL (números válidos):
    - Si el caracter en posición 0 es menor que el caracter en posición 1, restar caracter 0 a caracter 1. Devolver cadena sin ambos valores (desde posición 2 hasta el final).
    - Si no, sumar caracter 0; y devolver cadena sin el primero (desde posición 1 hasta el final).
    CASOS PARTICULARES (excepciones):
    - Si el número ingresado no es un número romano, devolver mensaje de error.
    - Si el número ingresado tiene sólo 1 caracter válido, devolver directamente la equivalencia del número.
'''

equivalencias = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def conversion(romano: str):
    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return equivalencias[romano[0]]
    elif len(romano) > 1:
        if (equivalencias[romano[0]] < equivalencias[romano[1]]):
            return equivalencias[romano[1]] - equivalencias[romano[0]] + conversion(romano[2:])
        else:
            return equivalencias[romano[0]] + conversion(romano[1:])

def romano_a_decimal(num_romano: str):
    romano = str(num_romano)
    if len(romano) == 0:
        return 'Debe escribir un número romano.'
    for i in range(len(romano)):
        if romano[i] not in equivalencias:
            return 'No es un número romano válido.'
    return conversion(romano)
    
# Prueba
print('------------------------------------------ Función: Convertir número romano a decimal ------------------------------------------')
num_romano = 'MCMXCIV'
resultado = romano_a_decimal(num_romano)
print(resultado)