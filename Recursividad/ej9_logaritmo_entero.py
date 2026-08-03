# 9. Implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que: log_b (n/b) = log_b n - log_b b

def logaritmo_entero(base, num):
    print(f'Dividiendo {num} entre {base}')
    if num < base:
        return 0
    else:
        return 1 + logaritmo_entero(base, num // base)
    
# Prueba
print('--------------------------------------------- Función: Calcular logaritmo entero -----------------------------------------------')
base = 2
num = 256
if base < 2:
    print('La base debe ser un entero mayor que 1.')
else:
    resultado = logaritmo_entero(base, num)
    print(f'El logaritmo en base {base} de {num} es {resultado} | log_{base} ({num}) = {resultado}')