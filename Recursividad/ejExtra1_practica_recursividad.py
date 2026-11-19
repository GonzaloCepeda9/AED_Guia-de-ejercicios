# #######################################################################################################################################
# from typing import Any

# # Extra: Implementar una función que permita calcular el factorial de un número entero dado.
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)

# numero = 5
# resultado = factorial(numero)
# print(f'\nFactorial || {numero}! = {resultado}')

# #######################################################################################################################################

# # 1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

# def fibonacci(num):
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibonacci(num-1) + fibonacci (num-2)

# numero = 9
# resultado = fibonacci(numero)
# print(f'\nFibonacci || {numero} = {resultado}')

# #######################################################################################################################################

# # 2. Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado

# def suma_enteros(num):
#     if num == 1:
#         return 1
#     else:
#         return num + suma_enteros(num-1)

# numero = 5
# resultado = suma_enteros(numero)
# print(f'\nSumatoria entre 0 y n || {numero} = {resultado} ')

# #######################################################################################################################################

# # 3. Implementar una función para calcular el producto de dos números enteros dados.

# def producto(num1, num2):
#     if num1 == 0 or num2 == 0:
#         return 0
#     elif num1 == 1:
#         return num2
#     elif num2 == 1:
#         return num1
#     else:
#         return num1 + producto(num1, num2-1)

# numero1 = 6
# numero2 = 3
# resultado = producto(numero1, numero2)
# print(f'\nProducto || {numero1} * {numero2} = {resultado} ')

# #######################################################################################################################################

# # 4. Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.
# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     elif exponente == 1:
#         return base
#     else:
#         return base * potencia(base, exponente-1)

# base = 3
# exponente = 3
# resultado = potencia(base, exponente)
# print(f'\nPotencia || {base} ^ {exponente} = {resultado}')

# #######################################################################################################################################

# # 5. Desarrollar una función que permita convertir un número romano en un número decimal.

# equivalencias = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }

# def romano_a_decimal(romano):
#     if len(romano) == 0:
#         return 0
#     elif len(romano) == 1:
#         return equivalencias[romano]
#     elif equivalencias[romano[-1]] <= equivalencias[romano[-2]]:
#         return romano_a_decimal(romano[:-1]) + equivalencias[romano[-1]]
#     else:
#         return romano_a_decimal(romano[:-2]) + equivalencias[romano[-1]] - equivalencias[romano[-2]]

# romano = 'MDCDXCIV'
# decimal = romano_a_decimal(romano)
# print(f'\nRomano a decimal | {romano} = {decimal}')

# #######################################################################################################################################

# # 6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.

# def invertir_secuencia(secuencia: Any):

#     print(f'\nÚltima letra: {secuencia[-1]}')
#     print(f'Resto secuencia: {secuencia[:-1]}')

#     if len(secuencia) == 1:
#         return secuencia
#     else:
#         return secuencia[-1] + invertir_secuencia(secuencia[:-1])

# palabra = 'Hola'
# palabra_invertida = invertir_secuencia(palabra)
# print(f'Palabra invertida = {palabra_invertida}')

# #######################################################################################################################################

# # 7. Desarrollar un algoritmo que permita calcular serie 1/n (Serie 1/n, donde n=1 hasta N)

# def calcular_serie(num):
#     print(f'Valor de num = {num} ')
#     if num == 1:
#         return 1
#     else: 
#         return 1/num + calcular_serie(num-1)

# num = 9
# resultado = calcular_serie(num)
# print(f'Resultado de la serie 1/{num} = {resultado}')

# #######################################################################################################################################

# # 8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario

# def decimal_a_binario(num):
#     if num == 0 or num == 1:
#         return str(num)
#     else:
#         if num % 2 == 0:
#             return decimal_a_binario(num//2) + str(0)
#         else:
#             return decimal_a_binario(num//2) + str(1)

# numero = 9
# resultado = decimal_a_binario(numero)
# print(f'Número decimal: {numero} | Número binario: {resultado}')

# #######################################################################################################################################

# # 10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

# def contar_digitos(num):
#     if num < 10:
#         return 1
#     else:
#         return 1 + contar_digitos(num//10)

# numero = 951753
# resultado = contar_digitos(numero)
# print(f'Número: {numero} | Dígitos: {resultado}')

# #######################################################################################################################################

# # 11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena. # Rehacer con un acumulador

# def invertir_entero(num: int, acum = 0):
#     if num < 10:
#         return acum * 10 + num
#     else:
#         resto = num % 10
#         acum = acum * 10 + resto
#         return invertir_entero(num//10, acum)

# numero = 27819
# resultado = invertir_entero(numero)
# print(f'Número original: {numero} | Número invertido: {resultado}')

# #######################################################################################################################################

# # 22. El problema de la mochila Jedi.
# '''
# Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos.
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.
# '''

# mochila_Jedi = [
#   'comunicador',
#   'capa',
#   'mapa',
#   'linterna',
#   'cuerda',
#   'piedra',
#   'sable de luz',
#   'par de guantes',
#   'botiquín'
# ]

# print(type(mochila_Jedi))

# '''
# Algoritmo para resolver el problema:
#     Sacar objetos de a uno a la vez y comparar:
#         Si es el sable de luz (caso base) retornar:
#             Mensaje afirmativo
#             Contador de objetos
#         Si no es sable de luz retornar:
#             Mensaje con objeto sacado
#             Llamada a la función recursiva sin el objeto sacado
# '''

# def usar_la_fuerza(mochila_Jedi: list, contador: int = 0, encontrado: bool = False):
#     objeto = mochila_Jedi[-1]
#     if objeto == 'sable de luz':
#         contador = contador + 1
#         encontrado = True
#         print(f'Objeto sacado: {objeto}.')
#         return contador, encontrado
#     else:
#         contador = contador + 1
#         print(f'Objeto sacado: {objeto}.')
#         return usar_la_fuerza(mochila_Jedi[:-1], contador)

# contador, encontrado = usar_la_fuerza(mochila_Jedi)
# if encontrado:
#     print(f'\nEl sable de luz fue encontrado. \nFue necesario sacar {contador} objeto/s hasta encontrarlo.')
# else:
#     print(f'\nEl sable de luz no se encontró en la mochila. \n Se sacaron {contador} objeto/s.')