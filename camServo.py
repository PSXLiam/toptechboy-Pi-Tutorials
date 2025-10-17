from time import sleep

def set_angle(pwm, pwmAngle):
    pwmPercent = (-1/18)*pwmAngle+7
    if pwmPercent > 12:
        pwmPercent = 12
    if pwmPercent < 2:
        pwmPercent = 2
    pwm.ChangeDutyCycle(pwmPercent)
    sleep(.1)
