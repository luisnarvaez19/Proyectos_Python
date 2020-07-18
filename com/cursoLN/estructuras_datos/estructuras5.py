'''
Created on Sep 8, 2018
Modified on Mar 31, 2020
@author: luis
List Comprehensions

'''

# Dadas dos listas: Cree todas las combinaciones de parejas en las que los numeros x y y no se repitan


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print('Primera forma')
print(combs)



combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print('Segunda forma')
print(combs)



