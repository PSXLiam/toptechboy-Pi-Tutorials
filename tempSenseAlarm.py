#Imports
import RPi.GPIO as GPIO
import ADC0834
import LCD1602
import dht11
from time import sleep
GPIO.setmode(GPIO.BCM)

#Pins
buttonPin = 24
tempPin = 26
buzzPin = 22

#Setup
myDHT = dht11.DHT11(pin = tempPin)
GPIO.setup(buzzPin, GPIO.OUT)
GPIO.output(buzzPin, GPIO.HIGH)
ADC0834.setup()
LCD1602.init(0x27, 1)

GPIO.setup(buttonPin, GPIO.IN,pull_up_down = GPIO.PUD_UP)
buttonState = 1
buttonStateOld = 1
setMode = True

try:
    while True:
        #Check mode toggle
        buttonState = GPIO.input(buttonPin)
        if buttonState == 1 and buttonStateOld == 0:
            setMode = not setMode
        #print(setmode)
        buttonStateOld = buttonState
        sleep(.2)
        if setMode == True: #Programming Mode
            analogVal = ADC0834.getResult()
            buzzVal = int(analogVal*(100/255))
            LCD1602.write(0,0, 'Set Trip Temp:')
            LCD1602.write(0,1, str(buzzVal))
            sleep(0.25)
            LCD1602.clear()
            GPIO.output(buzzPin, GPIO.HIGH)                
        if setMode == False: #Monitoring mode
            pass
            
except KeyboardInterrupt:
    sleep(.2)
    GPIO.cleanup()
    print('GPIO Clean!')