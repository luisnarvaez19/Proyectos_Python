

def suma_param(*numeros):
    '''
       Funcion que suma varios numeros
    '''
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado


print(f'La suma de los numeros es: {suma_param(5,4)}')

print(f'La suma de los numeros es: {suma_param(5,2,3,10)}')

