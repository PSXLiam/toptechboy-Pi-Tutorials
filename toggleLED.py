
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inPin=40
outPin=38
ledState=0
buttonState=1
buttonOld=1
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(outPin, GPIO.OUT)

try:
	while True:
		buttonState=GPIO.input(inPin)
		if buttonState == 0 and buttonOld==1:
			ledState= not ledState
			GPIO.output(outPin,ledState)
		buttonOld=buttonState
		sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
	print('GPIO Clean!')
