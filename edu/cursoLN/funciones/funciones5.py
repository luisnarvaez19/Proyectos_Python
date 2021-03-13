'''
Created on Agosto 18, 2019

Lambda expresions: devolviendo una funcion

@author: luis.
'''
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))

