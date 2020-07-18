'''
Created on Agosto 18, 2019

Escribir un programa en Python que calcule el capital
producido por un capital de 1.000.000 de pesetas, al cabo
de un año depositado a un interés del 2%.

Cf = Ci(1 + r) a la n
 Cf es el capital al final del enésimo período
 Ci es el capital inicial
 r es la tasa de interés expresada en tanto por uno (v.g., 4 % = 0,04)
 n es el número de períodos

@author: luis.
'''
def capital(interes, capitalini) :
   return capitalini*(1+interes/100)

Cf=capital(2,1000000)
print(f"El capital inicial de 1.000.000 de pesetas, se convertira, con un interes de 2% en: {Cf} ")