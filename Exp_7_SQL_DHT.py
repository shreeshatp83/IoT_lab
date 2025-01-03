
import time
import datetime
import MySQLdb
import Adafruit_DHT
sensor = Adafruit_DHT.DHT22  # You can change this to DHT11 if you're using a DHT11 sensor
pin = 21  # GPIO pin number where the DHT sensor is connected
db = MySQLdb.connect(host="localhost", user="newuser", passwd="hello1", db="newDB")
cur = db.cursor()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        timenow = datetime.datetime.utcnow()
        print(f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
        cur.execute('''INSERT INTO sensorstats1 (date_time, temperature, humidity)
                       VALUES (%s, %s, %s);''', (timenow, temperature, humidity))
        db.commit()
    else:
        print("Failed to retrieve data from sensor")
    time.sleep(2)
