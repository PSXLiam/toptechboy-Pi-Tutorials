#Imports
import LCD1602
from kpLib import keypad
from time import sleep
import threading
myKeypad = keypad(retChar = 'D')
LCD1602.init(0x27, 1)
myString = ''
password = '1234'

def readKp():
    global myString
    while True:
        myString = myKeypad.readKeypad()
        sleep(.2)

readThread = threading.Thread(target = readKp,)
readThread.daemon = True
readThread.start()

while True:
    CMD = myString
    if CMD == 'A' + password:
        LCD1602.write(0,0, '   --ARMED--   ')
    if CMD == 'B' + password:
        LCD1602.write(0,0, '  --DISARMED--   ')
    if CMD == 'C' + password:
        LCD1602.write(0,0, 'Password?       ')
        while myString == 'C' + password:
            pass
        password = myString
        LCD1602.write(0,0, password + '      ')
        sleep(2)
        LCD1602.clear()
        