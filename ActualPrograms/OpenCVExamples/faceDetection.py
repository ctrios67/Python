#! /usr/bin/env python3
# faceDetection.py - This application detects
import cv2

face_cascade = cv2.CascadeClassifier('Files/haarcascade_frontalface_default.xml')

# Greyscale face detection is much more accurate otherwise you'd get random crap
img = cv2.imread('Files/photo.jpg')
img2 = cv2.imread('Files/news.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Smaller scale factor increases accuracy, but at the cost of more processing/time
# These are generally accepted accurate numbers.
faces1 = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
faces2 = face_cascade.detectMultiScale(gray_img2, scaleFactor=1.1, minNeighbors=5)

print(type(faces1))
print(faces1)


for x, y, w, h in faces1:
    # So here, 1.) Is the image, 2.) The start point of the rect,
    # 3.) The end point of the rect, 4.) The BGR value of the rect
    # 5.) The width of the rectangle line
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)

for x, y, w, h in faces2:
    img2 = cv2.rectangle(img2, (x,y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow('Aqui Esta Una Cara', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('Aqui Esta Una Otra Cara Linda SOMEHOWO', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
