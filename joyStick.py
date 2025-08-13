import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
buttonPin = 21
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
    while True:
        analogValX = ADC0834.getResult(0)
        sleep(.1)
        analogValY = ADC0834.getResult(1)
        buttonState = GPIO.input(buttonPin)
        print('X Value: ', analogValX, 'Y Value: ', analogValY, 'Button: ', buttonState)
        sleep(.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')