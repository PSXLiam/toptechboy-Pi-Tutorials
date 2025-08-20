import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
buzzPin = 17
GPIO.setup(buzzPin, GPIO.OUT)
try:
    while True:
        GPIO.output(buzzPin, GPIO.HIGH)
        sleep(.1)
        GPIO.output(buzzPin, GPIO.LOW)
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')
    