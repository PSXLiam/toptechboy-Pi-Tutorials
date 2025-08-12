import RPi.GPIO as GPIO
import ADC0834
from time import sleep
dt = .2
rPin = 23
gPin = 21
bPin = 24
rDC = 0
gDC = 0
bDC = 0
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

rPWM = GPIO.PWM(rPin, 1000)
rPWM.start(rDC)
gPWM = GPIO.PWM(gPin, 1000)
gPWM.start(gDC)
bPWM = GPIO.PWM(bPin, 1000)
bPWM.start(bDC)

try:
    while True:
        rPotVal=ADC0834.getResult(0)
        rDC = (100/255)*rPotVal
        if rDC > 99:
            rDC = 99
        if rDC < 0:
            rDC = 0
        rPWM.ChangeDutyCycle(rDC)
        
        gPotVal=ADC0834.getResult(1)
        gDC = (100/255)*gPotVal
        if gDC > 99:
            gDC = 99
        if gDC < 0:
            gDC = 0
        gPWM.ChangeDutyCycle(gDC)
        
        bPotVal=ADC0834.getResult(2)
        bDC = (100/255)*bPotVal
        if bDC > 99:
            bDC = 99
        if bDC < 0:
            bDC = 0
        bPWM.ChangeDutyCycle(bDC)
        
        sleep(dt)
except KeyboardInterrupt:
    rPWM.stop()
    gPWM.stop()
    bPWM.stop()
    GPIO.cleanup()
    print('GPIO Clean!')
    