import curses
import RPi.GPIO as GPIO

class MotorControler(object):
    def __init__(self, parent=None):

        self._data = {'name': 'MOTOR', 'delay': 0.01, 'LD': 3, 'LU': 5, 'RD': 7, 'RU': 8}

        self.init_pin()

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

			
			
#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
motor = MotorControler()
try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
				motor.move_forward(count=15)
               
            elif char == curses.KEY_DOWN:
                motor.move_backward(count=15)
            elif char == curses.KEY_RIGHT:
                motor.move_right(count=15)
            elif char == curses.KEY_LEFT:
                motor.move_left(count=15)
            elif char == 10:
                motor.stop()
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
