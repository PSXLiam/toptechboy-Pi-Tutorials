#Imports
import RPi.GPIO as GPIO
import LCD1602
import threading
from kpLib import keypad
from time import sleep

myKeypad = keypad(retChar = 'D')
LCD1602.init(0x27, 1)

#Pins
PIRpin = 12

#Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIRpin, GPIO.IN)

#Variables
myString = ''
password = '1234'


def readKp():
    global myString
    while myString != '*':
        myString = myKeypad.readKeypad()
        sleep(.2)

readThread = threading.Thread(target = readKp,)
readThread.daemon = True
readThread.start()

while myString != '*':
    CMD = myString
    if CMD == 'A' + password:
        LCD1602.write(0,0, '   --ARMED--   ')
        moveVal = GPIO.input(PIRpin)
        if moveVal == 1:
            LCD1602.write(0,1, '  !!INTRUDER!! ')
        else:
            LCD1602.write(0,1, ' --All Clear-- ')
    if CMD == 'B' + password:
        LCD1602.write(0,0, '  --DISARMED--   ')
        LCD1602.write(0,1, '               ')
    if CMD == 'C' + password:
        LCD1602.write(0,0, 'Password?       ')
        LCD1602.write(0,1, '               ')
        while myString == 'C' + password:
            pass
        password = myString
        LCD1602.write(0,0, password + '      ')
        sleep(2)
        LCD1602.clear()
sleep(1)
GPIO.cleanup()
LCD1602.clear()
print('System Clean!')
