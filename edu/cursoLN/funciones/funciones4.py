'''
Created on Agosto 18, 2019

Imprime un rango de valores y *args como argumento

@author: luis.
'''
print(list(range(3, 6)))            # normal call with separate arguments

args = [3, 6]
print(list(range(*args)))            # call with arguments unpacked from a list

var_global = "cualquiera"

# Hacer multiplicacion de multiples numeros

def multiplicar(*args):
    resultado=1
    for i in args:
       resultado *= i
    return resultado

print(multiplicar(5,15,2,1))


# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


print(myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks'))


# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFun(**kwargs):
    for key, value in kwargs.items():
        #print("%s == %s" % (key, value))
        print(f"{key} == {value}")

    # Driver code


print(myFun(first='Geeks', mid='for', last='Geeks'))