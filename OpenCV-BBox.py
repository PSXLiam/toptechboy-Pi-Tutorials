#Imports
import cv2
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

#Box Variables
boxW = 250
boxH = 125
tlC = 50			#top left Column
tlR = 75			#top left Row
lrC = tlC + boxW	#lower right Column
lrR = tlR + boxH	#lower right Row
deltaC = 2
deltaR = 2
thickness = -1
rColor = (255, 0, 0)

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
    #Check if at edges
    if tlC + deltaC < 0 or lrC + deltaC > dispW-1:
        deltaC = deltaC*(-1)
    if tlR + deltaR < 0 or lrR + deltaR > dispH-1:
        deltaR = deltaR*(-1)
    #Move the Box
    tlC = tlC + deltaC
    tlR = tlR + deltaR
    lrC = lrC + deltaC
    lrR = lrR + deltaR
    cv2.rectangle(frame, (tlC, tlR), (lrC, lrR), rColor, thickness)
    cv2.putText(frame, str(int(fps)) + ' FPS', pos, font, height, myColor, weight)
    cv2.imshow("piCam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9*fps + .1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()
