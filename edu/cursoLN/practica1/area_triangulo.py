'''
Created on Agosto 18, 2019

Escribir un programa en Python que calcule el área de un triángulo

@author: luis.
'''
base, altura = [int(x) for x in input("Introduzca la base y la altura: ").split()]
print("El area del triangulo: ", base * altura)