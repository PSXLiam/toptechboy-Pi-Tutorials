#Imports
import cv2
from picamera2 import Picamera2
import time

#TrackBar Functions
def TrackX(val):
    global xPos
    xPos = val
    print("X Position:", xPos)
    
def TrackY(val):
    global yPos
    yPos = val
    print("Y Position:", yPos)
    
def TrackW(val):
    global boxW
    boxW = val
    print("Box Width:", boxW)
    
def TrackH(val):
    global boxH
    boxH = val
    print("Box Height:", boxH)

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

#Trackbars
cv2.namedWindow("My Trackbars")
cv2.createTrackbar("X Pos", "My Trackbars", 10, dispW-1, TrackX)
cv2.createTrackbar("Y Pos", "My Trackbars", 10, dispH-1, TrackY)
cv2.createTrackbar("Box Width", "My Trackbars", 10, dispW-1, TrackW)
cv2.createTrackbar("Box Height", "My Trackbars", 10, dispH-1, TrackH)

while True:
    tStart = time.time()
    frame = piCam.capture_array()
    ROI = frame[yPos:yPos+boxH, xPos:xPos+boxW]
    cv2.putText(frame, str(int(fps)) + ' FPS', pos, font, height, myColor, weight)
    cv2.rectangle(frame,(xPos, yPos), (xPos+boxW, yPos+boxH), myColor, 2)
    cv2.imshow("piCam", frame)
    cv2.imshow("ROI", ROI)
    if cv2.waitKey(1) == ord('q'):
        break
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9*fps + .1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()
