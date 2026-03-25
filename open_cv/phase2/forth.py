# fliping image 
# 0 - top to bottom
# 1 - left to right
# -1 - both

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    
    # flip horizontal
    flip_h = cv2.flip(image, 1)
    
    # flip vertica;
    flip_v = cv2.flip(image, 0)
    
    # flip both
    flip_b = cv2.flip(image, -1)
    
    cv2.imshow('original image', image)
    cv2.imshow('horizontal flip image', flip_h)
    cv2.imshow('vertical flip image', flip_v)
    cv2.imshow('both flip image', flip_b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                        