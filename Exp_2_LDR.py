import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
LDR_PIN = 26
LIGHT_PIN1 = 16

GPIO.setup(LIGHT_PIN1,GPIO.OUT)

GPIO.setup(LDR_PIN,GPIO.IN)
while True:
    if(GPIO.input(LDR_PIN)==1):
            GPIO.output(LIGHT_PIN1,True)
           
    else:
            GPIO.output(LIGHT_PIN1,False)
             
