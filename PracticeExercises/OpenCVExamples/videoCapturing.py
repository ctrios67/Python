#! /usr/bin/env python3
import cv2
import time

a=1
while True:
    a+=1
    # The different cameras available are indexed in an array. 0 for webcam, 1 for external, so on and so forth
    video = cv2.VideoCapture(0)
    check, frame = video.read()
    print(check)
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(5)
    cv2.imshow('Capturing', frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
print(a)
