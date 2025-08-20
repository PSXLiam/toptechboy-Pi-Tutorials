import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
buzzPin = 17
GPIO.setup(buzzPin, GPIO.OUT)
buzzPWM = GPIO.PWM(buzzPin, 400)
buzzPWM.start(50)
try:
    while True:
        for i in range(150, 2000):
            buzzPWM.ChangeFrequency(i)
            sleep(.0001)
        for i in range(2000, 150, -1):
            buzzPWM.ChangeFrequency(i)
            sleep(.0001)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')
