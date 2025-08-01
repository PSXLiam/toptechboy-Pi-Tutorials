
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inPin=40
outPin=38
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(outPin, GPIO.OUT)

try:
	while True:
		readVal=GPIO.input(inPin)
		print(readVal)
		if readVal == 0:
			GPIO.output(outPin, True)
		else: GPIO.output(outPin, False)
except KeyboardInterrupt:
	GPIO.cleanup()
