# -*- coding: utf-8 -*-
"""
EJERCICIO 3 - CLASE 2 - LUIS NARVÁEZ
"""


def factorial(x):
    if x == 0:
        return 1
    else:
        acumulador = 1
        for i in range(1, x + 1):  # Desde 1 hasta x
            acumulador *= i
        return acumulador


def series():
    n = int(input("Introduzca un número entero: "))

    print("Sumatorio: Pulse 1")
    print("Sumatorio factorial: Pulse 2")
    print("Sumatorio de cuadrados: Pulse 3")
    print("Si desea salir: Pulse 4")

    accion = int(input("¿Qué operación desea realizar?: "))

    while accion != 4:
        resultado = 0
        if accion == 1:
            for i in range(n + 1):
                resultado += i
            print(resultado)

        elif accion == 2:
            for i in range(n + 1):
                resultado += factorial(i)
            print(resultado)

        elif accion == 3:
            for i in range(n + 1):
                resultado += i ** 2
            print(resultado)

        elif accion == 4:
            print("Adiós, muchas gracias")

        else:
            print("Opción no válida, pulse 1, 2, 3 ó 4")

        accion = int(input("¿Qué operación desea realizar?: "))

series()
