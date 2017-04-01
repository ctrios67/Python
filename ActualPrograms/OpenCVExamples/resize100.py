#! /usr/bin/env python3
# resize100.py - This app resizes images in a directory to 100 by 100.

import cv2
import os
import glob2

os.chdir('./sample-images/')
files = glob2.glob('*.jpg')
newFileNames = []
img_resized = []
for i in range(len(files)):
    newFileNames.append('Resized_'+ files[i])
    img_resized.append(cv2.imread(files[i],0))
    img_resized[i] = cv2.resize(img_resized[i], (100, 100))
    cv2.imwrite(newFileNames[i], img_resized[i])
    cv2.imshow(files[i], img_resized[i])
    cv2.waitKey(500)
    cv2.destroyAllWindows()
