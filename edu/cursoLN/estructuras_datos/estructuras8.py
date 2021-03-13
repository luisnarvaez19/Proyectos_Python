'''
Created on Sep 10, 2018
Modified on Mar 31, 2020
@author: luis
'''

a = [-1, 1, 66.25, 333, 'carro', 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)