#! /usr/bin/env python3
import cv2
import time

first_frame = None

# iterating through the current frame
while True:
    # The different cameras available are indexed in an array. 0 for webcam, 1 for external, so on and so forth
    video = cv2.VideoCapture(0)
    check, frame = video.read()
    # Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blurring:Smooths and blurs the image for more accuracy
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    # Finding the delta frame, difference between the "background" and current image
    delta_frame = cv2.absdiff(first_frame, gray)
    # Apply the threshold, the black and white image
    thresh_frame = cv2.threshold(delta_frame, 30, 25, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # Find the countours, check the area, and draw the countours
    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Filter out the smaller contours
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow('Gray Frame', frame)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)
    cv2.imshow('Color Frame', frame)
    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
