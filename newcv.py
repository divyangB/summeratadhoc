#!/usr/bin/python3

#loading opencv module

import cv2

#to create blank image
import numpy as np

#img= np.zeroes((512,512))
img= np.zeros((512,512,3))

print(img)
print(img.shape)

#display
cv2.imshow('myownimage',img)
cv2.waitkey(0)

#to destryo one named window
#cv2.destroyWindows('myownimage')
cv2.destroyAllWindows()
