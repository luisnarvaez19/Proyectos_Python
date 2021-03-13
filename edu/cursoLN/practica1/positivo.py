'''
Created on Agosto 18, 2019

Escribir un programa en Python que detecte si un número introducido desde el teclado es positivo o negativo.

@author: luis.
'''
from celsius_fahrenheit import convertTemp

num=int(input('Introduzca un numero: '))
if num < 0:
    print('El numero es negativo')
elif num == 0:
    print('El numero es 0')
else :
    print('El numero es positivo')
print(f"La conversion es: {convertTemp(-273.15,1)}")
