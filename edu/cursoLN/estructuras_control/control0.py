from edu.cursoLN.funciones.funciones4 import var_global

print(var_global)

x = int(input("Please enter an integer: "))
#  IF:   La instruccion condicional
if x < 0:
    print('El numero es negativo')
elif x == 0:
    print('El numero es 0')
else:
    print('El numero es positivo')
