'''
Created on Agosto 18, 2019

@author: luis

Escribir un programa en Python que calcula el equivalente en grados Fahrenheit o Celsius
de temperaturas dadas

'''
def convertTemp(t,opc):
    '''

    :param t: temperatura a pasar
    :param opc: 1. C a F  2. F a C
    :return:  devuelve la temperatura convertida
    '''
    if opc == 1:
        conversion = (t * 9) / 5 + 32
    else :
        conversion = ((t - 32) * 5) / 9
    return conversion

def main():
    while True:
        print("""Seleccione que quiere transformar:
           1. Celsius a Fahrenheit
           2. Fahrenheit a Celsius
           3. Salir
        """)
        opcion = int(input('Presione su opcion: '))
        if opcion != 1 and opcion!=2 and opcion!=3 :
            print(f"Presiono una opcion invalida: {opcion}, intente de nuevo...")
        if opcion == 3:
            break
        else :
            temp = float(input("Indique la temperatura a pasar: "))
            resultado=convertTemp(temp, opcion)
            if opcion==1 :
                conv1 = "Celsius"
                conv2 = "Fahrenheit"
            else :
                conv2 = "Celsius"
                conv1 = "Fahrenheit"
            print(f"La temperatura en {conv1}: {temp}, en {conv2} es: {round(resultado,2)} ")

if __name__ == "__main__":
    main()