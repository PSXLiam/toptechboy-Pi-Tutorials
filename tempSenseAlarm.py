#Imports
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

#Pins
buttonPin = 24

#Setup
GPIO.setup(buttonPin, GPIO.IN,pull_up_down = GPIO.PUD_UP)
buttonState = 1
buttonStateOld = 1
setmode = True

try:
    while True:
        #Check mode toggle
        buttonState = GPIO.input(buttonPin)
        if buttonState == 1 and buttonStateOld == 0:
            setmode = not setmode
        print(setmode)
        buttonStateOld = buttonState
        sleep(.2)
except KeyboardInterrupt:
    sleep(.2)
    GPIO.cleanup()
    print('GPIO Clean!')