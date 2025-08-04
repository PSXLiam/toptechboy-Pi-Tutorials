
import RPi.GPIO as GPIO
from time import sleep

delay = .1
b1Pin = 40
b1State = 1
b1StateOld = 1
b2Pin = 38
b2state = 1
b2StateOld = 1
LEDPin = 37
DC = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1Pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(b2Pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LEDPin, GPIO.OUT)
myPWM = GPIO.PWM(LEDPin, 100)
myPWM.start(DC)

try:
	while True:
		b1State = GPIO.input(b1Pin)
		b2State = GPIO.input(b2Pin)
		if b1StateOld == 0 and b1State == 1:
			DC=DC-10
			print("Dim")
		if b2StateOld == 0 and b2State == 1:
			DC=DC+10
			print("Bright")
		if DC > 99:
			DC = 99
			print("Max Brightness")
		if DC < 0:
			DC = 0
			print("Max Dim")
		myPWM.ChangeDutyCycle(DC)
		b1StateOld = b1State
		b2StateOld = b2State
		sleep(delay)

except KeyboardInterrupt:
	myPWM.stop()
	GPIO.cleanup()
	print("GPIO Cleaned")
