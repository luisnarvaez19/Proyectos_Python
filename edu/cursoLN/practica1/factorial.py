def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

#  print(factorial(5))