#Imports
import cv2
from picamera2 import Picamera2
import time
from camServo import Servo

#Variables
dispW = 640
dispH = 360
fps = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.0
myColor = (0, 0, 255)
weight = 3

#Camera Setup
piCam = Picamera2()
piCam.preview_configuration.main.size = (dispW, dispH)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate = 30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

#Face Models
faceCascade = cv2.CascadeClassifier('./haar/haarcascade_frontalface_default.xml')
#eyeCascade = cv2.CascadeClassifier('./haar/haarcascade_eye.xml')

#Servo Setup
pan = Servo()
panAngle = 0
pan.set_angle(panAngle)

while True:
    tStart = time.time()
    frame = piCam.capture_array()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)
    pan.pwm_off()
    if len(faces) == 0 and panAngle != 0:
        pan.pwm_on()
        panAngle = 0
        pan.set_angle(panAngle)
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0), 3)
        pan.pwm_on()
        error = (x + w/2) - (dispW/2)
        panAngle = panAngle + error/70
        if panAngle > 90:
            panAngle = 90
        if panAngle < -90:
            panAngle = -90
        if abs(error) > 35:
            pan.set_angle(panAngle)
            pan.pwm_off()
#         roiColor = frame[y:y+h, x:x+w]
#         roiGray = frameGray[y:y+h, x:x+w]q
#         eyes = eyeCascade.detectMultiScale(roiGray, 1.3, 5)
#         for eye in eyes:
#             x, y, w, h = eye
#             cv2.rectangle(roiColor, (x,y),(x+w, y+h), (0,255,0), 3)
        
    cv2.putText(frame, str(int(fps)) + ' FPS', pos, font, height, myColor, weight)
    cv2.imshow("piCam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9*fps + .1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()
