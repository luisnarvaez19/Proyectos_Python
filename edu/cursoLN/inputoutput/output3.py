table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')



'''
Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(),
 and '!r' applies repr():
'''
animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals !r}.')
