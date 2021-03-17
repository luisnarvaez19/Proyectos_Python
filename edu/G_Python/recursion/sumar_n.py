

def sumar_n(n):
    if n == 0:
        return 0
    else:
        return n + sumar_n(n-1)

def main():
    n = int(input('Introduzca el numero n: '))
    print(sumar_n(n))


if __name__ == "__main__":
    main()

'''
    3 + 2 + 1
     
    sumar_n(0) = 0
    
    sumar_n(1) = 1 + 0
    
    sumar_n(2) = 2 + sumar_n(1)  (Segunda vez)
    
    sumar_n(2) = 2 + 1 + 0
    
    sumar_n(3) = 3 + sumar_n(2)  (Primera vez)
    
    sumar_n(3) = 3 + 2 + 1 + 0
     
'''