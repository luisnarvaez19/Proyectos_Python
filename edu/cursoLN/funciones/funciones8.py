'''
Created on Agosto 18, 2019

Lambda expresions: devolviendo una funcion

@author: luis.
'''
def argumentos() :
    return lambda *args: sum(args)

def my_func(*args):
    return reduce((lambda x, y: x + y), args)

varios=my_func()

print(varios(3, 4, 5))



