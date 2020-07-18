from factorial import factorial

def combinatoria(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

#print(combinatoria(5,2))
