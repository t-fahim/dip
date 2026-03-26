# =============================================================================
# Bitwise operations are used to manipulate images pixel by pixel at the binary level. 
# They are very useful for masking, combining images, and object extraction.
# 
# | Operation | Function            |
# | --------- | ------------------- |
# | AND       | `cv2.bitwise_and()` |
# | OR        | `cv2.bitwise_or()`  |
# | XOR       | `cv2.bitwise_xor()` |
# | NOT       | `cv2.bitwise_not()` |
# NB : image dimention must be same
# =============================================================================

import cv2
import numpy as np

img1 = np.zeros((300,300,3),dtype = 'uint8')
img2 = np.zeros((300,300,3),dtype = 'uint8')


img1 = cv2.circle(img1, (150,150), 100 , (0,0,255),-1)
img2 = cv2.rectangle(img2, (100,100),(250,250),(0,0,255),-1)

# bitwisw and
bitwise_and = cv2.bitwise_and(img1, img2)

# bitwise or
bitwise_or = cv2.bitwise_or(img1, img2)

# bitwise not
bitwise_not = cv2.bitwise_not(img1)

# bitwise xor
bitwise_xor = cv2.bitwise_xor(img1, img2)

cv2.imshow('circle', img1)
cv2.imshow('rectangle', img2)
cv2.imshow('bitwise and', bitwise_and)
cv2.imshow('bitwise or', bitwise_or)
cv2.imshow('bitwise not', bitwise_not)
cv2.imshow('bitwise xor', bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()

