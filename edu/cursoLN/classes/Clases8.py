
class Clases8():

    def __init__(self, nombre):
        self.nombre = nombre
        print("One")

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Two")

    def __init__(self, nombre, edad, titulo):
        self.nombre = nombre
        self.edad = edad
        self.titulo = titulo
        print("Three")


e1 = Clases8('luis')

e2 = Clases8('pedro', 30)

e3 = Clases8('maria', 40, 'constructor')

print(e1.nombre)
print(e2.edad)
print(e3.titulo)

