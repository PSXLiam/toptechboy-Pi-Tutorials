
import RPi.GPIO as GPIO
import time
cont='Y'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while cont=='Y':
	numBlinks = int(input("How Many Blinks?: "))
	for i in range (0, numBlinks):
		GPIO.output(11, True)
		time.sleep(1)
		GPIO.output(11, False)
		time.sleep(1)
	cont=input("Do You Want to Continue? (Y for Yes) ")
GPIO.cleanup()
