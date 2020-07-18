'''
Created on Sep 8, 2018
Modified on Mar 31, 2020
@author: luis
List Comprehensions

'''

#  Crear una lista con los cuadrados de los 10 primeros numeros

squares = []
for x in range(10):
    squares.append(x**2)

print('Primera forma')
print(squares)

squares = []

squares = list(map(lambda x: x**2, range(10)))

print('Segunda forma')
print(squares)

squares = []

squares = [x**2 for x in range(10)]

print('Tercera forma')
print(squares)

