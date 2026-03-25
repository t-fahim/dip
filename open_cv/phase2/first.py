# resizing and scaling

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    resize = cv2.resize(image, (300,300))
    scaled = cv2.resize(image, None, fx=.5,fy=1)
    cv2.imshow('original image', image)
    cv2.imshow('resize image', resize)
    cv2.imshow('scall image', scaled)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                        