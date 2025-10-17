import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
pwmPin = 18
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

def camServo():
    pwmAngle = float(input('Angle % '))
    pwmPercent = (-1/18)*pwmAngle+7
    if pwmPercent > 12:
        pwmPercent = 12
    if pwmPercent < 2:
        pwmPercent = 2
    pwm.ChangeDutyCycle(pwmPercent)
    sleep(.1)


try:
    while True:
        camServo()
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')