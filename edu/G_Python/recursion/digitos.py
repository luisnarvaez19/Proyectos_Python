

def digitos(n):

    if n < 10:
        return 1
    else:
        return 1 + digitos(n/10)


def main():
    n = int(input('Introduzca el numero n: '))
    print(digitos(n))


if __name__ == "__main__":
    main()


'''
      1234
      4 digitos
      
      123
      
      12
      
      1
'''