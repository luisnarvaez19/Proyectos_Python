

def potencia(x, n, y):

    if n == y:
        return 1
    else:
        return x * potencia(x, n+1, y)


def main():
    x = int(input('Introduzca el numero x: '))
    y = int(input('Introduzca el numero y: '))
    print(potencia(x, 0, y))


if __name__ == "__main__":
    main()


'''
    x elevado y 
    
    x * x * x  Y veces
    
    x
    
    x 
    
    
'''