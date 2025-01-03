import RPi.GPIO as GPIO
import time
pin1 = 18
pin2 = 23
pin3 = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
count = 0
try:
    while True:
        GPIO.output(pin1,count & 0b001)
        GPIO.output(pin2,count & 0b010)
        GPIO.output(pin3,count & 0b100)
        time.sleep(2)
        count =  count+1
        if count > 7 :
            count = 0
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

