
class Carros:
    marca = ''
    velocidad = 0
    tipo = 'Sedan'

    def __init__(self, marca, tipo, velocidad):
        self.marca = marca
        self.velocidad = velocidad
        self.tipo = tipo

    def correr(self):
        pass

    def estacionar(self):
        pass


if __name__ == "__main__":
    print('Hola Luis')
