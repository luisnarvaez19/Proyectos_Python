'''
Created on Sep 10, 2018

@author: luis

Sets
    The sets use Brackets
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                 # fast membership testing

print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print('a es: ',a)                                  # unique letters in a
print('b es: ',b)                                  # unique letters in b

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both  union

print(f'interseccion: {a & b}')                              # letters in both a and b  interseccion

print(a ^ b)                              # letters in a or b but not both  o exclusivo

seta = {x for x in 'abracadabra' if x not in 'abc'}

print(seta)
