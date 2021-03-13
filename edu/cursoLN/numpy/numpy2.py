"""
        Array vs Numpy array Ndarray
"""
import numpy as np
a = np.array([2,3,4])
print(a)
print(a.dtype)

b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

c = np.zeros((3,4))  # tambien np.ones
print(c)

d = np.arange(10, 30, 5)
print(d)

e = np.arange(0, 2, 0.3)            # it accepts float arguments
print(e)

a = np.arange(6)                         # 1d array
print(a)

b = np.arange(12).reshape(4,3)           # 2d array
print(b)

c = np.arange(24).reshape(2,3,4)         # 3d array
print(c)

print(np.arange(10000).reshape(100, 100))


