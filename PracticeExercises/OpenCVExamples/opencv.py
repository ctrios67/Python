#! /usr/bin/env python3
import cv2
#import matplotlib.pyplot as plt

# Pass 1 for colors rgb, 0 for Grayscale image which implies image has 1 band, -1 color image but also transpency
img = cv2.imread('galaxy.jpg',0)

print(type(img))
# Below, think of this list as literally an array of the pixels in this image.
print(img)
# shape shows basically the size
print(img.shape)
# ndim shows how many dimensions we have
print(img.ndim)

# Resize the image because it is too big to fit my screen.
resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))

# Title, the imread object
cv2.imshow('Galaxy', resized_image)
cv2.imwrite('Galaxy_resized.jpg', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.imshow(img)
#plt.show()
