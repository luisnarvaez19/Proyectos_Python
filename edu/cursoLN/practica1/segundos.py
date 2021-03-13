'''
Created on Agosto 18, 2019

Escribir un programa en Python que calcule el número de horas, minutos y segundos que hay en x segundos

@author: luis.
'''
segundos=int(input("Introduzca la cantidad en segundos: "))
horas=segundos // 3600
horas_resto= segundos % 3600
minutos = horas_resto // 60
minutos_resto = horas_resto % 60
print(f"En {segundos} segundos hay: {horas} horas, {minutos} minutos y {minutos_resto} segundos ")