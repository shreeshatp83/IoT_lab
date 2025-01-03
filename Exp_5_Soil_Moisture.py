import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
pin1=18
pin2 = 24
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.IN)
try:
    while True:
           if(GPIO.input(pin2)==1):
              GPIO.output(pin1,False)
              print("Soil is moist!")
           else:
             GPIO.output(pin1,True)
             print("Soil is dry!, WATERING")

except KeyboardInterrupt:
    GPIO.cleanup()
exit()
