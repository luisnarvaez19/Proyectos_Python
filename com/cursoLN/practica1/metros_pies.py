'''
Created on Agosto 18, 2019

Escribir un programa en Python que calcule el equivalente en pies de una longitud de x metros.
1 metro -------------39.27 pulgadas
12 pulgadas --------1 pie

@author: luis.
'''
def metros_pies(longmts) :
    return (longmts*39.3701/12)

longtransf=float(input("Introduzca la longitud a convertir: "))
print(f"La longitud {longtransf} en metros son: {round(metros_pies(longtransf),2)} pies")