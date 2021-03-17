
def entre(a, n):
    if n == a + 1:
        print(n)
    else:
        print(n)
        entre(a, n - 1)

def main():
    a = int(input('Introduzca el numero a: '))
    d = int(input('Introduzca el numero d: '))
    print(entre(a, d - 1))


if __name__ == "__main__":
    main()
