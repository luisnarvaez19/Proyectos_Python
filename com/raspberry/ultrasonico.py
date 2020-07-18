import RPi.GPIO as GPIO  #importar libreria GPIO
import time

'''
    Ultrasonico:
    
    Calcula la distancia dado un objeto
    
    
'''
#declarar las pines que se van a usar

trigger= 12  #pin output      
echo= 18     #pin input

#definir los pines GPIO como entrada y salida

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

#bucle infinito 
           
try: 

  while True:

   GPIO.output(12, False)
   time.sleep(0.5)

   GPIO.output(12, True)
   time.sleep(0.00001) 
   GPIO.output(12, False)
   inicio= time.time()

   while GPIO.input(18)==0:
       inicio=time.time()

   while GPIO.input(18)==1:
        final=time.time()

   total= final - inicio

   distancia= total*17150 #velocidad de la luz sobre 2 

   distancia= round(distancia, 2) #redondear numero

   print ("Distancia:", distancia, "cm") #imprimir distancia en cm

except KeyboardInterrupt:     #parar el bucle, con el teclado
  GPIO.cleanup()  #limpiar puertos GPIO
