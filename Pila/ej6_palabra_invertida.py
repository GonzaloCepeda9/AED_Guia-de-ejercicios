# 6. Leer una palabra y visualizarla en forma inversa.

from TDA_stack import Stack

stack = Stack()
stack_aux = Stack()

def invertir_palabra(texto):
    for character in texto:
        stack.push(character)

    texto = ""

    while stack.size() > 0:
        texto = texto + stack.pop()

    return texto

#################################################  Ejecución de pruebas del enunciado  #################################################
print('\n--------------------------------- Inversión de una palabra y visualización en forma inversa ----------------------------------')
texto = input('Ingrese una palabra: ')
palabra_invertida = invertir_palabra(texto)

if texto == "":
    print('Debe ingresar al menos un caracter.')
else:
    print(f'\nPalabra ingresada: {texto}')
    print(f'\nPalabra visualizada en forma inversa: {palabra_invertida}')