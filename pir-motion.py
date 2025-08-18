import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
motionPin = 18
ledPin = 21
GPIO.setup (motionPin, GPIO.IN)
GPIO.setup (ledPin, GPIO.OUT)
sleep(10)
try:
    while True:
        motion = GPIO.input(motionPin)
        print(motion)
        if motion == 1:
            GPIO.output(ledPin, 1)
        else:
            GPIO.output(ledPin, 0)
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')
    