#importar libreria GPIO
#importar libreria curses, para el control del teclado

'''
    Control Key

    Ya mueve el carro con las letras


    1. Medir la distancia con el sensor HC-SR04
    2. El raspberry detecta si encuentra un obstaculo y parar (autonomo)
    3. El raspberry  que se pare o retroceda (Manejo de prioridades)

'''
import RPi.GPIO as GPIO
import time
import curses


#declarar los pines GPIO como salida

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

GPIO.setup(11, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)

GPIO.setup(15, GPIO.OUT)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak
stdscr.keypad(True)

#niciamos bucle

try: 
   
    while True:
        char = stdscr.getch()
        #print letra
        if char == ord ('q'):
           break

        elif char == 97:   # codigo ASCII
            print ("adelante")
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)

        elif char == 115:
            print ("atras")
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, False)

        elif char == 100:
            print ("izquerda")
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(7, False)

        elif char == 102:
            print ("derecha")
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)

        
        else:
            print ("detener")
            GPIO.output(7, False)
            GPIO.output(11, False) 
            GPIO.output(13, False)
            GPIO.output(15, False)

finally:

   #Close down curses propely, inc turn echo back on!
   curses.nocbreak(); stdscr.keypad(0) ; curses.echo(0)
   GPIO.cleanup()


