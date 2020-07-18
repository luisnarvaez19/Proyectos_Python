# -*- coding: utf-8 -*-
"""
EJERCICIO 1 CLASE 2
PROFESOR: LUIS NARVÁEZ
ALUMNO: ENRIQUE CABEZAS
"""

# Factorial iterativo
def factorial(x):
    if x == 0:
        return 1
    else:
        acumulador = 1
        for i in range(1, x + 1):  # Desde 1 hasta x
            acumulador *= i
        return acumulador


def funcion1():
    n = int(input("Introduzca un número entero n: "))
    r = int(input("Introduzca otro número entero r: "))
    funcion = factorial(n) / (factorial(r) * factorial(n - r))
    print(funcion)


print(funcion1())
