import http.client
import urllib.parse
import time
import board
import adafruit_dht
import psutil

key = "DMW39YEA9GXU9D5D"

# Kill any existing processes
for proc in psutil.process_iter():
    if proc.name() in ['libgpiod_pulsein', 'libgpiod_pulsei']:
        proc.kill()

sensor = adafruit_dht.DHT11(board.D23)
def thermometer():
    while True:
        try:
            temp = sensor.temperature
            humidity = sensor.humidity
            
            if temp is not None and humidity is not None:
                params = urllib.parse.urlencode({
                    'field1': str(temp),
                    'field2': str(humidity),
                    'key': key
                })
                
                print("Sending data:", params)  # Debug output

                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "text/plain"
                }
                conn = http.client.HTTPConnection("api.thingspeak.com", 80)
                
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                
                print("Temperature: {} °C, Humidity: {} %".format(temp, humidity))
                print(response.status, response.reason)
                data = response.read()
                conn.close()
            else:
                print("Failed to read from sensor.")
        except Exception as e:
            print("Connection failed:", e)

        time.sleep(1)  # Delay between readings
        
if __name__ == "__main__":
    thermometer()

