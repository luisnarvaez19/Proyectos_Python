'''
Created on Agosto 18, 2019

Pasaje de parametros y por defecto la lista

@author: luis.
'''

def f(a, L=[]):
    L.append(a)
    return L

print(f(5))
print(f(8))
print(f(25))


# Pasar una lista como parametro