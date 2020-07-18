'''
Created on Sep 8, 2018
    Programa que calcula los numeros primos
@author: luis
'''

for n in range(2, 30):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')