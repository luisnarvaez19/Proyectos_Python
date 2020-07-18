# -*- coding: utf-8 -*-
"""
EJERCICIO 2 - LAMBDA EXPRESSION
"""
def ejercicio2():
    """
    2.	Haga una funcion lambda en Python que resuelva la ecuacion x*x + 2*x - 5
    Pruebela con los valores f(4) y f(5)

    """
    return lambda x : x*x + 2*x - 5

f = ejercicio2()

print(f(4))
print(f(5))