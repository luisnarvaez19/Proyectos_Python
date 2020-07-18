'''
Created on Agosto 18, 2019

Escribir un programa en Python que sume, reste, multiplique y divida dos números:

@author: luis.
'''
# Para numeros enteros

num1=int(input('Introduzca el primer numero: '))
num2=int(input('Introduzca el segundo numero: '))
print('La suma es: ', num1+num2)
print('Su producto es: ', num1*num2)
print('La division es: ', num1/num2)
print('El resto de la division o modulo es : ', num1%num2)


# Para numeros decimales

num1=float(input('Introduzca el primer numero: '))
num2=float(input('Introduzca el segundo numero: '))
print('La suma es: ', num1+num2)
print('Su producto es: ', num1*num2)
print('La division es: ', num1/num2)
print('El resto de la division o modulo es : ', num1%num2)


# Para String o cadenas

nombre = input("Dígame su nombre: ")
# apellido = input(f"Dígame su apellido, {nombre}: ")
apellido = input(f"Dígame su apellido, "+nombre + ": ")
print(f"Me alegro de conocerle, {nombre} {apellido}.")


# Leer los dos numeros enteros de una vez

num1, num2 = [int(x) for x in input("Introduzca dos numeros: ").split()]
print('La suma es: ', num1+num2)
print('Su producto es: ', num1*num2)
print('La division es: ', num1/num2)
print('El resto de la division o modulo es : ', num1%num2)

