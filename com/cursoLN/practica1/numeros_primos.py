'''
Created on Agosto 18, 2019

Escribir un programa en Python que detecte si un número introducido desde el teclado es primo.

@author: luis.
'''
def primos(n):
    '''
    Funcion que calcula si un numero es primo o no
    :param n: El numero primo a determinar
    :return:
    '''
    if (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0):
        return f"El numero {n} no es un número primo"
    for i in range(6, n):  # Rango de 1 hasta (n-1)
        if n % i == 0:
            return (f"El numero {n} no es un número primo")
    return (f"El numero {n} es un número primo")

print(primos(169))

help(primos)

