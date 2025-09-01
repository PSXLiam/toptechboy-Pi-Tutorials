#Imports
import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)

#Setup
ADC0834.setup()

try:
    while True:
        lightVal = ADC0834.getResult(0)
        print('Light Value: ', lightVal)
        sleep(.2)
except KeyboardInterrupt:
    sleep(.2)
    GPIO.cleanup()
    print('GPIO Clean!')