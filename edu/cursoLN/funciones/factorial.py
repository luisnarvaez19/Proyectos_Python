
# num=int(input('Introduzca el numero para calcular el factorial:'))
# resultado = 1
# for i in range(1, num+1):
#     resultado = resultado * i
# print(f'El factorial de {num} es: {resultado}')
import inspect
from optparse import OptionParser


def factorial_calc(num):
    '''
       Funcion que calcula el numero factorial com2
    '''
    resultado = 1
    for i in range(1, num + 1):
        resultado = resultado * i
    return resultado

def fibonacci(elemento):
    '''
        Calcula la serie de fibonacci, hasta el elemento i de la serie dado como parametro
    :param elemento:
    :return:
    '''


num=int(input('Introduzca el numero para calcular el factorial:'))
print(f'El factorial de {num} es: {factorial_calc(num)}')

print (factorial_calc.__doc__)
all_functions = inspect.getmembers(OptionParser, predicate=inspect.isroutine)
print(all_functions)

#method_list = [func for func in dir(factorial) if callable(getattr(factorial, func))]
# method_list = [func for func in dir(factorial) if callable(getattr(factorial, func)) and not func.startswith("__")]
# method_list = [func[0] for func in inspect.getmembers(factorial, predicate=inspect.isroutine) if callable(getattr(factorial, func[0]))]
# print(method_list)
# help(factorial(5))

# print([ m for m in dir(factorial) if not m.startswith('__')])
