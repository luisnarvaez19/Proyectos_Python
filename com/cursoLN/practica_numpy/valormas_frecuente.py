"""
       Escriba un programa usando numpy para encontrar el valor mas frecuente en un arreglo
"""
import numpy as np
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())
