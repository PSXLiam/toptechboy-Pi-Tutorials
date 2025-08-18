import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
motionPin = 18
GPIO.setup (motionPin, GPIO.IN)
sleep(10)
try:
    while True:
        motion = GPIO.input(motionPin)
        print(motion)
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')
    