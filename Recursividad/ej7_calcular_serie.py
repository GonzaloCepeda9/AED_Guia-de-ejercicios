# 7. Desarrollar un algoritmo que permita calcular serie 1/n

'''
◘ Algoritmo para resolver el problema:
    Dado un número x, hacer la sumatoria desde 1 hasta 1 sobre si mismo.
'''

def calcular_serie(num: int):
    if num == 1:
        return 1
    else:
        return 1/num + calcular_serie(num - 1)
    
# Prueba
print('-------------------------------------------- Función: Calcular serie numérica 1/n ----------------------------------------------')
numero_dado = 5
if numero_dado == 0:
    print('No se puede dividir entre cero.')
elif numero_dado < 0:
    print('Debe ingresar un número positivo.')
else:
    resultado = calcular_serie(numero_dado)
    print(f'El resultado de la serie 1/{numero_dado} es: {resultado}.')