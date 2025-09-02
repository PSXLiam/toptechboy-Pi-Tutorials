#Imports
import RPi.GPIO as GPIO
import ADC0834
from time import sleep

#Pins
motionPin = 23
buzzPin = 22

#Variables
Dark = 50

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
GPIO.output(buzzPin, GPIO.HIGH)
GPIO.setup(motionPin, GPIO.IN)
ADC0834.setup()
sleep(2)

try:
    while True:
        motion = GPIO.input(motionPin)
        lightVal = ADC0834.getResult(0)
        print('Light Value: ', lightVal, 'Motion: ', motion)
        sleep(.2)
        if motion == 1 and lightVal <= Dark:
            GPIO.output(buzzPin, GPIO.LOW)
            print('INTRUDER ALERT!')
        else:
            print('All Clear')
            GPIO.output(buzzPin, GPIO.HIGH)
except KeyboardInterrupt:
    sleep(.2)
    GPIO.cleanup()
    print('GPIO Clean!')
