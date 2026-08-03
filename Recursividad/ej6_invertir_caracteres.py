# 6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.

'''
◘ Algoritmo para resolver el problema:
    Capturar el último caracter de la cadena, y devolver los restantes.
'''

def invertir_secuencia(secuencia):
    if secuencia[1:] == '':
        return secuencia
    else:
        return secuencia[-1] + invertir_secuencia(secuencia[:-1])

# Prueba
print('------------------------------------------ Función: Invertir secuencia de caracteres -------------------------------------------')
secuencia = 9631
secuencia = str(secuencia)  # Convierte la secuencia a cadena, para poder utilizar el operador de indexación.
if secuencia[1:] == '':
    print('Debe ingresar una cadena de caracteres.')
else:
    resultado = invertir_secuencia(secuencia)
    print(f'Secuencia dada: {secuencia} | Secuencia invertida: {resultado}')