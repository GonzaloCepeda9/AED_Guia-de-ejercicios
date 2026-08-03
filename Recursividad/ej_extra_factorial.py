# Extra: Función factorial

print("--------- Función factorial recursiva ---------")   

def factorial(n):
    if n < 0:
        return "El número debe ser positivo."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

resultado1 = factorial(-1)
resultado2 = factorial(1)
resultado3 = factorial(3)
resultado4 = factorial(5)
resultado5 = factorial(7)
resultado6 = factorial(9)

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)

print("--------- Función factorial iterativa ---------")

def factorial_iterativa(num):
    acumulador = 1
    while num > 0:
        acumulador = acumulador * num
        num -= 1
    return acumulador

resultado1 = factorial_iterativa(-1)
resultado2 = factorial_iterativa(1)
resultado3 = factorial_iterativa(3)
resultado4 = factorial_iterativa(5)
resultado5 = factorial_iterativa(7)
resultado6 = factorial_iterativa(9)

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)