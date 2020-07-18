'''
    9. Escribir un programa en Python que detecte si se han introducido en orden creciente
     tres números introducidos por el usuario.

'''

x = 5
y = 9
z = 2

if x > y and y  > z:
    print('Si se han introducido en orden creciente')
else:
    print('No se han introducido en orden creciente')



'''
    9. Escribir un programa en Python que ordene 
     dos números introducidos por el usuario.

'''

x = 85
y = 59
temp = 0

if x > y:
    temp = y
    y = x  #  ahora y = 85
    x = temp


print(f'Ordenados en forma creciente, x es: {x}, y es: {y} ')


'''
    9. Escribir un programa en Python que ordene 
     tres números introducidos por el usuario.

'''

x = 5
y = 9
z = 2


print(f'Ordenados en forma creciente,  x es: {x}, y es: {y} y z es: {z}')


x = 85
y = 59
temp = 0

# y = luis    x = pablo  temp = silla intermedia temporal
if x > y : # perfecto
    temp = x
    x = y
    y = temp



print(f'Ordenados en forma creciente,  x es: {x}, y es: {y}' )



x = 85
y = 59
temp = 0


if x > y :
    temp = y
    y = x
    x = temp

print(f'Ordenados en forma creciente,  x es: {x}, y es: {y}' )


x = 85
y = 59
anterior = 0

if x > y :
    anterior = x
    x = y
    y = anterior

print(f'Ordenados en forma creciente,  x es: {x}, y es: {y}' )


x = 85
y = 59
temp = 0

if x > y:
    temp = x
    x = y
    y = temp

print(f'Ordenados en forma creciente,  x es: {x}, y es: {y}' )






