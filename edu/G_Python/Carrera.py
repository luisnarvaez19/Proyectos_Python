from com.G_Python.Carros import Carros


class Carrera:
    participantes = []

    def crearParticipantes(self):
        opcion = 1
        opcion = int(input('Introduzca su opcion: '))
        while opcion != 0:
            if opcion == 1:
                marca = input('Que marca es el carro: ')
                velocidad = int(input('Diga la velocidad maxima: '))
                tipo = input('Diga el tipo del carro: ')
                carro = Carros(marca, tipo, velocidad)
                self.participantes.append(carro)
            opcion = int(input('Introduzca su opcion: '))

    # Devolucion de lista de objetos
    # En este caso una lista de Carros (que son objetos de la clase Carro)
    def mostrarParticipantes(self):
        return self.participantes

    def imprimirParticipantes(self):
        for i in self.participantes:
            print(i.marca)


if __name__ == "__main__":
    carrera1 = Carrera()
    carrera1.crearParticipantes()
    lista = carrera1.mostrarParticipantes()
    # for i in lista:
    #    print(i.marca)
    carrera1.imprimirParticipantes()
