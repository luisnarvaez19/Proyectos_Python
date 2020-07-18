'''
Created on Sep 8, 2018
Modified on Mar 31, 2020
@author: luis
List Comprehensions

'''

#  Cree una lista con el numero pi en donde el primero tenga un decimal de pi, el segundo dos decimales

from math import pi

lista=[str(round(pi, i)) for i in range(1, 6)]

print(lista)
