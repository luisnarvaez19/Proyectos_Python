'''
Created on Sep 10, 2018

@author: luis

Conditions

'''

#  It is possible to assign the result of a comparison or other Boolean expression to a variable. 

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3]< [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)< (1, 2, 4))
print((1, 2)< (1, 2, -1))
print((1, 2, 3)== (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))< (1, 2, ('abc', 'a'), 4))