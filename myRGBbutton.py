
import RPi.GPIO as GPIO
from time import sleep

delay = .1
rPin = 37
gPin = 35
bPin = 33

rBut = 11
rButState = 1
rButStateOld = 1

gBut = 13
gButState = 1
gButStateOld = 1

bBut = 15
bButState = 1
bButStateOld = 1

rLEDState = 0
gLEDState = 0
bLEDState = 0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.setup(rBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(gBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(bBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
	while True:
		rButState = GPIO.input(rBut)
		gButState = GPIO.input(gBut)
		bButState = GPIO.input(bBut)

		if rButStateOld == 0 and rButState == 1:
			rLEDState = not rLEDState
			GPIO.output(rPin, rLEDState)
			print("RED")
		rButStateOld = rButState
		
		if gButStateOld == 0 and gButState == 1:
			gLEDState = not gLEDState
			GPIO.output(gPin, gLEDState)
			print("GREEN")
		gButStateOld = gButState
			
		if bButStateOld == 0 and bButState == 1:
			bLEDState = not bLEDState
			GPIO.output(bPin, bLEDState)
			print("BLUE")
		bButStateOld = bButState
		
		sleep(delay)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO Cleaned")
