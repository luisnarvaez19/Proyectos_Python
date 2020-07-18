# Serie de Fibonacci
# El elemento i es la suma de los dos anteriores
#  1. La var del ciclo tiene que tener valor inicial
#  2. La var del ciclo tiene que modificarse dentro del ciclo
#  3. Tiene que haber una expresion condicional en el ciclo
#  4.
#
a, b = 0, 1
while a < 100:
	# print(a)
	print(a, end=',')
	a, b = b, a+b
