# =============================================================================
# Thresholding is a technique used to separate objects from the background 
# by converting a grayscale image into a binary image (black and white).
# =============================================================================
# | Parameter        | Meaning                               |
# | ---------------- | ------------------------------------- |
# | `src`            | Grayscale image                       |
# | `thresh_value`   | Threshold value                       |
# | `max_value`      | Value assigned when condition is true |
# | `threshold_type` | Type of thresholding                  |
# =============================================================================

# =============================================================================
# | Threshold Type      | OpenCV Constant         | Rule Applied                              |
# | ------------------- | ----------------------- | ----------------------------------------- |
# | **Binary**          | `cv2.THRESH_BINARY`     | pixel > thresh → maxValue, else → 0       |
# | **Binary Inverse**  | `cv2.THRESH_BINARY_INV` | pixel > thresh → 0, else → maxValue       |
# | **Truncate**        | `cv2.THRESH_TRUNC`      | pixel > thresh → thresh, else → unchanged |
# | **To Zero**         | `cv2.THRESH_TOZERO`     | pixel > thresh → unchanged, else → 0      |
# | **To Zero Inverse** | `cv2.THRESH_TOZERO_INV` | pixel > thresh → 0, else → unchanged      |
# =============================================================================


import cv2

# only gray scale image
img = cv2.imread('man.png',cv2.IMREAD_GRAYSCALE)


ret, thresh_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)


cv2.imshow('original image', img)
cv2.imshow('threshold image', thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()