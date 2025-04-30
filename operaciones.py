import random

def sumar(a,b):
    return a + b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b == 0:
        return 'No es posible dividir por cero'
    return a/b

def random_1 (a,b):
    if a < 0:
        return 'la variable a no puede ser menor que cero'
    if a >= b:
        return 'la variable a no puede ser mayor o igual a b'
    return random.randint(a,b)