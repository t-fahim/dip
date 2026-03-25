# circle drawing
# color – Line color in BGR format (Blue, Green, Red)
# thickness – Thickness of the line in pixels (use -1 to fill)
# center → center coordinates (x, y)
# radius → circle radius in pixels

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    center = (200,300)
    color = (0,0,255)
    thickness = 5
    cv2.circle(image,center,100,color,thickness)
    cv2.imshow("circle image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    