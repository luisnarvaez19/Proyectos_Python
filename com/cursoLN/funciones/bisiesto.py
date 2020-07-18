def bisiesto(anio):
    if anio % 4 == 0:
        print('Es bisiesto')
    else:
        if ((anio % 100) == 0) and ((anio % 400) == 0):
            print('Es bisiesto')
        else:
            print('NO es bisiesto')
    print(anio)

year=int(input('Introduzca el año a comprobar:'))
bisiesto(year)

