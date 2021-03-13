
num = int(input('Introduzca el numero para calcular el factorial:'))
resultado = 1
for i in range(1, num+1):
    resultado = resultado * i
print(f'El factorial de {num} es: {resultado}')

proximo = num * 2

resultado = 1
for i in range(1, proximo+1):
    resultado = resultado * i
print(f'El factorial de {proximo} es: {resultado}')

proximo3 = num * 3

resultado = 1
for i in range(1, proximo3+1):
    resultado = resultado * i
print(f'El factorial de {proximo3} es: {resultado}')

