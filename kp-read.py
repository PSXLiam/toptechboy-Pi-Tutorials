
import RPi.GPIO as GPIO
from kpLib import keypad
myPad = keypad(retChar = 'A')
myString = myPad.readKeypad()
print(myString)
GPIO.cleanup()
