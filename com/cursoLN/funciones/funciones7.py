'''
Created on Agosto 18, 2019

Lambda expresions: devolviendo una funcion

@author: luis.
'''

def par_impar():
    return lambda x: (x % 2 and 'odd' or 'even')

f = par_impar()
print(f(23))

#  Calcular el cubo  de un número con lamba expresions