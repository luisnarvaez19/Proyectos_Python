'''
Created on Sep 10, 2018
@author: luis
Tuplas
'''

txt='Hola mi nombre es Pablo'

t = 12345, 54321, 'hello!'
print(t[0])

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
# t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
