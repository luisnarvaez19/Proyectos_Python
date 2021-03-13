def fib(n=5):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    print('Entre por aqui funcion')
    print(f'En la funcion:  {mepuedenver}')
    a, b = 0, 1
    contador = 0
    while contador < n:
        print(a, end=' ')
        a, b = b, a+b
        contador += 1  # contador = contador + 1
    print('\n')
# FIn de funcion Fibonacci



# Now call the function we just defined:
print('Entre por aqui principal')
# print(contador)
mepuedenver="Hola Enrique"
print(f'En principal:  {mepuedenver}')
fib(10)

f = fib
f(20)
print('Fin')
help(fib)
