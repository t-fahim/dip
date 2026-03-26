# Gaussian Blur is a smoothing technique used to reduce noise and detail in an image.

# =============================================================================
# | Parameter                       | Meaning                            |
# | ------------------------------- | ---------------------------------- |
# | `image`                         | Input image                        |
# | `(kernel_width, kernel_height)` | Size of the blur kernel            |
# | `sigma`                         | Standard deviation of the Gaussian |
# =============================================================================

# =============================================================================
# | Sigma Value    | Effect           |
# | -------------- | ---------------- |
# | Small σ (0–1)  | Very light blur  |
# | Medium σ (2–5) | Normal smoothing |
# | Large σ (>5)   | Strong blur      |
# =============================================================================

import cv2

img = cv2.imread('tree_image.jpg')

blur_img = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow('original image', img)
cv2.imshow('blur image', blur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()