# =============================================================================
# Finding contours in OpenCV is used to detect the boundaries of objects in an image.
# A contour is simply a curve joining all continuous points having the
# same intensity (usually the boundary of an object).
# 
# NB : binary image needed
# 
# | Parameter | Meaning                                                  |
# | --------- | -------------------------------------------------------- |
# | `image`   | Binary image (usually after threshold or edge detection) |
# | `mode`    | Contour retrieval mode                                   |
# | `method`  | Contour approximation method                             |
# 
# | Mode                | Meaning             |
# | ------------------- | ------------------- |
# | `cv2.RETR_EXTERNAL` | only outer contours |
# | `cv2.RETR_LIST`     | all contours        |
# | `cv2.RETR_TREE`     | full hierarchy      |
# | `cv2.RETR_CCOMP`    | two-level hierarchy |
# 
# | Method                    | Meaning                  |
# | ------------------------- | ------------------------ |
# | `cv2.CHAIN_APPROX_NONE`   | store all contour points |
# | `cv2.CHAIN_APPROX_SIMPLE` | compress points          |
# =============================================================================

# =============================================================================
#                              draw contour
# | Parameter       | Meaning                            
# | --------------- | ---------------------------------- 
# | `image`         | Image where contours will be drawn 
# | `contours`      | List of detected contours          
# | `contour_index` | Which contour to draw (-1 means draw every contour found)            
# | `color`         | Contour color (BGR)                
# | `thickness`     | Line thickness                     
# =============================================================================


import cv2

img = cv2.imread('shape.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)

# find contours
contours, heirarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, 1, (0,0,255),3)

cv2.imshow('contours image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()










