def fibonacci(n):
    if n == 0:
        print("0")
    if n == 1:
        print("1") 1
    else:
        return n+fibonacci(n-1)

print(fibonacci(5))