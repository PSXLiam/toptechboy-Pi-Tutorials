
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inPin=40
outPin=11
GPIO.setup(inPin, GPIO.IN)
GPIO.setup(outPin, GPIO.OUT)
from time import sleep
try:
	while True:
		readVal=GPIO.input(inPin)
		print(readVal)
		if readVal == 1:
			GPIO.output(outPin, True)
		else: GPIO.output(outPin, False)
		sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
