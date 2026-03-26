# =============================================================================
# approxPolyDP() in OpenCV is used to approximate a contour shape with fewer points.
# This is based on the Douglas–Peucker algorithm.
# It is commonly used for shape detection (triangle, rectangle, polygon).
# =============================================================================

# =============================================================================
# | Parameter | Meaning                                                     |
# | --------- | ----------------------------------------------------------- |
# | `curve`   | Input contour                                               |
# | `epsilon` | Maximum distance between original contour and approximation |
# | `closed`  | True if shape is closed                                     |
# =============================================================================

# =============================================================================
# epsilon = 0.02 * cv2.arcLength(cnt, True)
# epsilon controls how much simplification happens.
# Small epsilon	Shape stays very detailed
# Large epsilon	Shape becomes simpler
# =============================================================================

import cv2

img = cv2.imread('circle.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)

# find contours
contours, heirarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,0,255),3)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
    
    corners = len(approx)
    if corners == 3:
        shape = "Triangle"
    
    elif corners == 4:
        shape = "Rectangle"
        
    elif corners == 5:
        shape = "Pentagon"
        
    elif corners == 6:
        shape = "Hexagon"
        
    elif corners > 6:
        shape = "Circle"
        
    else:
        shape = 'Unknown'
        
    cv2.drawContours(img, [approx], 0 , (0,255,0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    
    cv2.putText(img, shape, (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
    
        

cv2.imshow('contours image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
