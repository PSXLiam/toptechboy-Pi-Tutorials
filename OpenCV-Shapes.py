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
    cv2.putText(frame, str(int(fps)) + ' FPS', pos, font, height, myColor, weight)
    cv2.imshow("piCam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9*fps + .1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()
