#Imports
import cv2
import numpy as np
from picamera2 import Picamera2
import time

#TrackBar Functions
def onTrack1(val):
    global hueLow
    hueLow = val
    print("Hue Low:", hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh = val
    print("Hue High:", hueHigh)
    
def onTrack3(val):
    global satLow
    satLow = val
    print("Saturation Low:", satLow)

def onTrack4(val):
    global satHigh
    satHigh = val
    print("Saturation High:", satHigh)
    
def onTrack5(val):
    global valLow
    valLow = val
    print("Value Low:", valLow)

def onTrack6(val):
    global valHigh
    valHigh = val
    print("Value High:", valHigh)

#Variables
dispW = 640
dispH = 360
fps = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.0
myColor = (0, 0, 255)
weight = 3

hueLow = 1
hueHigh = 25
satLow = 85
satHigh = 255
valLow = 50
valHigh = 255

#Camera Setup
piCam = Picamera2()
piCam.preview_configuration.main.size = (dispW, dispH)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate = 30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

#Trackbars
cv2.namedWindow("My Tracker")
cv2.createTrackbar("Hue Low", "My Tracker", 1, 179, onTrack1)
cv2.createTrackbar("Hue High", "My Tracker", 25, 179, onTrack2)
cv2.createTrackbar("Saturation Low", "My Tracker", 80, 255, onTrack3)
cv2.createTrackbar("Saturation High", "My Tracker", 255, 255, onTrack4)
cv2.createTrackbar("Value Low", "My Tracker", 50, 255, onTrack5)
cv2.createTrackbar("Value High", "My Tracker", 255, 255, onTrack6)

while True:
    tStart = time.time()
    frame = piCam.capture_array()
    
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    myMaskSmall = cv2.resize(myMask, (int(dispW/2),int(dispH/2)))
    objectOfInterest = cv2.bitwise_and(frame, frame, mask = myMask)
    objectOfInterestSmall = cv2.resize(objectOfInterest, (int(dispW/2),int(dispH/2)))
    #print(frameHSV [int(dispH/2), int(dispW/2)])
    
    contours, junk = cv2.findContours(myMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        contours = sorted(contours, key = lambda x:cv2.contourArea(x), reverse = True)
        cv2.drawContours(frame, contours, 0, (255,0,0),3)
        contour = contours[0]
        boxX, boxY, boxW, boxH = cv2.boundingRect(contour)
        cv2.rectangle(frame, (boxX, boxY), (boxX+boxW, boxY+boxH), (0, 0, 255), 3)
    
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
