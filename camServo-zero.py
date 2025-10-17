import RPi.GPIO as GPIO
from camServo import set_angle
from time import sleep
GPIO.setmode(GPIO.BCM)
pwmPin = 18
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

try:
    while True:
        angle = float(input('Angle % '))
        set_angle(pwm, angle)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean!')