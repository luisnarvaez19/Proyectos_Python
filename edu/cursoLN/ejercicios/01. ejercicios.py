'''
Escribir un programa en Python que detecte si un número introducido desde el teclado es positivo o negativo.


i = 0
n = int( input( "Introduce un número: " ) )
if n >= 0:
    print(f'El número {n} es positivo')
else:
    print(f'El número {n} es negativo')

print('Fin de programa.')
'''
'''
Escribir un programa en Python que sume, reste, multiplique y divida dos números:
x = 10 y = 2


x = 10
y = 2
print(x+y, x-y, x*y, x/y )
'''


'''
Escribir un programa en Python que calcule el área de un triángulo:
base = 7    
altura = 4        
área del triángulo = (base * altura)/2

base = 7
altura = 4
area_triángulo = (base * altura)/2
print(f' El área del triángulo es {area_triángulo}')
'''

'''
Escribir un programa en Python que calcula el equivalente en grados Fahrenheit o Celsius de las siguientes temperaturas
°F = (9/5) * °C + 32

c = int(input('Escribe la cantidad de grados Celsius a convertir: '))
f = (9/5) * c + 32
print(f'{c} grados Celsius equivalen a {f} grados Farenheit'  )
'''

'''     OOOOOOOOOOOOOOOOOOOOOOOJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
Escribir un programa que lea dos números enteros A y B, y obtenga los valores A div B  (A division entera B),   A mod B (A modulo B).


a = int( input( 'Introduce un número entero: ' ) )
b = int( input( 'Introduce otro número entero: ' ) )
#c = a / b
c = a // b    #  Division entera
d = a % b
print(f'A entre B es igual a {c}')
print(f'A modulo B es igual a {d}')

'''

'''    OOOOOOOOOOOOOOOOOOOOOOOJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
Escribir un programa en Python que calcule el número de horas, minutos y segundos que hay en x segundos.
1 hora = 60 minutos = 3600 segundos.
1 minuto = 60 segundos. 1 hora = 60 minutos.    


x = 1
cantidad = int(input('Escribe los segundos que quieres calcular: '))
minutos = 60/cantidad
hora = 3600/cantidad
print(f'{cantidad} segundo/s equivalen a {minutos} Minutos y {hora} horas')
'''


'''    
Escribir un programa en Python que calcule el capital producido por un capital de 1.000.000 de pesetas, al cabo de un año depositado a un interés del 2%.
C= (i* 100)/r*t
'''
'''
1.000.000 = 100%
interés 2%

c = (2*1000000)/100
print(c + 1000000 )
'''

'''   OOOOOOOOOOOOOOOOOOOOOOOJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
Escribir un programa en Python que calcule el equivalente en pies de una longitud de x metros.
1 metro  -------------- 39.27 pulgadas
12 pulgadas ----------- 1 pie


opcion = int(input('Escribe una longitud en metros: '))
m = 39.27
pie = opcion*39.27*12
print(f'{pie} pies.')

'''

'''
Escribir un programa en Python que muestre un mensaje afirmativo si el numero introducido es múltiplo de 5.


num = int(input('Introduce un número: '))
if num %5 == 0:
    print(f'el numero {num} es multiplo de 5')
else:
    print(f'el numero {num} NO es multiplo de 5')

'''

'''   OOOOOOOOOOOOOOOOOOOOOOOJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
Indica cuántos números de la lista son mayores que 5. Deberás obtener a la salida lo siguiente: 7


numeros = [1, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7]
for i in numeros:
    if i > 5:
        i == True:
    elif i < 5:
        i == False:
print(i)
print('fin de programa')

'''


