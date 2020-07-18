'''
Created on Sep 8, 2018
Modified on Mar 31, 2020
@author: luis
Matrices

'''

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns:

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print('Primera forma')
print(transposed)



transposed=[[row[i] for row in matrix] for i in range(4)]

print('Segunda forma')
print(transposed)


transposed=list(zip(*matrix))

print('Tercera forma')
print(transposed)


