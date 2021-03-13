'''
Created on Agosto 18, 2019

Pasaje de parametros y por defecto la lista en None

@author: luis.
'''

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(32))
p = [15, 200]
print(f(3, p))
