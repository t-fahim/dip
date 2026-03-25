# cropping

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    croped_img = image[100:200, 50:150]
    cv2.imshow('original image', image)
    cv2.imshow('croped image', croped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                        