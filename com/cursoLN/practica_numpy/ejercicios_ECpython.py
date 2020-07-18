# -*- coding: utf-8 -*-
"""
EJERCICIOS NUMPY - ENRIQUE CABEZAS

1.	Escriba un programa usando numpy para generar cinco numeros random de
distribucion normal
2.	Escriba un programa usando numpy para generar 6 numeros enteros del 10 al 30
3.	Escriba un programa usando numpy para encontrar el valor mas frecuente en un arreglo
"""
import numpy as np

a = np.random.rand(5)
print(a)

b = np.linspace(10, 30, 6)
print(b)

x = np.random.randint(low=10, high=30, size=6)
print(x)


arreglo = np.random.randint(0,16,10)
print(arreglo)
print(np.bincount(arreglo).argmax())
# np.bincount
# Count number of occurrences of each value in array of non-negative ints.
