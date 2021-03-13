import numpy as np
# The floor of the scalar x is the largest integer i, such that i <= x
#  NumPy instead uses the definition of floor where floor(-2.5) == -3
a = np.floor(10*np.random.random((3,4)))
print(a)

print(a.shape)

print(a.ravel())

"""
The reshape() function is used to give a new shape to an array without 
changing its data. The new shape should be compatible with the original
shape. If an integer, then the result will be a 1-D array of that length.
"""
b=a.reshape(6,2)
print(b)

print(a.T)

print(a.T.shape)

print(a)
a.resize((2,6))

print(a)
