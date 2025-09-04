class keypad:
    def __init__(self, rows = [11,13,15,29], columns = [31,33,35,37], keyLabels = [[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['+',0,'#','D']], retChar='D'):
        import RPi.GPIO as GPIO
        self.rows = rows
        self.columns = columns
        self.keyLabels = keyLabels
        self.retChar = retChar
        GPIO.setmode(GPIO.BOARD)
        for i in rows:
            GPIO.setup(i, GPIO.OUT)
        for j in columns:
            GPIO.setup(j, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

import RPi.GPIO as GPIO
myPad = keypad()
GPIO.cleanup()
