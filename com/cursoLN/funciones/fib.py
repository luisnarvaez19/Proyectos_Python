def fib(n=5):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    print('Entre por aqui funcion')
    print(mepuedenver)
    a, b = 0, 1
    contador = 0
    while contador < n:
        print(a, end=' ')
        a, b = b, a+b
        contador += 1  # contador = contador + 1

# Now call the function we just defined:
print('Entre por aqui principal')
# print(contador)
mepuedenver="Hola Enrique"
print(mepuedenver)
fib(10)

fib

f = fib
f(20)
print('Fin')
help(fib)
