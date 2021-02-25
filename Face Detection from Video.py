import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)
no_frames = 1
while video.isOpened() :
    no_frame = no_frames+1
    check, frame = video.read()
    if(check):
        img = cv2.resize(frame, (600, 400))
        cv2.imshow("Live Camera Video", img)
    else:
        continue
        
    key = cv2.waitKey(1)
    if key==ord('q'):
        print("Test")
        break

video.release()
cv2.destroyAllWindows()
print(no_frames)