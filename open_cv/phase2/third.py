# rotatin image

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    (h,w) = image.shape[:2]
    center = (w//2,h//2)
    m = cv2.getRotationMatrix2D(center, -45, 1.0)
    rotated = cv2.warpAffine(image, m, (w,h))
    
    cv2.imshow('original image', image)
    cv2.imshow('rotaed image', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                        