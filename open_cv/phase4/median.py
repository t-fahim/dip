# Median Blur is an image smoothing technique to remove noise while preserving edges.

# =============================================================================
# | Parameter     | Meaning                   |
# | ------------- | ------------------------- |
# | `image`       | Input image               |
# | `kernel_size` | Size of the filter window |
# =============================================================================


import cv2

img = cv2.imread('tree_image.jpg')

blur_img = cv2.medianBlur(img, 3) # only one value

cv2.imshow('original image', img)
cv2.imshow('blur image', blur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()