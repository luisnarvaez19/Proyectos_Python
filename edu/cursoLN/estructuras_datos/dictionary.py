'''
Created on Sep 10, 2018
Modified on Mar 31, 2020
@author: luis

Dictionary
'''

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

lista=list(tel) # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary
print(lista)

sorted(tel)
print(tel)

print('guido' in tel)

print('jack' not in tel)

# Formas de crear un diccionario

diccio=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print(diccio)

diccio={x: x**2 for x in (2, 4, 6)}

print(diccio)

diccio= dict(sape=4139, guido=4127, jack=4098)

print(diccio)


