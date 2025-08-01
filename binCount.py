
import RPi.GPIO as GPIO
import time
pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

i = 0
GPIO.output(11, 0)
GPIO.output(13, 0)
GPIO.output(15, 0)
time.sleep(1)
while i <= 7:
	if i%2  > 0:
		GPIO.output(11, True)
	else: GPIO.output(11, False)

	if i%4  > 1:
		GPIO.output(13, True)
	else: GPIO.output(13, False)

	if i%8  > 3:
		GPIO.output(15, True)
	else: GPIO.output(15, False)
	time.sleep(1)
	i = i+1
GPIO.cleanup()
