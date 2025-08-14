import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
pwmPin = 4
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)


try:
    while True:
        potVal=ADC0834.getResult(0)
        DC = (10/255)*potVal+2
        if DC > 12:
            DC = 12
        if DC < 2:
            DC = 2
        pwm.ChangeDutyCycle(DC)
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')