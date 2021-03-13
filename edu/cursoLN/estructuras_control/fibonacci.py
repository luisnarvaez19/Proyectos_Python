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


'''
In a, b = b, a + b, the expressions on the right hand side are evaluated before being assigned to the left hand side. So it is equivalent to:

c = a + b
a = b
b = c

is closer to:

temp_a = a
a = b
b = temp_a + b

a = 0  b = 1
0 ,  1 , 1, 2
a = 1  b = 1
a = 1  b = 2
a = 2  b = 3
a = 3  b = 5
'''