

def factorial_calc(num):
    '''
       Funcion que calcula el numero factorial com2
    '''
    resultado = 1
    for i in range(1, num + 1):
        resultado = resultado * i
    return resultado


num = int(input('Introduzca el numero para calcular el factorial: '))
print(f'El factorial de {num} es: {factorial_calc(num)}')

proximo = num * 2
print(f'El factorial de {proximo} es: {factorial_calc(proximo)}')

proximo3 = num * 3
print(f'El factorial de {proximo3} es: {factorial_calc(proximo3)}')
