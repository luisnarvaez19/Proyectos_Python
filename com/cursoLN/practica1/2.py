
def factorial(n,resultado=1):
    if (n==1):
        return(resultado)
    else:
        resultado=n*n-1
        return(factorial(n-1,resultado))

print(factorial(3,1))