import RPi.GPIO as GPIO
import ADC0834
from time import sleep
dt = .2
redPin = 23
DC = 0
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(redPin, GPIO.OUT)

myPWM = GPIO.PWM(redPin, 1000)
myPWM.start(DC)

try:
    while True:
        potVal=ADC0834.getResult(0)
        DC = (100/255)*potVal
        if DC > 99:
            DC = 99
        if DC < 0:
            DC = 0
        myPWM.ChangeDutyCycle(DC)
        #print(potVal, DC)
        sleep(dt)
except KeyboardInterrupt:
    myPWM.stop()
    GPIO.cleanup()
    print('GPIO Clean!')
    