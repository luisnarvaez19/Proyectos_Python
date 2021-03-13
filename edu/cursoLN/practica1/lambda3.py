from combinatoria import combinatoria
from factorial import factorial


def funciones(opcion):
    if opcion==1:
        return lambda x: x**2 + 2*x - 5
    elif opcion==2:
        return lambda x: factorial(x)
    elif opcion==3:
        return lambda n,r: combinatoria(n,r)

# f=opciones(3)
#
# print(f(5,2))
#
# f=opciones(2)
# print(f(5))

print("¿Qué desea hacer?")
print("Pulse 1: Resolver la ecuación: x*x + 2*x - 5")
print("Pulse 2: Realizar el factorial de un numero")
print("Pulse 3: Realizar la combinatorio de n en r")
print("Pulse 4: Salir")
accion = 0
while accion != 4:
    accion = int(input("Elija la opción deseada: "))
    if accion == 1:
        f=funciones(accion)
        print(f(3))

    if accion == 2:
        f = funciones(accion)
        fact=int(input("De que numero quieres el factorial: "))
        print(f(fact))

    if accion == 3:
        f = funciones(accion)
        print(f(5,2))

    if accion == 4:
        print("Adiós, muchas gracias")

    else:
        print("Acción no válida. Elija 1, 2, 3 o 4")
        accion = int(input("Elija la opción deseada: "))