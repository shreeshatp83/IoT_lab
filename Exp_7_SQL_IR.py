import time
import datetime
import csv
import MySQLdb
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
pin =21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

db = MySQLdb.connect(host="localhost",user="exampleeuser",passwd="pimylifeup",db="exampleedb")
cur = db.cursor()
while True:
    degrees = GPIO.input(pin)
    timenow= datetime.datetime.utcnow()
    print(degrees)
    cur.execute('''INSERT INTO Sensorstats(date_time,irsensorstat)VALUES(%s,%s);''',(timenow,degrees));
    db.commit()
    time.sleep(1)


