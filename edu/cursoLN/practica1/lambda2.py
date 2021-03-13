"""
  Haga una funcion lambda en cursoLN que resuelva la ecuacion x*x + 2*x - 5
  Pruebela con los valores f(4) y f(5)
"""
def ecuacion():
    return lambda x: x**2 + 2*x - 5

f=ecuacion()

print(f(3))