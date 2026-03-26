# =============================================================================
# Canny Edge Detection is one of the most widely used edge-detection algorithms in computer vision.
# use to detect sharp changes in intensity, which correspond to edges of objects.
# 
# | Parameter    | Meaning                         |
# | ------------ | ------------------------------- |
# | `image`      | Input image (usually grayscale) |
# | `threshold1` | Lower threshold                 |
# | `threshold2` | Upper threshold                 |
# =============================================================================

import cv2

# only gray scale image
img = cv2.imread('flower.png',cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(img, 50, 150)


cv2.imshow('original image', img)
cv2.imshow('edges image', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()