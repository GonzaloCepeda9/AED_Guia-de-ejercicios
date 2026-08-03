# 5. Determinar si una cadena de caracteres es un palíndromo.
'''
Definición:
    Una cadena de caracteres es palíndroma si la sucesión de sus caracteres coincide exactamente con su inversa, considerando cada carácter en su valor literal (mayúsculas, minúsculas, espacios y signos, son distintos entre sí).

Adaptación para el ejercicio:
    El concepto fue adaptado para que sea insensible a mayúsculas e ignore los espacios. Así, solo se compara letras significativas, lo que permite reconocer palíndromos frasales sin que los espacios ni el caso interfieran en la comparación con la pila.
'''

from TDA_stack import Stack

def palindromo(cadena: str):
    stack = Stack()
    cadena_normalizada = cadena.lower().replace(" ", "")
    for character in cadena_normalizada:
        stack.push(character)

    for caracter in cadena_normalizada:
        if caracter != stack.pop():
            return False
        else:
            return True

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n--------------------------------------------- Determinación de cadena palíndroma ---------------------------------------------')
cadena = input(f'Ingrese una cadena de caracteres: ') 
resultado = palindromo(cadena)
if resultado:
    print(f'La cadena de caracteres "{cadena}" es palíndroma.')
else:
    print(f'La cadena de caracteres "{cadena}" no es palíndroma.')