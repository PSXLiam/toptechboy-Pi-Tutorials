
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

gLEDState = 0
bLEDState = 0

rDC = .9
gDC = .9
bDC = .9

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.setup(rBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(gBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(bBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)

rPWM = GPIO.PWM(rPin, 100)
rPWM.start(int(rDC))
gPWM = GPIO.PWM(gPin, 100)
gPWM.start(int(gDC))
bPWM = GPIO.PWM(bPin, 100)
bPWM.start(int(bDC))

try:
	while True:
		rButState = GPIO.input(rBut)
		gButState = GPIO.input(gBut)
		bButState = GPIO.input(bBut)

		if rButStateOld == 0 and rButState == 1:
			rDC = rDC * 1.58
			print("RED ", rDC)
			if rDC > 99:
				rDC = .9
			rPWM.ChangeDutyCycle(int(rDC))
		rButStateOld = rButState
		
		if gButStateOld == 0 and gButState == 1:
			gDC = gDC * 1.58
			print("GREEN ", gDC)
			if gDC > 99:
				gDC = .9
			gPWM.ChangeDutyCycle(int(gDC))
		gButStateOld = gButState
		
		if bButStateOld == 0 and bButState == 1:
			bDC = bDC * 1.58
			print("BLUE ", bDC)
			if bDC > 99:
				bDC = .9
			bPWM.ChangeDutyCycle(int(bDC))
		bButStateOld = bButState
		
		sleep(delay)

except KeyboardInterrupt:
	rPWM.stop()
	gPWM.stop()
	bPWM.stop()
	GPIO.cleanup()
	print("GPIO Cleaned")
