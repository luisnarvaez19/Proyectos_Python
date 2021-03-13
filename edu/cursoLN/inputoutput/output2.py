s = 'Hello, world.'
str(s)

repr(s)

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + str(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
print(hello)
# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))

import math
print(f'The value of pi is approximately {math.pi:.3f}.')