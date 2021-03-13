'''
Created on Agosto 18, 2019

Ejercicios varios de cadenas

@author: luis.
'''
var1 = 'Hello World!'
var2 = "cursoLN programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
print ("Updated String :- ", var1[:6] + 'Python')

print(var2.upper())
print(var2.title())
number = "5"
letters = "abcdef"

print(number.isnumeric())
print(letters.isnumeric())

print(len(letters))

print(letters * 2)

name = "Eric"
mensaje="Hello, %s." % name
print(mensaje)

age = 74
mensaje="Hello, %s. You are %s." % (name, age)
print(mensaje)

print("Otra forma: Hello, {}. You are {}.".format(name, age))

print("Ref index. Hello, {1}. You are {0}.".format(age, name))

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))

print("Con **. Hello, {name}. You are {age}.".format(**person))

# f-Strings: A New and Improved Way to Format Strings in Python

print(f"Con f-strings. Hello, {name}. You are {age}.")

print(f"{2 * 37}")

def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
print(f"Llamo a funcion. {to_lowercase(name)} is funny.")

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)

# Comparando las velocidades de las 3 formas

import timeit
print("Primera forma: ",timeit.timeit("""name = "Eric"
age = 74
'%s is %s.' % (name, age)""", number = 10000))

print("Segunda forma: ",timeit.timeit("""name = "Eric"
age = 74
'{} is {}.' .format(name, age)""", number = 10000))

print("Tercera forma: ",timeit.timeit("""name = "Eric"
age = 74
f'(name, age).'""", number = 10000))

