#Imports
import cv2
import numpy as np
from picamera2 import Picamera2
import time

#Variables
dispW = 640
dispH = 360
fps = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.0
myColor = (0, 0, 255)
weight = 3
hueLow = 15
hueHigh = 25
satLow = 120
satHigh = 255
valLow = 120
valHigh = 255

lowerBound = np.array([hueLow, satLow, valLow])
upperBound = np.array([hueHigh, satHigh, valHigh])

#Camera Setup
piCam = Picamera2()
piCam.preview_configuration.main.size = (dispW, dispH)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate = 30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

while True:
    tStart = time.time()
    frame = piCam.capture_array()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    myMaskSmall = cv2.resize(myMask, (int(dispW/2),int(dispH/2)))
    objectOfInterest = cv2.bitwise_and(frame, frame, mask = myMask)
    objectOfInterestSmall = cv2.resize(objectOfInterest, (int(dispW/2),int(dispH/2)))
    #print(frameHSV [int(dispH/2), int(dispW/2)])
    cv2.putText(frame, str(int(fps)) + ' FPS', pos, font, height, myColor, weight)
    cv2.imshow("piCam", frame)
    cv2.imshow("My Mask", myMaskSmall)
    cv2.imshow("Object of Interest", objectOfInterestSmall)
    if cv2.waitKey(1) == ord('q'):
        break
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9*fps + .1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()
