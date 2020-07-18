# -*- coding: utf-8 -*-
"""
EJERCICIO 3 - LAMBDA EXPRESSION
"""
from lambda1_EC import combinatoria
from lambda1_EC import factorial
from lambda2_EC import ejercicio2


def ejercicio3():
    """
    Haga un programa en Python que según un menu solicitado al usuario,
    resuelva la ecuación del ejercicio 2, el factorial de un numero y
    la combinatoria de n en r.
    Dependiendo de la selección del usuario se devolvera la funcion lambda
    que resuelva el ejercicio.
    """
    print("¿Qué desea hacer?")
    print("Pulse 1: Resolver la ecuación: x*x + 2*x - 5")
    print("Pulse 2: Realizar el factorial de un numero")
    print("Pulse 3: Realizar la combinatorio de n en r")
    print("Pulse 4: Salir")

    accion = 0
    while accion != 4:
        accion = int(input("Elija la opción deseada: "))
        if accion == 1:
            return lambda x: ejercicio2(x)

        if accion == 2:
            return lambda x: factorial(x)

        if accion == 3:
            return lambda n, r: combinatoria(n, r)

        if accion == 4:
            print("Adiós, muchas gracias")

        else:
            print("Acción no válida. Elija 1, 2, 3 o 4")
            accion = int(input("Elija la opción deseada: "))


print(ejercicio3())
