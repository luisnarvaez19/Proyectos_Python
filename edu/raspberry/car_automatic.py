import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

obstacle = 20

class MotorControler(object):


    # Constructor
    def __init__(self, parent=None):
        self._data = {'name': 'MOTOR', 'delay': 0.01, 'LD': 3, 'LU': 5, 'RD': 7, 'RU': 8}
        self.init_pin()

    '''
        Funcion que define los pines y toma los datos del diccionario data
        Inicializa todos los pines de salida
    '''

    def init_pin(self):
        self.GPIO_LD_PIN = self._data.get('LD', -1)
        self.GPIO_LU_PIN = self._data.get('LU', -1)

        self.GPIO_RD_PIN = self._data.get('RD', -1)
        self.GPIO_RU_PIN = self._data.get('RU', -1)

        if self.GPIO_LD_PIN == -1 or self.GPIO_LU_PIN == -1 or self.GPIO_RD_PIN == -1 or self.GPIO_RU_PIN == -1:
            print('message', 'FATAL ERROR : INVALID PIN ENCOUNTER # ' + str(self.GPIO_LD_PIN) + ', ' + + str(
                self.GPIO_LU_PIN) + ', ' + + str(self.GPIO_RD_PIN) + ', ' + + str(self.GPIO_RU_PIN))

        # pin setup

        # set GPIO numbering mode and define output pins

        GPIO.setup(self.GPIO_LD_PIN, GPIO.OUT)
        GPIO.setup(self.GPIO_LU_PIN, GPIO.OUT)
        GPIO.setup(self.GPIO_RD_PIN, GPIO.OUT)
        GPIO.setup(self.GPIO_RU_PIN, GPIO.OUT)
        time.sleep(0.5)  # warmup time
        self.stop()


    def stop(self):
        GPIO.output(self.GPIO_LD_PIN, False)
        GPIO.output(self.GPIO_LU_PIN, False)
        GPIO.output(self.GPIO_RD_PIN, False)
        GPIO.output(self.GPIO_RU_PIN, False)


    def step_forward(self):
        GPIO.output(self.GPIO_LD_PIN, False)
        GPIO.output(self.GPIO_LU_PIN, True)
        GPIO.output(self.GPIO_RD_PIN, False)
        GPIO.output(self.GPIO_RU_PIN, True)
        print('Move Forward')


    def step_backward(self):
        GPIO.output(self.GPIO_LD_PIN, True)
        GPIO.output(self.GPIO_LU_PIN, False)
        GPIO.output(self.GPIO_RD_PIN, True)
        GPIO.output(self.GPIO_RU_PIN, False)
        print('Move Backward')


    def step_right(self):
        GPIO.output(self.GPIO_LD_PIN, True)
        GPIO.output(self.GPIO_LU_PIN, False)
        GPIO.output(self.GPIO_RD_PIN, False)
        GPIO.output(self.GPIO_RU_PIN, True)
        print('Move Right')


    def step_left(self):
        GPIO.output(self.GPIO_LD_PIN, False)
        GPIO.output(self.GPIO_LU_PIN, True)
        GPIO.output(self.GPIO_RD_PIN, True)
        GPIO.output(self.GPIO_RU_PIN, False)
        print('Move Left')


    def move_forward(self, count=15):
        for i in range(count):
            self.step_forward()
            self.stop()

    def move_dance(self, count=15):
        self.step_left();
        self.step_right();
        self.step_left();
        self.step_right();
        self.step_left();
        self.step_right();
        self.step_left();
        self.step_right();
        self.step_left();
        self.step_right();
        self.step_left();
        self.step_right();
        self.stop()

    def move_backward(self, count=15):
        for i in range(count):
            self.step_backward()
            self.stop()


    def move_right(self, count=15):
        for i in range(count):
            self.step_right()
            self.stop()


    def move_left(self, count=15):
        for i in range(count):
            self.step_left()
            self.stop()


    def distance():

        GPIO.output(12, False)
        time.sleep(0.5)

        GPIO.output(12, True)
        time.sleep(0.00001)
        GPIO.output(12, False)
        inicio = time.time()

        while GPIO.input(18) == 0:
            inicio = time.time()

        while GPIO.input(18) == 1:
            final = time.time()

        total = final - inicio

        distancia = total * 17150  # velocidad de la luz sobre 2

        distancia = round(distancia, 2)  # redondear numero

        print("Distancia:", distancia, "cm")  # imprimir distancia en cm

        return distancia



# FOR DEMO

    def run():

        motor = MotorControler()

        while True:

            distance = motor.distance()

            if distance > obstacle:
                motor.move_forward(count=15)
            elif np.random.ranf() > 0.5 :  #  devuelve un valor decimal entre 0 y 1
                motor.move_right(count=15)
            else:
                motor.move_left(count=15) # provide more condotion for better maneuvering


    run()

