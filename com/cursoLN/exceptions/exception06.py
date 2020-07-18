'''
Created on Sep 17, 2018

@author: luis
'''

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
    