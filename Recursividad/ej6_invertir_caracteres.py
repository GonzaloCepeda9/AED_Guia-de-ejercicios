# 6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.
'''
◘ Algoritmo para resolver el problema:
    Capturar el último carácter de la cadena, y devolver los restantes. Cunado quede uno sólo, devolver ese carácter.
'''

def invertir_secuencia(secuencia):
    if secuencia[1:] == '':
        return secuencia
    else:
        return secuencia[-1] + invertir_secuencia(secuencia[:-1])

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n------------------------------------------ Inversión de una secuencia de caracteres ------------------------------------------')
secuencia = 'Cadena#1994'
secuencia = str(secuencia)  # Convierte la secuencia a cadena, para poder utilizar el operador de indexación.
if secuencia:
    resultado = invertir_secuencia(secuencia)
    print(f'Secuencia dada: {secuencia} | Secuencia invertida: {resultado}')
else:
    print(f'Debe ingresar una cadena de caracteres.')