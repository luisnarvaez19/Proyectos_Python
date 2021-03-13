'''
     Estructuras de datos

     Lists
'''

cuadrados = [1, 4, 9, 16, 25]

print(cuadrados)

print(cuadrados[0])

print(cuadrados[-2])

print(cuadrados[-3:])

cuadrados += [36, 49, 64, 81, 100]

print(cuadrados)

cubos = [1, 8, 27, 65, 125]

# Lists son mutables

cubos[3] = 64

print(cubos)

cubos.append(216)

cubos.append(7 ** 3)

print(cubos)

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letras[2:5] = ['C', 'D', 'E']

print(letras)

letras[2:5] = []

print(letras)

letras[:] = []

print(letras)

a = ['a', 'b', 'c']

n = [1, 2, 3]

x = [a, n]

print(x)

print(x[0])

print(x[0][1])

nueva = [5, 'Luis', [2, 3], 'ramon']