import RPi.GPIO as gp
import time
gp.setwarnings(False)
gp.cleanup()
gp.setmode(gp.BCM)
pin1=21
pin2=20
gp.setup(pin1,gp.OUT)
gp.setup(pin2,gp.OUT)
try:
     while True:
        gp.output(pin1,True)
        time.sleep(6)
        gp.output(pin1,False)
        time.sleep(6)
        gp.output(pin2,False)
        time.sleep(6)
        gp.output(pin2,True)
        time.sleep(6)
            
except KeyboardInterrupt:
    gp.cleanup()
exit()

