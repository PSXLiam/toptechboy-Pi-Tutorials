#Imports
import RPi.GPIO as GPIO
import LCD1602
from kpLib import keypad
from time import sleep
myKeypad = keypad(retChar = 'D')
LCD1602.init(0x27, 1)

try:
    while True:
        LCD1602.write(0,0, 'Input Value:')
        myString = myKeypad.readKeypad()
        LCD1602.write(0,0, 'User Input was:')
        LCD1602.write(0,1, myString)
        sleep(5)
        LCD1602.clear()
except KeyboardInterrupt:
    sleep(.2)
    LCD.clear()
    GPIO.cleanup()
    print('GPIO Clean!')
