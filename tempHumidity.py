import RPi.GPIO as GPIO
import dht11
from time import sleep
GPIO.setmode(GPIO.BCM)
myDHT = dht11.DHT11(pin = 17)
try:
    while True:
        result = myDHT.read()
        if result.is_valid():
            print('Temperature is: ' ,result.temperature, 'Humidity is: ',result.humidity)
        sleep(.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')
    