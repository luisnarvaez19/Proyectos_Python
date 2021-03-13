"""
     Operaciones basicas
"""
import numpy as np

a = np.array( [20,30,40,50] )
print(a)
b = np.arange( 4 )
print(f'El arreglo b es: {b}')

c = a-b
print(c)

print(b**2)

print(10*np.sin(a))

print(a<35)

a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a *= 3
print(a)


b += a
print(b)


#a += b                  # b is not automatically converted to integer type

B = np.arange(3)
print(B)
print(np.exp(B))

print(np.sqrt(B))

C = np.array([2., -1., 4.])
print(C)
print(np.add(B, C))
print(np.append(B,C))


