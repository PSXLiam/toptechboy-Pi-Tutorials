#Imports
import cv2
from picamera2 import Picamera2
import time

piCam = Picamera2()
piCam.preview_configuration.main.size = (640, 360)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate = 30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()
fps = 0

while True:
    tStart = time.time()
    frame = piCam.capture_array()
    cv2.imshow("piCam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9*fps + .1*(1/loopTime)
    print(int(fps))
cv2.destroyAllWindows()
