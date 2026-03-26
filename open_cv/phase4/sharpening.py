# sharpening

# -1 means: Use the same depth as the input image.

import cv2
import numpy as np

img = cv2.imread('tree_image.jpg')
kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0],
    ])

sharped_img = cv2.filter2D(img, -1, kernel)

cv2.imshow("original  image", img)
cv2.imshow("sharped image", sharped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()