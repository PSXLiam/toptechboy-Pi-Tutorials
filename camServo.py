import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

class Servo():
    
    def __init__(self, min_angle=-90, max_angle=90):

        self.pwm = GPIO.PWM(18, 50)
        self.pwm.start(0)
        self.angle = 0
        self.min_angle = min_angle
        self.max_angle = max_angle
        
    def pwm_on(self):
        self.pwm.start(0)
        
    def pwm_off(self):
        self.pwm.stop()

    def set_angle(self, pwmAngle):
        self.angle =  pwmAngle
        pwmPercent = (-1/18)*pwmAngle+7
        if pwmPercent > 12:
            pwmPercent = 12
        if pwmPercent < 2:
            pwmPercent = 2
        self.pwm.ChangeDutyCycle(pwmPercent)
        sleep(.1)
        
    def get_angle(self):
        return self.angle
    
    def GPIO_Clean(self):
        GPIO.cleanup()
        print('GPIO Clean!')
