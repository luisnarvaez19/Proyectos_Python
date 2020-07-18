'''
Created on Sep 17, 2018

@author: luis
'''

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise