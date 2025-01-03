import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
LDR_PIN = 26
LIGHT_PIN1 = 16
LIGHT_PIN2 = 20
LIGHT_PIN3 = 21
GPIO.setup(LIGHT_PIN1,GPIO.OUT)
GPIO.setup(LIGHT_PIN2,GPIO.OUT)
GPIO.setup(LIGHT_PIN3,GPIO.OUT)
GPIO.setup(LDR_PIN,GPIO.IN)
while True:
    if(GPIO.input(LDR_PIN)==1):
            GPIO.output(LIGHT_PIN1,True)
            GPIO.output(LIGHT_PIN2,True)
            GPIO.output(LIGHT_PIN3,True)
        
            
    else:
            GPIO.output(LIGHT_PIN1,False)
            GPIO.output(LIGHT_PIN2,False)
            GPIO.output(LIGHT_PIN3,False)

