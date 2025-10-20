from camServo import Servo
from time import sleep

pan = Servo()

try:
    while True:
        angle = float(input('Angle % '))
        pan.set_angle(angle)
        print (pan.get_angle())

except KeyboardInterrupt:
    pan.GPIO_Clean()
